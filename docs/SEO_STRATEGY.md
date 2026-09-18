# SEO stratejisi

## Hedef ve sınır

Organexa’nın Türkiye’deki etkinlik profesyonellerine hangi işi kolaylaştırdığını açıkça anlatmak. Başarı; arama niyetine uygun içerik, çalışan sayfalar ve gerçek ürün davranışı üzerinden değerlendirilir. Sıralama, indekslenme veya trafik garantisi yoktur. Anahtar kelimeler hacim araştırması sonucu değil, ürün kapsamına dayalı editoryal hedeflerdir.

## Mimari

- `/`: Organexa ve genel etkinlik yönetim uygulaması niyeti.
- `/features/`: özellikleri karşılaştırma ve ayrıntı sayfalarına geçiş merkezi.
- `/for-pianists/`, `/for-djs/`, `/for-event-companies/`: her mesleğin günlük sorununa özgü iş akışları.
- `/event-management/`, `/customer-management/`, `/payment-tracking/`, `/whatsapp-reminders/`, `/backup-and-restore/`: belirli bir işlevin yararı, kullanımı ve sınırları.
- `/privacy/`, `/terms/`, `/contact/`: güven, geliştirici kimliği ve ürünün hukuki/iletişim bilgileri. Ticari anahtar kelimelere göre şişirilmez.

Her sayfanın primary keyword, başlık, H1, canonical ve bağlantıları [anahtar kelime haritasında](SEO_KEYWORD_MAP.md). Ana sayfa tüm ürün kümelerine bağlanır; özellik merkezi tüm özellik/persona sayfalarına, içerikler de ilgili iş akışlarına bağlanır. Breadcrumb bağlantıları görünürdür ve JSON-LD ile eşleşir. Şehir bazlı kopyalar veya yüzlerce benzer sayfa oluşturulmaz.

## İçerik doğruluğu

Ürün anlatımı sahibinin verdiği kapsamla sınırlıdır. Mobil uygulama kodu bu repoda değildir. Yayından önce gerçek sürümle karşılaştırılması gerekenler: Google izinleri, yedeklerden hariç tutulan tokenlar, silme/restore davranışı, WhatsApp akışı ve platform kullanılabilirliği. Android/iOS ürün hedefi hem görünür içerikte hem schema içinde yer alır; mağazada yayımlanma iddiası yoktur. Otomatik mesaj, banka entegrasyonu, anlık senkronizasyon, ekip yetkilendirmesi veya şifreleme türü uydurulmaz.

Organexa bir ürün/marka olarak Organization ile tanımlanır; bir şirket türü, tüzel unvan veya adres uydurulmaz. Geliştirici İzzet ÖRS görünür ve tutarlıdır. Gerçek destek adresi kesinleşene kadar config boş kalır. Bu eksiklik OAuth başvurusu öncesinde giderilmelidir.

## Structured data

Ana sayfa: Organization, WebSite, SoftwareApplication, WebPage. Yeni sayfalar: WebPage ve BreadcrumbList. Yalnız görünür soru/yanıtı olan sayfalarda FAQPage bulunur; yanıtlar HTML ve JSON-LD içinde aynı olmalıdır.

Schema.org bakımından bir uygulamayı tanımlamak, Google Software App zengin sonucuna hak kazanmakla aynı şey değildir. Google’ın ilgili sonuç türü fiyat ve gerçek değerlendirme/yorum verileri ister. Henüz doğrulanmış fiyat veya yorum olmadığından Offer, Review ve AggregateRating eklenmez. Bu nedenle Rich Results Test’in uygulama zengin sonucu için eksik alan bildirmesi beklenebilir; veri uydurarak giderilmez. [Google Software App gereksinimleri](https://developers.google.com/search/docs/appearance/structured-data/software-app).

FAQ içeriği kullanıcıya yardımcı olmak içindir; FAQ işaretlemesi özel arama görünümü garantisi değildir. [Google yapılandırılmış veri ilkeleri](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

## Teknik ilkeler

Tek canonical host `https://organexa.com.tr`, temiz dizin URL’leri ve sonda `/`. İçerik ilk HTML yanıtındadır, JS ile sonradan oluşturulmaz. Aynı içerik mobil/masaüstünde bulunur. Mobil menü bağlantıları kaynak HTML’de kalır; menünün kapalı olması gizli SEO metni değildir. 404 noindex ve sitemap dışında; tüm 13 public içerik sayfası sitemap içindedir.

Sistem fontları, küçük yerel görseller, açık boyutlar ve ertelenmiş minimal JavaScript kullanılır. CSS ilk görünüm için gereklidir; gereksiz preload veya üçüncü taraf kod eklenmez. Yalnız ilk görünümde bulunan logo görselleri var; gelecekte alt bölümlere gerçek görsel eklenirse `loading="lazy"`, anlamlı alt metin ve width/height eklenmelidir.

## Ölçüm ve geliştirme

Search Console’da sorgu, sayfa, gösterim, tıklama ve CTR’yi birlikte değerlendirin. Ortalama konumu tek başına başarı ölçüsü yapmayın. Aynı niyetli sorgular iki sayfaya dağılıyorsa kapsamları netleştirin; eşdeğer sayfaları ancak yönlendirme planıyla birleştirin. Henüz analytics kurulmadığı için dönüşüm sayıları iddia edilmez.

Lighthouse hedefleri Performance/Accessibility/Best Practices ≥95, SEO 100’dür; ölçüm koşulları ve gerçek sonuç ayrıca raporlanır. Laboratuvar skoru Core Web Vitals saha verisi değildir. Yeterli trafik oluştuğunda Search Console/CrUX verisinden LCP, CLS ve INP izlenir. Otomatik erişilebilirlik testi tam WCAG uygunluğu belgesi değildir.

## Yerelleştirme

Şimdilik `lang="tr"`, `og:locale=tr_TR`, schema `inLanguage=tr-TR`. İngilizce içerik gerçekten hazırlanırsa `/en/` mimarisi, self-canonical ve iki yönlü hreflang uygulanır. Mevcut sayfaya var olmayan çeviri bağlantıları veya yalnız SEO için ince çeviriler eklenmez.
