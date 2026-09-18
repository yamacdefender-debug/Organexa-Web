# SEO yayın kontrol listesi

Kontrol tarihi: 18 Eylül 2026. Bu belge otomatik test ile canlı servis durumunu ayrı raporlar.

## Tamamlanan yerel kontroller

- [x] 13 indekslenebilir public sayfa ve noindex markalı 404.
- [x] Her sayfada bir H1; benzersiz title/description ve self-canonical.
- [x] OG/Twitter metadata, 1200×630 paylaşım görseli, OX ikonları.
- [x] 9 yeni sayfada görünür breadcrumb ve eşleşen BreadcrumbList.
- [x] Ana sayfada Organization/WebSite/SoftwareApplication; sayfalarda WebPage.
- [x] Görünür FAQ ile JSON-LD soru/yanıt eşleşmesi.
- [x] Sitemap XML, robots sitemap satırı, tek HTTPS/non-www canonical host.
- [x] `python tools/seo_audit.py`: PASS, 14 HTML, 13 indexable, **0 kırık iç bağlantı**; ana sayfadan erişilemeyen public sayfa yok.
- [x] Betiğin hata yakalaması ayrı kopyada doğrulandı: kırık URL, eksik anchor, tekrarlı title, bozuk JSON-LD, yanlış FAQ, eksik sitemap URL’si ve eksik alt için çıkış kodu 1.
- [x] html-validate 10.17.0: tüm 14 HTML sayfası, 0 hata. `node --check` her iki JS dosyası için geçti.
- [x] 390 px genişlikte tüm 14 sayfa; 320/768/1440 px örnek sayfalar: yatay taşma yok.
- [x] Ayrı test kopyasında kök yazı boyutu 32 px (%200): ana sayfa, özellikler, ödeme, yedekleme ve iletişim 390/768/1440 genişlikte taşmadı.
- [x] Mobil menü aç/kapat, Escape ile kapanma ve odağın düğmeye dönmesi; klavyeyle FAQ açılması.
- [x] Kaynak HTML’de gezinme bağlantıları var. JS kapalıysa noscript stil dosyası mobil gezinmeyi görünür tutar.
- [x] İlk mobil gezinme yüklemesinde yerleşim kayması giderildi; son yerel Lighthouse CLS = 0.

Betiğin NOTE satırlarında privacy/terms/404 title uzunlukları görülebilir. Bu sayfalarda kısa ve açık isimler bilinçli tercihtir; ticari anahtar kelimelerle uzatılmaz.

## Lighthouse laboratuvar sonucu

18 Eylül 2026, Lighthouse 12.8.2, kurulu Chrome headless, varsayılan mobil benzetimi ve throttling, `http://localhost:8000/`. Son yerel ölçüm:

| Performance | Accessibility | Best Practices | SEO | LCP | CLS | TBT |
| --- | --- | --- | --- | --- | --- | --- |
| 72 | 100 | 82 | 100 | 5,7 s | 0 | 0 ms |

**Ölçüm sınırlaması:** Cihazdaki Kaspersky, repo dosyalarında bulunmayan `gc.kis.v2.scr.kaspersky-labs.com` kaynaklı script ve CSS’yi yerel HTTP sayfasına enjekte etti. Lighthouse bu kaynakları render-blocking ve HTTP içerik olarak raporladı. Bu yüzden Performance ≥95 ve Best Practices ≥95 hedefleri bu ölçümle doğrulanmış değildir. Güvenlik yazılımı kapatılmadı, istekler sonuçları yükseltmek için engellenmedi. Yerel Python sunucusu üretim cache başlıklarını da taklit etmez. Ham yerel rapor geçici `.qa/lighthouse-home-final.json` dosyasındadır; kişiye/ortama özel enjekte URL’leri nedeniyle yayımlanmaz.

Lighthouse skoru saha Core Web Vitals ölçümü veya tam WCAG denetimi değildir. Canlı HTTPS yayını sonrası PageSpeed Insights/Lighthouse ve yeterli veri oluştuğunda Search Console saha raporlarıyla ayrıca değerlendirilmelidir.

