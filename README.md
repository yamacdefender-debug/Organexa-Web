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

`.nojekyll` doğrudan statik yayını sağlar. Workflow veya build server gerekmez. Bu repo özel alan adı kökü için hazırlanmıştır; `/Organexa-Web/` proje alt yolundaki önizleme hedeflenmez. Pages etkinleştirme ve DNS işlemleri ayrıca yapılmalıdır.

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

Alan adı sahipliğini Google’ın istediği yöntemle doğrulayın. Support email ve developer contact alanlarına gerçek, izlenen adresler girin. Redirect URI ve istemci türünü gerçek mobil uygulama yapılandırmasına göre tanımlayın; bu statik site OAuth callback uygulamaz. Homepage ve Privacy Policy oturum açmadan HTTPS ile erişilebilir olmalıdır.

Google Drive izni: `https://www.googleapis.com/auth/drive.appdata`. Sign-In için temel kimlik, e-posta ve görünen ad açıklanır. Web sitesi kendisi Google oturumu veya Drive erişimi başlatmaz.

Politika, ürün sahibinin sağladığı veri akışı gereksinimlerine göre hazırlanmıştır; mobil uygulama kaynak kodu bu repoda olmadığı için davranışı burada doğrulanmamıştır. Production başvurusundan önce gerçek izinleri, tokenların yedeklerden hariç tutulmasını, silme/bağlantı kaldırma davranışını ve veri akışlarını metinle karşılaştırın. Metinde belirtilmeyen sunucu işlemesi, analitik veya farklı bir veri kullanımı varsa politikayı güncelleyin. Kesin saklama süresi, şifreleme ve resmi Google onayı gibi doğrulanmamış iddialar eklenmemiştir. Türkiye’deki fiili veri işleme ve KVKK aydınlatma gereklilikleri için hukuki değerlendirme ayrıca yapılmalıdır. Site hazırlığı OAuth doğrulaması tamamlandı anlamına gelmez.

Kaynak: [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), [Drive uygulama veri alanı](https://developers.google.com/workspace/drive/api/guides/appdata).

## Destek e-postasını değiştirme

`assets/config.js` içindeki tek ayarı değiştirin:

```js
window.ORGANEXA_CONFIG = Object.freeze({ supportEmail: "" });
```

Gerçek adres kesinleşene kadar boş bırakın. Boşken iletişim sayfası adresin henüz yayımlanmadığını belirtir; sahte adres gösterilmez. Geçerli adres girildiğinde güvenli DOM metni ve `mailto:` bağlantısı oluşturulur. JavaScript kapalıyken de adresi göstermek için `contact/index.html` içindeki `data-support` paragrafını aynı adresle güncelleyin. Adres yayımlandığında `privacy/index.html` içindeki henüz yayımlanmadığına ilişkin cümleyi de güncelleyin. Config içine gizli anahtar/token koymayın; tüm dosyalar herkese açıktır.

## Yapı ve tasarım

```text
index.html          Ana sayfa
privacy/index.html  Gizlilik Politikası
terms/index.html    Kullanım Koşulları
contact/index.html  İletişim
404.html            Bulunamayan sayfa
assets/styles.css   Responsive marka tasarımı
assets/site.js      Mobil menü ve destek bağlantısı
assets/config.js    Public destek adresi
assets/favicon.svg OX monogramı
assets/og-image.png Sosyal paylaşım görseli (1200 × 630)
robots.txt
sitemap.xml
CNAME
.nojekyll
```

Harici font, izleme, çerez, kütüphane veya üçüncü taraf istemci isteği yoktur. Sistem fontları, yerel SVG ve küçük PNG kullanılır. OX monogramı ve telefon içindeki HTML/CSS tasviri, verilen lacivert/altın marka yönlendirmesine göre bu repo için hazırlanmıştır; mobil uygulamanın özgün logo dosyası veya ekran görüntüsü sağlanmamıştır. Önizleme temsili olarak etiketlenmiştir; gerçek müşteri verisi içermez. CTA’lar çalışan sayfa/bölüm bağlantılarıdır; sahte mağaza bağlantısı yoktur.

## Yayın kontrolü

- Desktop, tablet, telefon ve %200 metin büyütmede taşma, menü ve bağlantıları kontrol edin.
- Tab / Shift+Tab, görünür odak, içeriğe geç bağlantısı ve mobil menüde Escape davranışını kontrol edin.
- JavaScript kapalıyken metinlerin, alt menünün ve ana gezinmenin çalıştığını kontrol edin.
- Tüm canonical / Open Graph adresleri ve sitemap üretim alan adını kullanır.
- Politikalar hukuki danışmanlık değildir; gerçek ürün ve veri akışı değiştikçe güncellenmelidir.
