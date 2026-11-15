# İzibiz API Catalog

Source: https://dev.izibiz.com.tr/
Companion rule: `.cursor/rules/izibiz-edonusum.mdc`
Machine-readable: `api_ref.json` (guides + SOAP ops + endpoint schemas).

## Kimlik Doğrulama ve Mükellef

Kimlik Doğrulama ve Mükellef

### Başlarken

- **Guide:** [Genel Bilgilendirme](https://dev.izibiz.com.tr/guide/kimlik-dogrulama-baslarken/kimlik-dogrulama-genel-bilgilendirme)
  - Kimlik Doğrulama servisi, entegrasyon sürecinin ilk adımıdır. Yapılan her işlem mutlaka aktif bir oturum ile gerçekleştirilmelidir.
- **Guide:** [Dikkat Edilmesi Gereken Hususlar](https://dev.izibiz.com.tr/guide/kimlik-dogrulama-baslarken/kimlik-dogrulama-dikkat-edilmesi-gereken-hususlar)
  - Uygulamanızı tasarlarken aşağıdaki hususlara dikkat edilmelidir.
### Kimlik Doğrulama

#### SOAP-WS

Kimlik Doğrulama SOAP Webservice

- **SOAP** [AuthenticationWS](https://dev.izibiz.com.tr/soap/kimlik-soap-webservice/authenticationws-auth)
  - WSDL: `https://efaturatest.izibiz.com.tr/AuthenticationWS?wsdl`
  - [Oturum Açma (Login)](https://dev.izibiz.com.tr/soap/kimlik-soap-webservice/authenticationws-auth/oturum-acma-login)
    - * Web servis istemcisinin(client) özel entegratör platformuna kimlik doğrulayarak giriş yapmasını sağlar. * Bu servise giriş için kullanılan kullanıcı bilgileri, portale giriş için kullanılan kullanıcı bilgileri ile aynıdır. * **Login** işleminden dönen işlem ID parametresi daha 
    - Params: REQUEST_HEADER*, USER_NAME*, PASSWORD*
#### Auth REST API

Kimlik Doğrulama API

- **POST** [Oturum Açma - v1/auth/token](https://dev.izibiz.com.tr/endpoint/authentication-api/auth-token) — `{{baseUrl}}/{{v1}}/auth/token`
  - Login endpoint; token at `data.accessToken` → env `None`
  - Body (json): username*, password*
- **POST** [Müşteri Olarak Token Alma](https://dev.izibiz.com.tr/endpoint/authentication-api/musteri-olarak-token-alma) — `{{baseUrl}}/{{version}}/auth/token`
  - Body (json): username, password
- **POST** [Kanal Olarak Token Alma](https://dev.izibiz.com.tr/endpoint/authentication-api/kanal-olarak-token-alma) — `{{baseUrl}}/{{version}}/auth/token`
  - Body (json): username, password
- **POST** [Satış Olarak Token Alma](https://dev.izibiz.com.tr/endpoint/authentication-api/satis-olarak-token-alma) — `{{baseUrl}}/{{version}}/auth/token`
  - Body (json): username, password
- **POST** [Destek Olarak Token Alma](https://dev.izibiz.com.tr/endpoint/authentication-api/destek-olarak-token-alma) — `{{baseUrl}}/{{version}}/auth/token`
  - Body (json): username, password
- **PUT** [Token Uzatma](https://dev.izibiz.com.tr/endpoint/authentication-api/token-uzatma) — `{{baseUrl}}/{{version}}/auth/token`
### GİB Kayıtlı Mükellef

GİB sisteminde kayıtlı mükelleflerin tekil veya toplu sorgulanamasını sağlar

#### SOAP WS

- **SOAP** [AuthenticationWS-GIBUser](https://dev.izibiz.com.tr/soap/soap-ws/authenticationws-gi-buser)
  - WSDL: `https://efaturatest.izibiz.com.tr/AuthenticationWS?wsdl`
  - [Mükellef Sorgulama (CheckUser)](https://dev.izibiz.com.tr/soap/soap-ws/authenticationws-gi-buser/mukellef-sorgulama-checkuser)
    - * Mükellefin, Gelir İdaresi Başkanlığı sistemine kayıtlı olup olmadığının kontrol edildiği servistir. * Sorgulanan VKN GİB sistemine kayıtlıysa, sistemde tanımlanmış etiket listesi dönülmektedir. * Sorgulanan VKN GİB sistemine kayıtlı değilse liste boş dönülür. **Sonuç boş ise fi
    - Params: REQUEST_HEADER*, USER*, DOCUMENT_TYPE*
  - [Mükellef Listesi Dosyası Çekme (GetGibUserList)](https://dev.izibiz.com.tr/soap/soap-ws/authenticationws-gi-buser/mukellef-listesi-dosyasi-cekme-getgibuserlist)
    - E-Fatura ve E-İrsaliye sistemine kayıtlı firmalara ait GB/PK etiketlerinin sıkıştırılmış olarak istenilen tipte dönüldüğü servistir.  Servisten dönen parametreler şu şekildedir:  Parametre | Tip        | Açıklama --------- | ----------- | ----------- **CONTENT** | Base64Encoded |
    - Params: REQUEST_HEADER*, TYPE, DOCUMENT_TYPE, REGISTER_TIME_START, ALIAS_TYPE, ALIAS_MODIFY_DATE
#### REST API

- **GET** [Nace - Faaliyet Sorgulama Servisi](https://dev.izibiz.com.tr/endpoint/gib-user-services-rest-api/nace-faaliyet-sorgulama-servisi) — `{{baseUrl}}/v2/taxpayers/{vkn}`
  - Query: includeActivities, enforceFromGib, documentDate
- **GET** [Mükellef Listesini Zip Olarak İndir](https://dev.izibiz.com.tr/endpoint/gib-user-services-rest-api/gib-users-binary) — `{{baseUrl}}/{{version}}/resources/gib-users/binary`
  - GİB e-Fatura kayıtlı kullanıcı listesinin tamamını zip dosyası olarak indirir. Tekil mükellef sorgulama için SOAP tarafındaki `AuthenticationWS-GIBUser` servisi kullanılır.

## E-Fatura ve E-Arşiv

E-Fatura ve E-Arşiv Webservisi

### Başlarken

Genel Bilgilendirme

- **Guide:** [Genel Bilgilendirme](https://dev.izibiz.com.tr/guide/e-fatura-baslarken/e-fatura-genel-bilgilendirme)
  - e-Fatura servisi, e-fatura mükellefinin fatura gönderimini ve gelen faturaları kendi sistemine çekmesini sağlayan web servis uygulamasıdır.
- **Guide:** [Dikkat Edilmesi Gereken Hususlar](https://dev.izibiz.com.tr/guide/e-fatura-baslarken/e-fatura-dikkat-edilmesi-gereken-hususlar)
  - Uygulamanızı tasarlarken aşağıdaki hususlara dikkat edilmelidir.
### E-Fatura

E-Fatura : E-Fatura sistemine kayıtlı firmalara fatura düzenlemek için kullanılan servistir. Fatura alıcısının e-Fatura mükellef listesinde kayıtlı olup olmadığı kontrol edilmelidir.

#### E-Fatura REST API

##### E-Fatura API - v1

- **POST** [Fatura Gönderme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/e-fatura-rest-api) — `{{baseUrl}}/{{version}}/einvoices`
  - JSON gövde ile e-Fatura gönderir.

**Önemli:** Her gönderimde `content.uuid` ve `content.documentNo` **benzersiz** olmalıdır. Aşağıdaki senaryodaki değerler doğrulama amacıyla bir kez kullanılmıştır; tekrar gönderirken bu iki alanı değiştirin. `assig
  - Body (json): documentAction, assignNumber, seriePrefix, selectedSeriesId, xsltName, compressed, mailFlag, mailAddress, schematronControl, sendingType, ecommerceUpload, receiverAlias
- **GET** [Gelen e-Fatura Listeleme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-list) — `{{baseUrl}}/{{v1}}/einvoices/inbox`
  - Query: dateType*, startDate, endDate, status, page*, pageSize*, sortProperty, sort
- **POST** [Taslak - UBL Gönderme Numara Ata Kaydet](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/taslak-ubl-gonderme-numara-ata-kaydet) — `{{baseUrl}}/{{version}}/einvoices/ubl`
  - Body (json): assignNumber, seriePrefix, compressed, documentAction, content
- **GET** [Giden e-Fatura Listeleme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-list) — `{{baseUrl}}/{{v1}}/einvoices/outbox`
  - Query: uuid, dateType, startDate, endDate, status, page, pageSize, sortProperty, sort
- **GET** [Gelen e-Fatura Durumları (Lookup Status)](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-lookup-statuses) — `{{baseUrl}}/{{v1}}/einvoices/inbox/lookup-statuses`
  - Gelen e-Fatura listeleme servisinde `status` parametresine verilebilecek durum kodlarını döner.

Doğrulandı: 200, 7 durum kodu döndü. e-Fatura bu eski yolu kullanmaya devam eder; diğer ürünlerdeki `{{v2}}/{ürün}/lookup/{scope}` deseni e-Fatura'da 403
- **GET** [Giden e-Fatura Durumları (Lookup Status)](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-lookup-statuses) — `{{baseUrl}}/{{v1}}/einvoices/outbox/lookup-statuses`
  - Giden e-Fatura listeleme servisinde `status` parametresine verilebilecek durum kodlarını döner.

Doğrulandı: 200, 19 durum kodu döndü. e-Fatura bu eski yolu kullanmaya devam eder; diğer ürünlerdeki `{{v2}}/{ürün}/lookup/{scope}` deseni e-Fatura'da 40
- **GET** [Gelen e-Fatura Görüntüleme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-preview) — `{{baseUrl}}/{{v1}}/einvoices/inbox/{id}/preview/{format}`
  - `{id}` gelen fatura kaydının id değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).
- **POST** [Gelen e-Fatura İndirme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-download) — `{{baseUrl}}/{{v1}}/einvoices/inbox/download/{format}`
  - `{format}` indirme biçimidir (pdf, ubl, html). Gövdede indirilecek gelen fatura id listesi gönderilir.
- **GET** [Giden e-Fatura Görüntüleme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-preview) — `{{baseUrl}}/{{v1}}/einvoices/outbox/{id}/preview/{format}`
  - `{id}` giden fatura kaydının id değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).
- **POST** [Giden e-Fatura İndirme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-download) — `{{baseUrl}}/{{v1}}/einvoices/outbox/download/{format}`
  - `{format}` indirme biçimidir (pdf, ubl, html). Gövdede indirilecek giden fatura id listesi gönderilir.
- **POST** [Giden e-Fatura Toplu Önizleme](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-bulk-preview) — `{{baseUrl}}/{{v1}}/einvoices/outbox/preview`
  - Birden fazla giden faturanın önizlemesini tek istekte alır. Gövdede id listesi gönderilir.
- **POST** [Giden e-Fatura Satır Yükleme (Excel Ayrıştırma)](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/outgoing-invoice-import-parse) — `{{baseUrl}}/{{v1}}/einvoices/outbox/import/parse`
  - Excel dosyasını ayrıştırıp fatura satırlarının önizlemesini döner; kayıt oluşturmaz.
  - Body (json): documentType*, type*, compressed, content*
- **POST** [Gelen e-Fatura Okundu/Okunmadı Yapma](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-read-flag) — `{{baseUrl}}/{{v1}}/einvoices/inbox/{flagType}-read-flag/{status}`
  - `{flagType}`: portal | erp, `{status}`: READ | UNREAD. Gövdede işlem yapılacak belgeler id, documentUuid veya documentNo ile belirtilebilir.
- **POST** [Gelen e-Fatura Yanıtlama (Kabul/Red)](https://dev.izibiz.com.tr/endpoint/einvoice-v1-api/incoming-invoice-response) — `{{baseUrl}}/{{v1}}/einvoices/inbox/{id}/response`
  - Ticari faturaya kabul veya red yanıtı gönderir. `{id}` gelen fatura kaydının id değeridir. Red işleminde `description` zorunludur.
##### E-Fatura API - v2

- **POST** [e-Fatura Gönderme (v2)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-einvoice-send) — `{{baseUrl}}/{{v2}}/einvoices/send`
  - JSON gövde ile e-Fatura gönderir. Belge içeriği `content` nesnesinde taşınır.
  - Body (json): isVuk507, mailFlag, mailAdress, xsltName, compressed, seriePrefix, assignNumber, content*
- **POST** [e-Arşiv Yükleme (v2)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-earchive-load) — `{{baseUrl}}/{{v2}}/einvoices/load`
  - JSON gövde ile e-Arşiv faturası yükler. XSLT eki `additionalReferences` içinde Base64 olarak gönderilir; örnekte içerik yer tutucu ile kısaltılmıştır.
  - Body (json): assignNumber, compressed, mailFlag, mailAdress, content*
- **POST** [Gelen Belge Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-inbox-check-status) — `{{baseUrl}}/{{v2}}/einvoices/inbox/check-status`
  - Gövdede verilen UUID listesi için gelen belgelerin durumunu toplu sorgular. Tek belge için `GET {{baseUrl}}/{{v2}}/einvoices/inbox/{uuid}/check-status` kullanılabilir.
- **POST** [Giden Belge Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-check-status) — `{{baseUrl}}/{{v2}}/einvoices/outbox/check-status`
  - Gövdede verilen UUID listesi için giden belgelerin durumunu toplu sorgular. Tek belge için `GET {{baseUrl}}/{{v2}}/einvoices/outbox/{uuid}/check-status` kullanılabilir.
- **GET** [Gelen Belge Tekil Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-inbox-check-status-single) — `{{baseUrl}}/{{v2}}/einvoices/inbox/{uuid}/check-status`
  - Tek bir gelen belgenin durumunu döner. `{uuid}` belge UUID değeridir.
- **GET** [Giden Belge Tekil Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-check-status-single) — `{{baseUrl}}/{{v2}}/einvoices/outbox/{uuid}/check-status`
  - Tek bir giden belgenin durumunu döner. `{uuid}` belge UUID değeridir.
- **GET** [Gelen Belge Görüntüleme](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-inbox-view) — `{{baseUrl}}/{{v2}}/einvoices/inbox/{uuid}/view/{format}`
  - `{uuid}` belge UUID değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).
- **POST** [Gelen Belge İndirme](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-inbox-download) — `{{baseUrl}}/{{v2}}/einvoices/inbox/download/{format}`
  - `{format}` indirme biçimidir (html, pdf, ubl). Gövdede indirilecek belgelerin UUID listesi gönderilir.
- **GET** [Giden Belge Görüntüleme (ID ile)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-preview-by-id) — `{{baseUrl}}/{{v2}}/einvoices/outbox/{id}/preview/{format}`
  - `{id}` giden belge kaydının id değeri, `{format}` görüntüleme biçimidir (html, pdf).
- **GET** [Giden Belge Görüntüleme (UUID ile)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-view-by-uuid) — `{{baseUrl}}/{{v2}}/einvoices/outbox/{uuid}/view/{format}`
  - `{uuid}` belge UUID değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).
- **POST** [Giden Belge İndirme](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-download) — `{{baseUrl}}/{{v2}}/einvoices/outbox/download/{format}`
  - `{format}` indirme biçimidir (html, pdf, ubl). Gövdede indirilecek belgelerin UUID listesi gönderilir.
- **POST** [Sistemde Olmayan Belge Önizleme (UBL)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-preview-ubl) — `{{baseUrl}}/{{v2}}/einvoices/outbox/preview/ubl/{format}`
  - Sisteme kayıtlı olmayan bir belgenin UBL içeriğinden önizleme üretir. `{format}`: html, pdf, ubl.
  - Body (json): compressed, xsltName, content*
- **POST** [Sistemde Olmayan Belge Önizleme (JSON)](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-outbox-preview-json) — `{{baseUrl}}/{{v2}}/einvoices/outbox/preview/{format}`
  - Sisteme kayıtlı olmayan bir belgenin JSON içeriğinden önizleme üretir. `{format}`: html, pdf, ubl. Gövde yapısı `e-Fatura Gönderme (v2)` ucundaki `content` ile aynıdır.
  - Body (json): compressed, xsltName, content*
- **GET** [Taslak Belge Görüntüleme](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-draft-view) — `{{baseUrl}}/{{v2}}/einvoices/draft/{idOrUuid}/view/{format}`
  - `{idOrUuid}` taslak kaydının id ya da UUID değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).
- **POST** [Taslak Belge İndirme](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-draft-download) — `{{baseUrl}}/{{v2}}/einvoices/draft/download/{format}`
  - `{format}` indirme biçimidir (html, pdf, ubl). Gövdede indirilecek taslak belgelerin UUID listesi gönderilir.
- **DELETE** [e-Arşiv İptal](https://dev.izibiz.com.tr/endpoint/einvoice-v2-api/v2-earchive-cancel) — `{{baseUrl}}/{{v2}}/einvoices/cancel`
  - Gövdede verilen UUID listesindeki e-Arşiv faturalarını iptal eder.
#### SOAP WS

- **SOAP** [E-Fatura WS (EInvoiceWS)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews)
  - WSDL: `https://efaturatest.izibiz.com.tr/EInvoiceWS?wsdl`
  - [Fatura Gönderme (SendInvoice)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-gonderme-sendinvoice)
    - * Tekli veya çoklu fatura gönderimini destekler. * Bu işlemden sonra gönderilen faturaların durumları GetInvoiceStatus servisi ile kontrol edilmelidir. * Faturanın durumu GIB’de hatalı olduğu zaman bu servis ile faturayı aynı fatura numarası ve aynı ETTN ile tekrar gönderilebilir
    - Params: REQUEST_HEADER*, SENDER, RECEIVER, XSLT_NAME, SERI_PREFIX, DISABLE_DATE_CONTROL, INVOICE*, ECOMMERCE_UPLOAD
  - [Taslak Fatura Yükleme (LoadInvoice)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/taslak-fatura-yukleme-loadinvoice)
    - * FATURA Entegrasyon Platformu üzerinden 1 yada daha fazla faturayı E-Fatura sistemine yükler. * Eğer fatura numarası atanmışsa (16 hane ise) şema ve şematron kontrolünden geçirilir. Fatura numarası atanmamışsa şema ve şematron kontrolü yapılmaz. * Aynı faturanın tekrar yüklenme
    - Params: REQUEST_HEADER*, INVOICE*
  - [Fatura Listeleme (GetInvoice)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-listeleme-getinvoice)
    - * E-Fatura sisteminde satış (giden) veya alış (gelen) faturaların üst başlık ve dosyalarını sorgulamak için kullanılır.
    - Params: REQUEST_HEADER*, INVOICE_SEARCH_KEY*, HEADER_ONLY
  - [Fatura Durum Sorgulama (GetInvoiceStatus)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-durum-sorgulama-getinvoicestatus)
    - * E-Fatura sisteminde bulunan bir veya birden fazla taslak, gelen ve giden faturaların durumunu sorgulamayı sağlayan servistir.
    - Params: REQUEST_HEADER*, MARK
  - [Fatura Görüntüleme (GetInvoiceWithType)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-goruntuleme-getinvoicewithtype)
    - * E-Fatura sisteminden bulunan bir faturanın görselini çekmek için tasarlanmış servistir. * Faturaların HTML ve PDF görsellerini çekebilirsiniz. * Fatura görseli içerisinde ki XSLT ile yapılacaktır. Eğer fatura içerisinde ki şablonda sorun varsa hata fırlatılacaktır. * İçerik sık
    - Params: REQUEST_HEADER*, INVOICE_SEARCH_KEY*, HEADER_ONLY
  - [Fatura Alındı/Okundu İşaretleme (MarkInvoice)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-alindi-okundu-i-saretleme-markinvoice)
    - * E-Fatura sisteminde bir veya birden fazla faturayı alındı/alınmadı olarak işaretlemek için geliştirilmiş servistir. * GetInvoice servisi ile müşteri ortamına başarı alınan faturaların tekrar sorgulandığında listede gelmemesi için MarkInvoice servisi ile alındı olarak işaretlenm
    - Params: REQUEST_HEADER*, MARK
  - [Fatura Durum Sorgulama (GetInvoiceStatusAll)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/fatura-durum-sorgulama-getinvoicestatusall)
    - * E-Fatura sisteminde bulunan bir veya birden fazla taslak, gelen ve giden faturaların durumunu sorgulamayı sağlayan servistir.  Servisten dönen parametreler şu şekildedir:  Parametre | Tip        | Açıklama --------- | ----------- | ----------- **INVOICE_STATUS** | ComplexType |
    - Params: REQUEST_HEADER*, UUID*
  - [Ticari Faturaya Yanıt Gönderme (SendInvoiceResponseWithServerSign)](https://dev.izibiz.com.tr/soap/efatura-soap-webservice/einvoicews/ticari-faturaya-yanit-gonderme-sendinvoiceresponsewithserversign)
    - Params: REQUEST_HEADER*, STATUS*, INVOICE*, DESCRIPTION*
### E-Arşiv

E-Arşiv Fatura : E-Fatura sistemine kayıtlı olmayan firmalara veya nihai tüketicilere fatura düzenlemek için kullanılan servistir. Fatura alıcısının e-Fatura mükellef listesinde kayıtlı ise bu servis kullanılmamalıdır.

#### Başlarken

- **Guide:** [Genel Bilgilendirme](https://dev.izibiz.com.tr/guide/e-arsiv-baslarken/e-arsiv-genel-bilgilendirme)
  - E-Arşiv Fatura servisi, e-Fatura mükellefi olmayan firmalara veya nihai tüketiciye düzenlenen faturaların özel entegratör sistemine gönderilmesini ve GİB'e raporlanmasını sağlayan web servis uygulamasıdır.
- **Guide:** [Dikkat Edilmesi Gereken Hususlar](https://dev.izibiz.com.tr/guide/e-arsiv-baslarken/e-arsiv-dikkat-edilmesi-gereken-hususlar)
  - Uygulamanızı tasarlarken aşağıdaki hususlara dikkat edilmelidir.
- **Guide:** [Gelen E-Arşiv Fatura – Ön Koşullar](https://dev.izibiz.com.tr/guide/e-arsiv-baslarken/gelen-earsiv-on-kosullar)
  - GİB İnteraktif Vergi Dairesi (5.000/30.000 portalı) üzerinden müşterilerimize kesilen **gelen e-Arşiv Fatura** belgeleri, **Gelen E-Arşiv Fatura** servisleri ile API üzerinden listelenebilir, görüntülenebilir ve indirilebilir.
#### E-Arşiv REST API

- **POST** [E-Arşiv Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-send-json) — `{{baseUrl}}/{{version}}/earchives`
  - JSON gövde ile e-Arşiv faturası gönderir. Belge tipi `content.documentTypeCode`, gönderim şekli `additionalReferences` içindeki `SendingType` ve `EArchiveType` ile belirlenir.

**Önemli:** Her gönderimde `content.uuid` ve `content.documentNo` **benze
  - Body (json): documentAction, assignNumber, seriePrefix, xsltName, mailFlag, mailAdress, content
- **GET** [E-Arşiv Listeleme](https://dev.izibiz.com.tr/endpoint/rest-api2/e-arsiv-listeleme) — `{{baseUrl}}/{{v1}}/earchives`
  - Query: dateType, pageSize, page, sort, startDate, direction
- **POST** [E-Arşiv Gönderme (einvoices/send ile)](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-send-via-einvoices) — `{{baseUrl}}/{{version}}/einvoices/send`
  - e-Arşiv faturasını e-Fatura gönderim ucu üzerinden gönderir. `content.profile` = EARSIVFATURA verilir. Aynı belge `POST {{baseUrl}}/{{version}}/earchives` ile de gönderilebilir.
  - Body (json): xsltName, assignNumber, seriePrefix, compressed, isVuk507, mailFlag, content*
- **GET** [E-Arşiv Fatura Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-status-query) — `{{baseUrl}}/{{version}}/earchives`
  - Belge numarası (`documentNo`) verilen e-Arşiv faturasını sorgular ve durum bilgisini döner.

Sorgulanacak belge numarasını **Query** sekmesindeki `documentNo` alanına yazın; istek o numarayla gönderilir (ör. `UAB2026000002990`).

Yanıttaki `data.cont
  - Query: documentNo*
- **POST** [UBL ile E-Arşiv Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-send-ubl) — `{{baseUrl}}/{{version}}/earchives/ubl`
  - Hazır UBL içeriğini Base64 olarak gönderir.
  - Body (json): compressed, content*
- **POST** [E-Arşiv Fatura İndirme - UBL](https://dev.izibiz.com.tr/endpoint/rest-api2/e-arsiv-fatura-i-ndirme-ubl) — `{{baseUrl}}/{{version}}/earchives/download/ubl`
- **GET** [E-Arşiv Fatura Görüntüleme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-preview) — `{{baseUrl}}/{{version}}/earchives/{id}/preview/{format}`
  - `{id}` e-Arşiv fatura kaydının id değeri, `{format}` görüntüleme biçimidir (html, pdf).
- **GET** [E-Arşiv Fatura UBL Sorgulama](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-get-ubl) — `{{baseUrl}}/{{version}}/earchives/{id}/ubl`
  - Belgenin UBL içeriğini döner. `{id}` e-Arşiv fatura kaydının id değeridir.
- **GET** [E-Arşiv Fatura XML Çekme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-get-xml) — `{{baseUrl}}/{{version}}/earchives/{id}/xml`
  - Belgenin ham XML içeriğini döner. `{id}` e-Arşiv fatura kaydının id değeridir.
- **POST** [E-Arşiv Fatura İndirme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-download) — `{{baseUrl}}/{{version}}/earchives/download/{format}`
  - `{format}` indirme biçimidir (ubl, html, pdf). Gövdede indirilecek belgelerin id listesi gönderilir. UBL indirme için kategorideki ayrı endpoint de kullanılabilir.
- **POST** [UBL ile Belge Görüntüleme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-preview-ubl-v2) — `{{baseUrl}}/{{v2}}/earchives/outbox/preview/ubl/{format}`
  - Sistemde kayıtlı olmayan bir belgenin UBL içeriğinden önizleme üretir. `{format}`: html, pdf, ubl.
  - Body (json): compressed, xsltName, content*
- **POST** [JSON ile Belge Görüntüleme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-preview-json-v2) — `{{baseUrl}}/{{v2}}/earchives/outbox/preview/{format}`
  - Sistemde kayıtlı olmayan bir belgenin JSON içeriğinden önizleme üretir. `{format}`: html, pdf, ubl.
  - Body (json): compressed, xsltName, content*
- **POST** [Şema-Şematron Kontrolü](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-validate) — `{{baseUrl}}/{{version}}/earchives/validate`
  - Gönderim öncesi UBL içeriğini şema ve şematron kurallarına göre doğrular.
  - Body (json): compressed, content*
- **POST** [İçe Aktarma Önizleme (Excel)](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-import-parse) — `{{baseUrl}}/{{version}}/earchives/import/parse`
  - Excel dosyasını ayrıştırıp içe aktarılacak belgelerin önizlemesini döner.
  - Body (json): documentType*, type*, compressed, content*
- **GET** [Gelen E-Arşiv Fatura Listeleme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-inbox-list) — `{{baseUrl}}/{{v2}}/earchives/inbox`
  - Gelen belgeleri sayfalı olarak listeler. Tüm filtreler opsiyoneldir.

Yanıttaki `id` değeri; **Gelen E-Arşiv Fatura Görüntüleme** ve **Gelen E-Arşiv Fatura İndirme** servislerinde belge kimliği olarak, `portalReadStatus` ise belgenin portalda okunup 
  - Query: startDate, endDate, page, pageSize, documentNo, uuid, senderIdentifier, portalReadStatus
- **GET** [Gelen E-Arşiv Fatura Görüntüleme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-inbox-view) — `{{baseUrl}}/{{v2}}/earchives/inbox/{{earchiveInboxId}}/view/{{inboxViewFormat}}`
  - GİB İnteraktif Vergi Dairesi (5.000/30.000 portalı) üzerinden müşterilerimize kesilen **gelen e-Arşiv Fatura** belgeleri için kullanılır.

Tek bir gelen belgeyi HTML, PDF veya UBL (XML) olarak görüntüler. Görüntüleme formatı hazır senaryolardan seçil
- **POST** [Gelen E-Arşiv Fatura İndirme](https://dev.izibiz.com.tr/endpoint/rest-api2/earchive-inbox-download) — `{{baseUrl}}/{{v2}}/earchives/inbox/download/{{inboxDownloadFormat}}`
  - GİB İnteraktif Vergi Dairesi (5.000/30.000 portalı) üzerinden müşterilerimize kesilen **gelen e-Arşiv Fatura** belgeleri için kullanılır.

Seçilen gelen belgeleri HTML, PDF veya UBL (XML) formatında **zip** dosyası içinde indirir. İndirme formatı haz
  - Body (json): id*
#### SOAP-WS

- **SOAP** [EArşiv WS (EArchiveWS)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews)
  - WSDL: `https://efaturatest.izibiz.com.tr/EIArchiveWS/EFaturaArchive?wsdl`
  - [E-Arşiv Gönderme (WriteToArchiveExtended)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-gonderme-writetoarchiveextended)
    - E-Fatura mükellefi olmayan firma veya nihai tüketiciye düzenlenen faturaların özel entegratör sistemine gönderilmesi ve raporlamasını sağlayan webservis uygulamasıdır.
    - Params: REQUEST_HEADER*, ArchiveInvoiceExtendedContent*
  - [E-Arşiv Fatura Okuma (ReadFromArchive)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-fatura-okuma-readfromarchive)
    - Özel entegratör sistemine gönderilen e-arşiv faturalarının farklı formatlarda (XML,HTML,PDF) okumasını sağlayan servistir.
    - Params: REQUEST_HEADER*, INVOICEID*, PORTAL_DIRECTION*, PROFILE*
  - [E-Arşiv Durum Sorgulama (GetEArchiveStatus)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-durum-sorgulama-getearchivestatus)
    - Özel entegratör platformuna gönderilen bir veya birden çok faturanın durumunu sorgulamayı sağlayan servistir.
    - Params: REQUEST_HEADER*, UUID*
  - [E-Arşiv Fatura İptal (CancelEArchiveInvoice)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-fatura-i-ptal-cancelearchiveinvoice)
    - * Özel entegratör platformuna gönderildikten veya GİB'e raporlandıktan sonra eksik veya hata tespit edilen veya müşteri tarafından iade edilen belgenin GIB'e iptal fatura durumunda raporlanmasını sağlayan servistir. * GİB'e raporlamadan tespit edilmiş bir hata sebebi ile hiç rapo
    - Params: REQUEST_HEADER*, CancelEArsivInvoiceContent*
  - [E-Arşiv Faturasını E-Posta Olarak Tekrar Gönderme (GetEmailEarchiveInvoice)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-faturasini-e-posta-olarak-tekrar-gonderme-getemailearchiveinvoice)
    - * E-Arşiv faturasını yükledikten sonra e-posta olarak aynı veya farklı e-postalara tekrar gönderilmesini sağlayan servistir. * Birden fazla e-postaya göndermek için virgül (,) ile ayırarak gönderilmelidir.
    - Params: REQUEST_HEADER*, FATURA_UUID*, FATURA_ID, EMAIL*
  - [E-Arşiv Fatura Sayılarını Sorgulama (EArchiveInvoiceCount)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-fatura-sayilarini-sorgulama-earchiveinvoicecount)
    - Params: REQUEST_HEADER*, ISSUE_DATE_START, ISSUE_DATE_END, CDATE_START, CDATE_END
  - [E-Arşiv Rapor Listesini Çekme (GetEArchiveReport)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-rapor-listesini-cekme-getearchivereport)
    - Özel entegratör platformunda mükellefe ait oluşturulan bir döneme ait rapor listesini çekmek için kullanılır. Bu servis sadece rapor listesini döndecektir. Servisin döndüğü raporlara ait içerikleri almak için ReadEArchiveReport servisi kullanılabilir.
    - Params: REQUEST_HEADER*, REPORT_PERIOD*, REPORT_STATUS_FLAG*
  - [E-Arşiv Rapor Çekme (ReadEArchiveReport)](https://dev.izibiz.com.tr/soap/soap-ws2/earchivews/e-arsiv-rapor-cekme-readearchivereport)
    - Mükellef için GİB'e gönderilen raporun imzalı XML dosyasını okumayı sağlayan servistir
    - Params: REQUEST_HEADER*, RAPOR_NO*

## E-İrsaliye

### Başlarken

- **Guide:** [Genel Bilgilendirme](https://dev.izibiz.com.tr/guide/e-irsaliye-baslarken/e-irsaliye-genel-bilgilendirme)
  - e-İrsaliye servisi, irsaliye gönderimini sağlayan web servis uygulamasıdır.
- **Guide:** [Dikkat Edilmesi Gereken Hususlar](https://dev.izibiz.com.tr/guide/e-irsaliye-baslarken/e-irsaliye-dikkat-edilmesi-gereken-hususlar)
  - E-İrsaliye uygulamanızı tasarlarken aşağıdaki hususlara dikkat edilmelidir.
### E-İrsaliye REST API

- **POST** [Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-durum-sorgulama) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/check-status`
  - `{{despatchDirection}}` yön bilgisidir: `outbox` (giden) veya `inbox` (gelen). Değeri seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebilirsiniz. Bu segment zorunludur; verilmezse servis 403 döner.
- **GET** [E-İrsaliye Listeleme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-listeleme) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}`
  - `{{despatchDirection}}` yön bilgisidir: `outbox` (giden) veya `inbox` (gelen). Değeri seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebilirsiniz. Bu segment zorunludur; verilmezse servis 403 döner.
  - Query: direction, startDate, endDate, page, pageSize, sortProperties
- **POST** [Okundu/Okunmadı Yapma](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-okundu-okunmadi-yapma) — `{{baseUrl}}/{{v2}}/edespatches/inbox/{flagType}-read-flag/{status}`
- **GET** [Belge Görüntüleme (HTML)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-goruntuleme) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/{{despatchId}}/view/html`
  - Belgeyi **HTML** formatında görüntüler.

Yoldaki değerler seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebilirsiniz:

- `{{despatchDirection}}`: yön bilgisi, `outbox` (giden) veya `inbox` (gelen). Bu segment zo
- **GET** [Belge Görüntüleme (PDF)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-goruntuleme-pdf) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/{{despatchId}}/view/pdf`
  - Belgeyi **PDF** formatında görüntüler.

Yoldaki değerler seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebilirsiniz:

- `{{despatchDirection}}`: yön bilgisi, `outbox` (giden) veya `inbox` (gelen). Bu segment zor
- **GET** [Belge Görüntüleme (UBL)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-goruntuleme-ubl) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/{{despatchId}}/view/ubl`
  - Belgeyi **UBL** formatında görüntüler.

Yoldaki değerler seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebilirsiniz:

- `{{despatchDirection}}`: yön bilgisi, `outbox` (giden) veya `inbox` (gelen). Bu segment zor
- **POST** [Belge İndirme (HTML)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-indirme) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/download/html`
  - Gövdede gönderilen id listesindeki belgeleri **HTML** formatında indirir.

`{{despatchDirection}}` yön bilgisidir: `outbox` (giden) veya `inbox` (gelen). Değeri seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebi
- **POST** [Belge İndirme (PDF)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-indirme-pdf) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/download/pdf`
  - Gövdede gönderilen id listesindeki belgeleri **PDF** formatında indirir.

`{{despatchDirection}}` yön bilgisidir: `outbox` (giden) veya `inbox` (gelen). Değeri seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebil
- **POST** [Belge İndirme (UBL)](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-indirme-ubl) — `{{baseUrl}}/{{v2}}/edespatches/{{despatchDirection}}/download/ubl`
  - Gövdede gönderilen id listesindeki belgeleri **UBL** formatında indirir.

`{{despatchDirection}}` yön bilgisidir: `outbox` (giden) veya `inbox` (gelen). Değeri seçili ortamın değişkenlerinden gelir; portalda ortam değişkenleri panelinden değiştirebil
- **POST** [Giden Belge UBL İndirme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-giden-belge-ubl-indirme) — `{{baseUrl}}/{{v2}}/edespatches/outbox/download/ubl`
- **POST** [Belge Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-belge-gonderme) — `{{baseUrl}}/{{v2}}/edespatches/send`
  - JSON gövde ile e-İrsaliye gönderir.

**Görüntüleme şablonu zorunludur.** İki yoldan biri kullanılır: gövdeye `xsltName` alanı eklenir (örn. `DEFAULT`), ya da `content.additionalReferences` içinde `documentType: "XSLT"` kaydıyla şablon Base64 olarak g
- **POST** [UBL ile Belge Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-ubl-ile-belge-gonderme) — `{{baseUrl}}/{{v2}}/edespatches/send/ubl`
- **POST** [Sistemde Olmayan Belgenin Önizlemesi](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-sistemde-olmayan-belgenin-onizlemesi) — `{{baseUrl}}/v2/edespatches/outbox/preview/ubl/{format}`
- **POST** [Şema-Şematron Kontrolü](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-sema-sematron-kontrolu) — `{{baseUrl}}/{{v2}}/edespatches/outbox/validate`
  - Gönderilecek e-İrsaliye belgesinin şema ve şematron kontrolünün yapılması.
- **POST** [İçe Aktarma Önizleme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-ice-aktarma-onizleme) — `{{baseUrl}}/v2/edespatches/import/parse`
  - Excel veya XML formatındaki e-İrsaliye belgesinin içe aktarılmadan önce ayrıştırılıp önizlemesinin alınması.
- **POST** [Giden Belge Satır Yükleme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-giden-belge-satir-yukleme) — `{{baseUrl}}/{{version}}/edespatches/outbox/import/parse`
  - Excel dosyasındaki satırların giden e-İrsaliye belgesi olarak sisteme yüklenmesi.
- **POST** [E-İrsaliye Yanıtı Durum Sorgulama](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-durum-sorgulama) — `{{baseUrl}}/{{v2}}/edespatch-responses/{direction}/check-status`
  - Gönderilen e-İrsaliye yanıtının işlem durumunun sorgulanması.

`{direction}` yön bilgisidir: `inbox` (gelen) veya `outbox` (giden). Bu segment zorunludur; verilmezse servis 403 döner.
- **GET** [E-İrsaliye Yanıtı Listeleme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-listeleme) — `{{baseUrl}}/{{v2}}/edespatch-responses/{direction}`
  - Gelen veya giden e-İrsaliye yanıtlarının filtrelenerek listelenmesi.

`{direction}` yön bilgisidir: `inbox` (gelen) veya `outbox` (giden). Bu segment zorunludur; verilmezse servis 403 döner.
  - Query: directionType*, startDate, endDate, page, pageSize, sort, sortProperty, status
- **GET** [E-İrsaliye Yanıtı Belge Görüntüleme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-belge-goruntuleme) — `{{baseUrl}}/{{v2}}/edespatch-responses/{direction}/{id}/view/{format}`
  - `{id}` yanıt kaydının id değeri, `{format}` görüntüleme biçimidir (html, pdf, ubl).

`{direction}` yön bilgisidir: `inbox` (gelen) veya `outbox` (giden). Bu segment zorunludur; verilmezse servis 403 döner.
- **POST** [E-İrsaliye Yanıtı Belge İndirme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-belge-indirme) — `{{baseUrl}}/{{v2}}/edespatch-responses/{direction}/download/{format}`
  - `{format}` indirme biçimidir (ubl, html, pdf). Gövdede indirilecek yanıtların id listesi gönderilir.

`{direction}` yön bilgisidir: `inbox` (gelen) veya `outbox` (giden). Bu segment zorunludur; verilmezse servis 403 döner.
- **POST** [E-İrsaliye Yanıtı Okundu/Okunmadı Yapma](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-okundu-okunmadi-yapma) — `{{baseUrl}}/{{v2}}/edespatch-responses/{flagType}-read-flag/{status}`
  - Gelen e-İrsaliye yanıtının Portal veya ERP tarafında okundu/okunmadı olarak işaretlenmesi.
- **POST** [E-İrsaliye Yanıtı Belge Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-belge-gonderme) — `{{baseUrl}}/{{v2}}/edespatch-responses/send`
  - JSON gövde ile e-İrsaliye yanıtı gönderir.

**Yanıt verilecek irsaliye** `content.despatchDocumentReference` alanında belirtilir. Bu alan **dizi** olmalıdır; nesne olarak gönderilirse servis JSON ayrıştırma hatası verir. Her öğe `id` (yanıtlanan irsa
- **POST** [E-İrsaliye Yanıtı UBL ile Belge Gönderme](https://dev.izibiz.com.tr/endpoint/rest-api3/e-irsaliye-yaniti-ubl-ile-belge-gonderme) — `{{baseUrl}}/{{v2}}/edespatch-responses/send/ubl`
  - UBL formatında e-İrsaliye yanıtı belgesinin gönderilmesi.
### SOAP WS

- **SOAP** [E-İrsaliye (EIrsaliyeWS)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye)
  - WSDL: `https://efaturatest.izibiz.com.tr/EIrsaliyeWS/EIrsaliye?wsdl`
  - [E-İrsaliye Gönderme (SendDespatchAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-gonderme-senddespatchadvice)
    - * E-İrsaliye Platformu üzerinden 1 ya da daha fazla e-irsaliyeyi GIB (Gelir İdaresi Başkanlığı) E-İrsaliye sistemine gönderir. * E-İrsaliye gönderim esnasında hatalı duruma geçen irsaliyeler bu servis ile tekrar gönderilebilir. * Bir alıcıya birden fazla irsaliye gönderilebilir.
    - Params: REQUEST_HEADER*, SENDER, RECEIVER*, DESPATCHADVICE
  - [Taslak İrsaliye Yükleme (LoadDespatchAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/taslak-i-rsaliye-yukleme-loaddespatchadvice)
    - * Özel entegratör platformu üzerinden 1 yada daha fazla irsaliyeyi sisteme yükler. * Eğer irsaliye numarası atanmışsa (16 hane ise) şema ve şematron kontrolünden geçirilir. İrsaliye numarası atanmamışsa şema ve şematron kontrolü yapılmaz. * Aynı İrsaliye tekrar taslaklara yüklen
    - Params: REQUEST_HEADER*, DESPATCHADVICE*
  - [E-İrsaliye Yanıtı Gönderme (SendReceiptAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-yaniti-gonderme-sendreceiptadvice)
    - E-İrsaliye Yanıtı belgesinin özel entegratör sistemlerine gönderilmesini sağlayan servistir.
    - Params: REQUEST_HEADER*, SENDER, RECEIVER, ID_ASSIGN_FLAG, ID_ASSIGN_PREFIX, XSLT_NAME, RECEIPTADVICE
  - [E-İrsaliye Okuma (GetDespatchAdvice) @](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-okuma-getdespatchadvice)
    - * E-İrsaliye sisteminden giden imzalı irsaliye veya gelen irsaliyeyi ERP/muhasebe paketine çekmek için kullanılır. * İrsaliye özet bilgilerini veya irsaliye özet bilgileri ile beraber XML içeriğini de çekmek için kullanılabilir. * Entegrasyon yapan iş ortaklarımızdan yeni gelen b
    - Params: REQUEST_HEADER*, SEARCH_KEY, HEADER_ONLY
  - [Taslak E-İrsaliye Yanıtı Yükleme (LoadReceiptAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/taslak-e-i-rsaliye-yaniti-yukleme-loadreceiptadvice)
    - Taslak E-İrsaliye Yanıtı belgelerini yüklemek için kullanılan servistir.
    - Params: REQUEST_HEADER*, RECEIPTADVICE*
  - [E-İrsaliye Durum Sorgulama (GetDespatchAdviceStatus)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-durum-sorgulama-getdespatchadvicestatus)
    - * Entegrasyon platformunda bulunan bir veya birden fazla taslak, gelen ve giden irsaliyenin durumunu sorgulamayı sağlayan servistir. * Birden fazla belge durumu sorgulamak için DESPATCHADVICEINFO parametresi çoklanabilir.
    - Params: REQUEST_HEADER*, UUID*
  - [E-İrsaliye Yanıtı Okuma (GetReceiptAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-yaniti-okuma-getreceiptadvice)
    - Sistemde bulunan e-İrsaliye yanıtlarını okumak için kullanılan servistir.
    - Params: REQUEST_HEADER*, SEARCH_KEY, HEADER_ONLY
  - [E-İrsaliye Yanıtı Durumu Okuma (GetReceiptAdviceStatus)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-yaniti-durumu-okuma-getreceiptadvicestatus)
    - Sistemde bulunan e-İrsaliye yanıtlarının durumlarını okumak için kullanılan servistir.
    - Params: REQUEST_HEADER*, UUID*
  - [E-İrsaliye Yanıtını Okundu İşaretleme (MarkReceiptAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliye-yanitini-okundu-i-saretleme-markreceiptadvice)
    - E-İrsaliye Yanıtı belgelerini okundu/okunmadı olarak işaretlemek için kullanılan servistir.
    - Params: REQUEST_HEADER*, MARK
  - [E-İrsaliyeyi Okundu İşaretleme (MarkDespatchAdvice)](https://dev.izibiz.com.tr/soap/soap-ws3/e-irsaliye/e-i-rsaliyeyi-okundu-i-saretleme-markdespatchadvice)
    - E-İrsaliye belgelerini okundu/okunmadı olarak işaretlemek için kullanılan servistir.
    - Params: REQUEST_HEADER*, MARK