## Üretim altyapısı

- [x] GitHub Pages kaynağı main / root, custom domain `organexa.com.tr`.
- [x] Apex ve www için sertifika onaylı; **Enforce HTTPS etkinleştirildi**.
- [x] `http://organexa.com.tr/` → 301 `https://organexa.com.tr/`.
- [x] `https://www.organexa.com.tr/` → 301 `https://organexa.com.tr/`.
- [x] `https://organexa.com.tr/` → 200; yeni ana sayfa başlığı ve canonical doğrulandı.
- [x] Yeni sürümde 13 sitemap içerik URL’sinin tamamı HTTPS 200 ve doğru self-canonical; sitemap.xml ve robots.txt 200.
- [x] `/features` → 301 `/features/`; bilinmeyen test yolu gerçek HTTP 404 ve markalı hata içeriği döndürüyor.

## Hesap / ürün sahibinde kalan yayın işleri

- [x] Public destek e-postası `izzetors42@gmail.com` olarak config, statik iletişim sayfası, privacy ve terms içinde tamamlandı.
- [ ] Mobil uygulamadaki izinler, token hariç tutma, silme ve restore davranışlarını politika metniyle karşılaştır.
- [ ] Search Console domain property için hesap özelinde DNS TXT doğrulaması yap.
- [ ] Sitemap gönder, ana sayfa ve önemli landing URL’leri için URL Inspection yap; uygun sayfalarda indexing iste.
- [ ] Google’ın seçtiği canonical ve indeksleme durumunu zaman içinde izle.
- [ ] İstenirse Bing mülkünü ekle veya Search Console’dan içe aktar, sitemap durumunu kontrol et.
- [ ] Gelecekteki gerçek ürün davranışı / içerik değişikliklerinde metadata, schema, sitemap ve keyword map’i birlikte güncelle.

SEO hazırlığı, Google’ın indekslediği veya belirli aramalarda sıralama verdiği anlamına gelmez. Schema sözdiziminin geçmesi de uygulama zengin sonucu uygunluğu değildir; fiyat/yorum uydurulmamıştır.

## Canlı HTTPS Lighthouse ölçümü

Aynı cihazda Lighthouse 12.8.2 / Chrome headless / varsayılan mobil benzetimi, 18 Eylül 2026; içerik commit’i `d77b95d3c489d37f2637dae695c9e222e562f3a7` yayımlandıktan sonra:

| Sayfa | Performance | Accessibility | Best Practices | SEO | LCP | CLS | TBT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| https://organexa.com.tr/ | 68 | 100 | 100 | 100 | 5,9 s | 0 | 170 ms |
| https://organexa.com.tr/payment-tracking/ | 71 | 100 | 100 | 100 | 5,8 s | 0 | 50 ms |

Canlı HTTPS ölçümlerinde de Kaspersky’nin harici script/CSS enjeksiyonu ağ kayıtlarında bulunuyor. Performance 95+ hedefi **doğrulanamadı**; bu sonuçlar temiz istemcideki gerçek site performansı olarak sunulamaz. Yerel ana sayfanın siteye ait HTML, CSS, JS ve logo toplam ham aktarım büyüklüğü yaklaşık 31,8 KB’dır. Enjekte kaynaklar repoda yoktur. Temiz ortamda yeni bir saha/laboratuvar ölçümü gerekir; güvenlik yazılımı devre dışı bırakılmamıştır.

Bağımsız Google PageSpeed Insights API ölçümü de denendi; API `429 quota exceeded` döndürdüğü için bir skor üretmedi. Eksik ölçüm PASS olarak işaretlenmez. Ham canlı raporlar yerelde `.qa/lighthouse-production.json` ve `.qa/lighthouse-payment-production.json`; ağ kayıtları ortama özel parametreler içerdiğinden Git’e eklenmez.

HTTP ve www yönlendirmeleri, geçerli HTTPS erişimi ve gerçek 404 ağ yanıtları Node fetch ile sertifika doğrulaması korunarak kontrol edildi. Google Search Console hesabına giriş, domain TXT doğrulaması veya sitemap gönderimi yapılmadı.
