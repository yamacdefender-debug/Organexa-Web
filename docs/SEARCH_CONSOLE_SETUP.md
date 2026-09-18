# Search Console ve Bing kurulumu

Bu belge hazırlık rehberidir; hesap doğrulaması, DNS değişikliği ve sitemap gönderimi yapılmış sayılmaz.

## Google Search Console

1. [Search Console](https://search.google.com/search-console) içinde **Domain property** ekleyin: `organexa.com.tr` (protokol veya yol eklemeden).
2. Google’ın bu hesap için ürettiği TXT doğrulama değerini DNS sağlayıcısında istenen ada ekleyin. Değeri uydurmayın, başka TXT/MX kayıtlarını silmeyin. DNS yayılımından sonra Verify işlemini yapın ve kaydı koruyun.
3. Site HTTPS üzerinden yayımlandıktan sonra Sitemaps bölümünde `https://organexa.com.tr/sitemap.xml` gönderin. Başarılı okunmasını ve keşfedilen sayfa sayısını kontrol edin.
4. URL Inspection alanında `https://organexa.com.tr/` adresini inceleyin. **Test live URL** ile erişim ve işlenen HTML’yi kontrol edin. Kullanıcı tarafından belirtilen canonical ile Google’ın seçtiği canonical’ı karşılaştırın.
5. İçerik erişilebilir ve indekslemeye uygunsa **Request indexing** isteyin. Önemli özellik/persona sayfaları için de URL inspection yapın. Tekrar tekrar istek göndermek sıralama veya hızlı tarama garantisi vermez.
6. **Page indexing** raporunda robots engeli, noindex, soft 404, yönlendirme ve duplicate/canonical durumlarını inceleyin. 404 sayfasının indekslenmemesi beklenir; tüm keşfedilen adreslerin indekslenmesi zorunlu değildir.
7. **Core Web Vitals** raporunda yeterli saha verisi oluştuktan sonra LCP, CLS ve INP durumuna bakın. Yeni sitelerde veri bulunmaması tek başına hata değildir.
8. Sunuluyorsa **Enhancements** raporlarında breadcrumb/structured data sorunlarını inceleyin. Raporun görünmemesi schema olmadığı anlamına gelmez. Sahte fiyat veya yorum eklemeyin.
9. Security issues ve Manual actions raporlarını, ardından Performance → Search results içindeki sorgu/sayfa kırılımını düzenli kontrol edin.

**Mobil kontrol güncellemesi:** Search Console’un Mobile Usability raporu ve eski Mobile-Friendly Test 2023’te kaldırıldı. Artık olmayan menüleri aramayın. Mobil Lighthouse/PageSpeed Insights, gerçek cihaz testi, responsive görünüm, klavye ve %200 büyütme testlerini kullanın. URL Inspection ile mobil tarayıcının aldığı içeriği kontrol edin.

Resmi kaynaklar:
- [Domain property ve doğrulama](https://support.google.com/webmasters/answer/9008080)
- [URL Inspection](https://support.google.com/webmasters/answer/9012289)
- [Sitemap yönetimi](https://support.google.com/webmasters/answer/7451001)
- [Google dokümantasyon güncellemeleri — 1 Aralık 2023 kaldırmaları](https://developers.google.com/search/updates)

## Bing Webmaster Tools (isteğe bağlı)

1. [Bing Webmaster Tools](https://www.bing.com/webmasters/) hesabında siteyi ekleyin. Google Search Console’da zaten doğrulandıysa **Import from Google Search Console** seçeneği kullanılabilir; istenen hesap izinlerini inceleyin.
2. İçe aktarma yerine manuel doğrulama seçerseniz Bing’in ürettiği gerçek DNS/HTML doğrulama değerini uygulayın. Örnek doğrulama anahtarı yayımlamayın.
3. Sitemaps bölümünde `https://organexa.com.tr/sitemap.xml` adresini kontrol edin; aktarılmadıysa gönderin.
4. URL Inspection ve Site Scan ile taranabilirlik sorunlarını takip edin. Bing dizini ve raporları Google’dan bağımsızdır.

[Bing’in resmi içe aktarma açıklaması](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools).
