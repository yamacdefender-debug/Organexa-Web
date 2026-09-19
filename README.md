# Organexa — resmi web sitesi

Organexa’nın Türkçe ürün vitrini ve herkese açık politika sayfaları. Geliştirici: **İzzet ÖRS**. Üretim adresi: **https://organexa.com.tr**.

## Yerel önizleme

Derleme, npm paketi veya framework gerekmez. Repo kökünde:

```sh
python -m http.server 8000
```

Tarayıcıda http://localhost:8000 adresini açın. Kökten başlayan bağlantılar nedeniyle HTML dosyasına çift tıklamak yerine HTTP sunucusu kullanın. `/privacy`, `/terms`, `/contact` dizinleri sonuna `/` eklenerek açılır. JavaScript kapalıyken de içerik ve gezinme çalışır.

## GitHub Pages yayını

1. `yamacdefender-debug/Organexa-Web` → Settings → Pages.
2. Build and deployment: **Deploy from a branch**, **main**, **/ (root)** → Save.
3. Custom domain: `organexa.com.tr`. Kökteki `CNAME` bu alan adını içerir.
4. DNS doğrulaması ve sertifika tamamlanınca **Enforce HTTPS** seçeneğini etkinleştirin.
5. HTTPS üzerinden ana sayfa, politika, koşullar, iletişim ve bilinmeyen bir adresin 404 sayfasını kontrol edin.

`.nojekyll` doğrudan statik yayını sağlar. Workflow veya build server gerekmez. Bu repo özel alan adı kökü için hazırlanmıştır; `/Organexa-Web/` proje alt yolundaki önizleme hedeflenmez. 18 Eylül 2026 kontrolünde Pages yayını ve alan adı aktif, sertifika onaylıdır. Bu milestone sırasında Enforce HTTPS etkinleştirilmiştir. Yukarıdaki adımlar yeniden kurulum içindir.

## Özel alan adı ve DNS

DNS sağlayıcısında `@` için şu dört A kaydını ekleyin:

| Tür | Ad | Değer |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | yamacdefender-debug.github.io |

İsteğe bağlı IPv6 AAAA: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`. Eski/çakışan web A/AAAA kayıtlarını kontrol edin; e-posta MX/TXT kayıtlarını koruyun. DNS yayılımını bekleyin. GitHub hesap ayarlarındaki Pages alan adı doğrulaması için verilen TXT kaydını ekleyin; doğrulama kodu hesaba özeldir. Wildcard DNS kullanmayın.

Güncel adımlar: [GitHub özel alan adı dokümanı](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## Google OAuth branding

| Alan | Değer |
| --- | --- |
| Application name | Organexa |
| Homepage | https://organexa.com.tr/ |
| Privacy Policy | https://organexa.com.tr/privacy/ |
| Terms of Service | https://organexa.com.tr/terms/ |
| Authorized domain | organexa.com.tr |
| Public support / developer contact | izzetors42@gmail.com |

Alan adı sahipliğini Google’ın istediği yöntemle doğrulayın. Support email ve developer contact alanlarında `izzetors42@gmail.com` adresini kullanın; Google Cloud konsolundaki alanların kaydedilmesi hesap sahibi tarafından ayrıca yapılmalıdır. Redirect URI ve istemci türünü gerçek mobil uygulama yapılandırmasına göre tanımlayın; bu statik site OAuth callback uygulamaz. Homepage ve Privacy Policy oturum açmadan HTTPS ile erişilebilir olmalıdır.

Google Drive izni: `https://www.googleapis.com/auth/drive.appdata`. Sign-In için temel kimlik, e-posta ve görünen ad açıklanır. Web sitesi kendisi Google oturumu veya Drive erişimi başlatmaz.

