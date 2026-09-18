#!/usr/bin/env python3
"""Dependency-free static SEO/link audit. Run: python tools/seo_audit.py [site-root].
Checks published HTML only; does not claim live HTTPS, indexing or rich-result eligibility.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin
from collections import Counter
import json
import sys
import xml.etree.ElementTree as ET

HOST = 'https://organexa.com.tr'
REQUIRED = {'/', '/features/', '/for-pianists/', '/for-djs/', '/for-event-companies/',
            '/event-management/', '/customer-management/', '/payment-tracking/',
            '/whatsapp-reminders/', '/backup-and-restore/', '/privacy/', '/terms/', '/contact/'}
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Page(HTMLParser):
    def __init__(self, path, url):
        super().__init__(convert_charrefs=True)
        self.path, self.url = path, url
        self.meta, self.links, self.images, self.ids = {}, [], [], set()
        self.canonicals, self.titles, self.h1s, self.ld = [], [], [], []
        self.stack, self.problems, self.crumbs, self.faq, self.text = [], [], [], [], []
        self.title = self.heading = self.json_buffer = self.question = self.answer = None
        self.in_breadcrumb = False
        self.crumb = None
        self.in_details = False
        self.lang = ''
        self.last_heading = 0
        self.counts = Counter()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.counts[tag] += 1
        if tag not in VOID: self.stack.append(tag)
        if tag == 'html': self.lang = a.get('lang', '')
        if 'id' in a:
            if a['id'] in self.ids: self.problems.append('duplicate id: '+a['id'])
            self.ids.add(a['id'])
        if tag == 'title': self.title = ''
        if tag in {'h1','h2','h3','h4','h5','h6'}:
            level = int(tag[1])
            if level > self.last_heading + 1: self.problems.append('skipped heading level: '+tag)
            self.last_heading = level
            if tag == 'h1': self.heading = ''
        if tag == 'meta':
            key = a.get('name', a.get('property', ''))
            if key:
                if key in self.meta: self.problems.append('duplicate metadata: '+key)
                self.meta[key] = a.get('content','')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href',''))
        for key in ('href','src'):
            if key in a: self.links.append((tag, a[key]))
        if tag == 'img': self.images.append(a)
        if tag == 'script' and a.get('type') == 'application/ld+json': self.json_buffer = ''
        if tag == 'nav' and a.get('aria-label') == 'İçerik yolu': self.in_breadcrumb = True
        if self.in_breadcrumb and tag == 'a': self.crumb = [a.get('href',''),'']
        if tag == 'details': self.in_details = True; self.question = ''; self.answer = ''
        if tag == 'p' and self.in_details: self.answer = ''

    def handle_data(self, text):
        self.text.append(text)
        if self.title is not None: self.title += text
        if self.heading is not None: self.heading += text
        if self.json_buffer is not None: self.json_buffer += text
        if self.crumb is not None: self.crumb[1] += text
        if self.in_details and 'summary' in self.stack: self.question += text
        elif self.in_details and 'p' in self.stack: self.answer += text

    def handle_endtag(self, tag):
        if tag not in VOID:
            if not self.stack or self.stack[-1] != tag: self.problems.append('unbalanced HTML near </'+tag+'>')
            if tag in self.stack:
                while self.stack.pop() != tag: pass
        if tag == 'title': self.titles.append(self.title.strip()); self.title = None
        if tag == 'h1': self.h1s.append(self.heading.strip()); self.heading = None
        if tag == 'script' and self.json_buffer is not None:
            try: self.ld.append(json.loads(self.json_buffer))
            except ValueError: self.problems.append('invalid JSON-LD')
            self.json_buffer = None
        if tag == 'a' and self.crumb is not None: self.crumbs.append(self.crumb); self.crumb = None
        if tag == 'nav': self.in_breadcrumb = False
        if tag == 'details': self.faq.append((self.question.strip(),self.answer.strip())); self.in_details = False


def walk(value):
    if isinstance(value,dict):
        yield value
        for item in value.values(): yield from walk(item)
    elif isinstance(value,list):
        for item in value: yield from walk(item)


def audit(root):
    errors, warnings, pages, broken = [], [], {}, 0
    def error(page, message): errors.append(f'{page}: {message}')
    for path in sorted(root.rglob('*.html')):
        rel = path.relative_to(root)
        if any(part.startswith('.') or part in {'node_modules','tools','docs'} for part in rel.parts): continue
        url = '/' + rel.as_posix()
        if url.endswith('index.html'): url = url[:-10]
        page = Page(path,url)
        page.feed(path.read_text(encoding='utf-8-sig'))
        page.close()
        if page.stack: page.problems.append('unclosed tags: '+str(page.stack))
        pages[url] = page
    if not pages: error('site','no HTML pages found')
    if not REQUIRED.issubset(pages): error('site','missing required pages: '+str(REQUIRED-set(pages)))
    indexable = {u for u,p in pages.items() if 'noindex' not in p.meta.get('robots','').lower()}
    seen_titles, seen_descriptions, graph = {}, {}, {u:set() for u in pages}
    for url,p in pages.items():
        for message in p.problems: error(url,message)
        if p.lang != 'tr': error(url,'expected lang=tr')
        if len(p.h1s) != 1 or not p.h1s[0]: error(url,'expected one nonempty H1')
        if len(p.titles) != 1 or not p.titles[0]: error(url,'expected one nonempty title')
        title = p.titles[0] if p.titles else ''
        desc = p.meta.get('description','')
        if not desc: error(url,'missing description')
        for value,seen,label in [(title,seen_titles,'title'),(desc,seen_descriptions,'description')]:
            if value in seen: error(url,f'duplicate {label} with {seen[value]}')
            seen[value] = url
        if title and not 40 <= len(title) <= 65: warnings.append(f'{url}: natural title length {len(title)}')
        if desc and not 120 <= len(desc) <= 170: warnings.append(f'{url}: natural description length {len(desc)}')
        if p.canonicals != [HOST+url]: error(url,'canonical must be unique, self-referencing and HTTPS/non-www')
        for key in ['og:type','og:title','og:description','og:url','og:image','og:image:alt','og:site_name','og:locale','twitter:card','twitter:title','twitter:description','twitter:image']:
            if not p.meta.get(key): error(url,'missing '+key)
        for key,wanted in {'og:title':title,'og:description':desc,'og:url':HOST+url,'twitter:title':title,'twitter:description':desc,'twitter:card':'summary_large_image','og:locale':'tr_TR'}.items():
            if p.meta.get(key) != wanted: error(url,'inconsistent '+key)
        if p.counts['main'] != 1 or not p.counts['header'] or not p.counts['footer']: error(url,'missing semantic landmarks')
        if ('a','#main') not in p.links: error(url,'missing skip link')
        if url != '/404.html' and url not in indexable: error(url,'unexpected noindex')
        if url == '/404.html' and url in indexable: error(url,'404 must be noindex')
        for image in p.images:
            if 'alt' not in image: error(url,'image missing alt')
            for size in ('width','height'):
                if not image.get(size,'').isdigit() or int(image[size])<1: error(url,'image missing explicit '+size)
        for tag,link in p.links + [('meta',p.meta.get('og:image','')),('meta',p.meta.get('twitter:image',''))]:
            u = urlsplit(urljoin(HOST+url,link))
            if u.scheme not in {'http','https'}: continue
            if u.netloc not in {'organexa.com.tr','www.organexa.com.tr'}: continue
            if u.netloc != 'organexa.com.tr' or u.scheme != 'https': error(url,'noncanonical internal host: '+link)
            path = unquote(u.path)
            if path in pages:
                target = pages[path].path
                if tag=='a' and path != url: graph[url].add(path)
            else:
                target = root/path.lstrip('/')
                if target.is_dir(): target = target/'index.html'
                if target.suffix=='.html' and tag=='a': error(url,'HTML links must use clean trailing-slash route: '+link)
            if not target.is_relative_to(root) or not target.is_file():
                broken += 1; error(url,'broken internal link: '+link); continue
            if u.fragment:
                other=pages.get(path)
                if other is None or unquote(u.fragment) not in other.ids: broken += 1; error(url,'missing anchor: '+link)
        nodes=[n for ld in p.ld for n in walk(ld)]
        types={n.get('@type') for n in nodes if isinstance(n.get('@type'),str)}
        if url in indexable and 'WebPage' not in types: error(url,'missing WebPage schema')
        if url=='/' and not {'Organization','WebSite','SoftwareApplication'}.issubset(types): error(url,'missing homepage schema')
        if {'Review','AggregateRating','Offer'} & types: error(url,'unverified commercial schema')
        for app in [n for n in nodes if n.get('@type')=='SoftwareApplication']:
            if app.get('name')!='Organexa' or app.get('applicationCategory')!='BusinessApplication' or app.get('operatingSystem')!='Android, iOS': error(url,'incorrect application schema')
        breadcrumbs=[n for n in nodes if n.get('@type')=='BreadcrumbList']
        if url in REQUIRED-{'/','/privacy/','/terms/','/contact/'} and not breadcrumbs: error(url,'missing BreadcrumbList')
        if breadcrumbs:
            items=breadcrumbs[0].get('itemListElement',[])
            expected=[{'@type':'ListItem','position':i,'name':name,'item':HOST+href} for i,(href,name) in enumerate(p.crumbs,1)]
            if items != expected: error(url,'visible breadcrumbs do not match schema')
        faqs=[n for n in nodes if n.get('@type')=='FAQPage']
        if p.faq and not faqs: error(url,'FAQ missing schema')
        if faqs:
            values=[(n.get('name'),n.get('acceptedAnswer',{}).get('text')) for n in faqs[0].get('mainEntity',[])]
            if values != p.faq or not values: error(url,'FAQ schema differs from visible FAQ')
    reached, todo = set(), ['/']
    while todo:
        current=todo.pop()
        if current in reached: continue
        reached.add(current);todo.extend(graph.get(current,set())-reached)
    for url in indexable-reached: error(url,'orphan page: not reachable from homepage')
    try:
        xml=ET.parse(root/'sitemap.xml')
        urls=[n.text for n in xml.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        if len(urls)!=len(set(urls)): error('sitemap','duplicate URLs')
        if set(urls)!={HOST+u for u in indexable}: error('sitemap','URLs differ from indexable pages')
        if xml.getroot().tag!='{http://www.sitemaps.org/schemas/sitemap/0.9}urlset': error('sitemap','invalid namespace/root')
    except (OSError,ET.ParseError) as exc: error('sitemap',str(exc))
    try:
        robots=(root/'robots.txt').read_text(encoding='utf-8-sig')
        if 'Sitemap: '+HOST+'/sitemap.xml' not in robots: error('robots','missing canonical sitemap URL')
        if 'User-agent: *' not in robots or 'Allow: /' not in robots: error('robots','missing allow policy')
        if any(line.lower().startswith('disallow:') and line.split(':',1)[1].strip() for line in robots.splitlines()): error('robots','unexpected disallow')
    except OSError as exc: error('robots',str(exc))
    try:
        if (root/'CNAME').read_text().strip()!='organexa.com.tr': error('CNAME','wrong canonical domain')
        manifest=json.loads((root/'site.webmanifest').read_text(encoding='utf-8'))
        for icon in manifest['icons']:
            if not (root/icon['src'].lstrip('/')).is_file(): error('manifest','missing icon')
    except (OSError,ValueError,KeyError) as exc: error('assets',str(exc))
    print(f'HTML pages: {len(pages)}; indexable: {len(indexable)}; broken links: {broken}')
    for message in warnings: print('NOTE '+message)
    for message in errors: print('FAIL '+message)
    print('SEO AUDIT: '+('FAIL' if errors else 'PASS'))
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(audit(Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]))