Politika, ürün sahibinin sağladığı veri akışı gereksinimlerine göre hazırlanmıştır; mobil uygulama kaynak kodu bu repoda olmadığı için davranışı burada doğrulanmamıştır. Production başvurusundan önce gerçek izinleri, tokenların yedeklerden hariç tutulmasını, silme/bağlantı kaldırma davranışını ve veri akışlarını metinle karşılaştırın. Metinde belirtilmeyen sunucu işlemesi, analitik veya farklı bir veri kullanımı varsa politikayı güncelleyin. Kesin saklama süresi, şifreleme ve resmi Google onayı gibi doğrulanmamış iddialar eklenmemiştir. Türkiye’deki fiili veri işleme ve KVKK aydınlatma gereklilikleri için hukuki değerlendirme ayrıca yapılmalıdır. Site hazırlığı OAuth doğrulaması tamamlandı anlamına gelmez.

Kaynak: [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), [Drive uygulama veri alanı](https://developers.google.com/workspace/drive/api/guides/appdata).

## İletişim ve GoatCounter

Resmi telefon **0543 461 5884** (`tel:+905434615884`), e-posta `izzetors42@gmail.com` adresidir. Telefonun görünen biçimi ve URI'si `assets/config.js` içindeki `contactPhone` alanından gelir. İletişim sayfası, footer ve DJ CTA içinde JavaScript kapalıyken de çalışan telefon bağlantıları vardır; numara değişince bu statik yedekleri de güncelleyin.

GoatCounter aktivasyonu:

1. [GoatCounter](https://www.goatcounter.com/) üzerinde site oluşturun ve public site code değerini alın.
2. `assets/config.js` içindeki `goatcounterCode: ""` değerine yalnızca bu code'u yazın. Yönetici erişim token'ı veya gizli anahtar eklemeyin.
3. GoatCounter site ayarlarında **Allow adding visitor counts on your website** seçeneğini açın.
4. Deploy edin; ana sayfa ve `/for-djs/` dahil tüm HTML sayfalarını kontrol edin.

Site code boşsa analytics script'i ve toplam ziyaret isteği çalışmaz; footer'daki gösterge gizli kalır. Kod ayarlandığında `/assets/site.js` her sayfada GoatCounter `count.js` dosyasını bir kez yükler. Sayfalar SPA değildir, dolayısıyla her HTML yüklemesi tek otomatik pageview gönderir; ek route sayımı yoktur. Footer gerçek toplamı `https://<code>.goatcounter.com/counter/TOTAL.json` yanıtından alır. Bu endpoint erişilemezse, yanıt geçersizse veya public counter ayarı kapalıysa gösterge gizli kalır. GoatCounter toplam yanıtını önbelleğe alabilir; gösterge anlık olmayabilir. Yerel `localhost` ve `127.0.0.1` önizlemelerinde analytics ve sayaç istekleri yapılmaz.

## Destek e-postasını değiştirme

`assets/config.js` içindeki `supportEmail` alanını değiştirin:

```js
window.ORGANEXA_CONFIG = Object.freeze({
  supportEmail: "izzetors42@gmail.com",
  contactPhone: Object.freeze({ display: "0543 461 5884", uri: "tel:+905434615884" }),
  goatcounterCode: ""
});
```

Public adres `izzetors42@gmail.com` olarak ayarlanmıştır. JavaScript yalnız `[data-support-email]` bağlantılarının adresini günceller; CTA metnini korur. Bağlantılar statik HTML içinde de bulunduğundan JavaScript kapalıyken e-posta ve buton çalışır. Adres değişirse config ile birlikte `contact/index.html`, `privacy/index.html`, `terms/index.html` içindeki mailto/görünen adresleri, OAuth bilgilerini ve ilgili belgeleri güncelleyin. Config içine gizli anahtar veya token koymayın; tüm dosyalar herkese açıktır. Site mevcut dark/gold tasarımını sistemin açık ve koyu renk tercihlerinde korur; ayrı bir açık tema anahtarı yoktur.

## Yapı ve tasarım

```text
index.html          Ana sayfa
privacy/index.html  Gizlilik Politikası
terms/index.html    Kullanım Koşulları
contact/index.html  İletişim
404.html            Bulunamayan sayfa
assets/styles.css   Responsive marka tasarımı
assets/site.js      Mobil menü ve destek bağlantısı
assets/config.js    Public iletişim bilgileri ve GoatCounter site code
assets/favicon.svg OX monogramı
assets/og-image.png Sosyal paylaşım görseli (1200 × 630)
robots.txt
sitemap.xml
CNAME
.nojekyll
```

Harici font veya uygulama kütüphanesi yoktur. GoatCounter yapılandırıldığında üçüncü taraf analytics istekleri yapılır; entegrasyon tarayıcı çerezi kullanmaz. Sistem fontları, yerel SVG ve küçük PNG kullanılır. OX monogramı ve telefon içindeki HTML/CSS tasviri, verilen lacivert/altın marka yönlendirmesine göre bu repo için hazırlanmıştır; mobil uygulamanın özgün logo dosyası veya ekran görüntüsü sağlanmamıştır. Önizleme temsili olarak etiketlenmiştir; gerçek müşteri verisi içermez. CTA’lar çalışan sayfa/bölüm bağlantılarıdır; sahte mağaza bağlantısı yoktur.

## Yayın kontrolü

- Desktop, tablet, telefon ve %200 metin büyütmede taşma, menü ve bağlantıları kontrol edin.
- Tab / Shift+Tab, görünür odak, içeriğe geç bağlantısı ve mobil menüde Escape davranışını kontrol edin.
- JavaScript kapalıyken metinlerin, alt menünün ve ana gezinmenin çalıştığını kontrol edin.
- Tüm canonical / Open Graph adresleri ve sitemap üretim alan adını kullanır.
- Politikalar hukuki danışmanlık değildir; gerçek ürün ve veri akışı değiştikçe güncellenmelidir.
## SEO mimarisi ve bakım

Bu milestone ile dokuz yeni içerik sayfası eklenmiştir:

- `/features/`
- `/for-pianists/`, `/for-djs/`, `/for-event-companies/`
- `/event-management/`, `/customer-management/`, `/payment-tracking/`
- `/whatsapp-reminders/`, `/backup-and-restore/`

Tüm içerik statik HTML’dir; derleme adımı gerektirmez. Yeni sayfa veya içerik düzenlerken HTML’yi doğrudan güncelleyin. Title, description, OG/Twitter metinleri ve WebPage JSON-LD birbirleriyle tutarlı olmalı; FAQ değişirse görünür cevap ve FAQPage JSON-LD birlikte değişmelidir. Breadcrumb HTML ve BreadcrumbList eşleşmelidir. Yeni URL’yi sitemap ve anahtar kelime haritasına ekleyip en az bir bağlamsal iç bağlantı verin. Gizli `.qa/` çalışma çıktıları git tarafından dışlanır ve yayımlanmaz.

```sh
python tools/seo_audit.py
```

Standart kütüphane dışında Python bağımlılığı yoktur. Betik repo kökünü kendisi bulur; isteğe bağlı site kökü argümanı alır. H1, metadata, canonical, OG, Twitter, HTML tag dengesi, heading sırası, alt/boyutlar, iç bağlantı/anchor, erişilebilir sayfa grafiği, JSON-LD, görünür FAQ/breadcrumb eşleşmesi, sitemap ve robots kontrollerinde kritik hata varsa sıfırdan farklı çıkış kodu döndürür. Harici sitelerin kullanılabilirliğini, sunucu HTTP başlıklarını veya Google indeksini denetlemez.

Belgeler:

- [SEO stratejisi](docs/SEO_STRATEGY.md)
- [Anahtar kelime haritası](docs/SEO_KEYWORD_MAP.md)
- [Search Console ve Bing kurulumu](docs/SEARCH_CONSOLE_SETUP.md)
- [Yayın kontrol listesi ve ölçümler](docs/SEO_RELEASE_CHECKLIST.md)
- [Gelecek içerik planı](docs/SEO_CONTENT_ROADMAP.md)

## Canonical, yönlendirmeler ve 404

Tek host `https://organexa.com.tr`; dizin sayfalarında son `/` kullanılır. Canonical etiketi yönlendirme değildir. GitHub Pages’te Custom domain bu apex ad olmalı; `www` DNS CNAME kaydı `yamacdefender-debug.github.io` adresine yönelmeli. GitHub Pages apex/www yönlendirmesini DNS doğruysa sağlar. Enforce HTTPS ayrıca etkinleştirilmelidir. Üretimde `http`, `https`, `www`, slash’sız ve `/index.html` URL’lerini kontrol edin; tüm eşdeğer adresler tercih edilen sürüme yönlenmeli veya self-canonical ile aynı içeriğin tercih edilen dizin sürümünü belirtmelidir. `/index.html` için özel 301 kuralı gerekiyorsa Pages’in önünde yönlendirme destekleyen bir katman gerekir; JS yönlendirmesi eklenmemiştir.

Bilinmeyen URL gerçek HTTP **404** döndürmelidir. SPA fallback kullanılmaz. Kökteki `404.html` markalı hata sayfasıdır, noindex taşır ve sitemap’e dahil değildir. `python -m http.server` bilinmeyen yolda kendi standart 404 yanıtını verir; tasarımı yerelde `/404.html` ile, üretim 404 davranışını bilinmeyen bir yol ile kontrol edin.

## Güvenlik başlıkları ve GitHub Pages sınırları

GitHub Pages statik deposundan özel HTTP yanıt başlıkları tanımlanamaz. `_headers`, `.htaccess` veya HTML `http-equiv` ile aşağıdaki başlıkları etkinmiş gibi göstermeyin. Başlıkların çoğu için yapılandırılabilir CDN/reverse proxy veya başka bir barındırma katmanı gerekir; bu milestone böyle bir katman kurmaz.

| Politika | Mevcut durum / uygulanacak yer |
| --- | --- |
| Referrer-Policy | Her HTML’de `meta name="referrer" content="strict-origin-when-cross-origin"` var. Yanıt başlığı sunucu/CDN üzerinden ayrıca uygulanabilir. |
| Content-Security-Policy | Zorunlu bir CSP şu anda uygulanmıyor. Önce tüm sayfaları ve JSON-LD’yi test ederek sunucu/CDN’de Report-Only ile başlayın; ardından dar bir allowlist uygulayın. |
| X-Content-Type-Options | Sunucu/CDN’de `nosniff`; HTML meta karşılığı yok. Pages’in gerçek yanıtını incelemeden mevcut olduğu iddia edilmez. |
| Permissions-Policy | Sunucu/CDN’de örneğin `camera=(), microphone=(), geolocation=()`; sitede bu özellikler kullanılmıyor. |

Başlangıç CSP taslağı: `default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'self'; form-action 'none'; frame-ancestors 'none'`. Bu bir **taslaktır**, etkin başlık değildir. JSON-LD ve tarayıcı davranışını kontrol edip gerekiyorsa tam içerik hash’i kullanın; sırf kolaylık için unsafe-inline eklemeyin. Meta CSP sınırlı direktifler için kullanılabilir ancak `frame-ancestors`, report-only ve raporlama yeteneklerinin yerini tutmaz. [MDN CSP rehberi](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP), [frame-ancestors sınırı](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors).

## Marka görselleri

`assets/og-image.png` 1200×630 paylaşım görselidir. OX markası için `favicon.ico`, `assets/favicon.svg`, `assets/apple-touch-icon.png` (180), `assets/icon-192.png`, `assets/icon-512.png` ve `site.webmanifest` eklidir. Manifest yalnız site kimliği/görünümü sağlar; service worker veya çevrimdışı çalışan uygulama iddiası yoktur. Gerçek mobil marka dosyaları verilirse türevleri birlikte yenileyin.
