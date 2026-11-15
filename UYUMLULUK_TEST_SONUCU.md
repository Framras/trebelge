# Uyumluluk testi sonucu

Tarih: 2026-11-15. Site: `fiadev.cursor`. Dal: `version-16`. XML üretici yok; round-trip okuma yoluyla doğrulandı.

## A. Streaming

**Geçti.** Ayrıntı: `STREAMING_TEST_SONUCU.md`.

Filtreli tepe bellek: tracemalloc 4,14 MB, RSS ~17,8 MB. Tam liste: tracemalloc 130,64 MB, RSS ~300 MB. Altı VKN için sonuçlar aynı.

## B. Okuma eksikleri (§3, 1–7)

Test: `trebelge.tests.test_reading_gaps.TestReadingGaps.test_invoice_read_stores_seven_gaps` — **OK** (0,90 s).

`InvoiceHandler` kayıt sonunda `frappe.db.commit()` çağırır. Test aynı kurucuyu (`TRUBLInvoiceBuilder` + `TRUBLDirector.make_tr_ubl_invoice`) kullanır ve commit çağırmaz. XML yazıcı olmadığı için üretilen XML farkı yok; okunan alanlar kaynak XML ile aynı.

| # | Eleman | Sonuç | Okunan değer |
|---|---|---|---|
| 1 | `LegalMonetaryTotal/PrepaidAmount` | Geçti | `prepaidamount=25.50`, `prepaidamountcurrencyid=TRY`. Aynı atama `TRUBLCreditNoteBuilder.build_legalmonetarytotal` içinde de var. |
| 2 | `Invoice/PrepaidPayment` | Geçti | Satır: `id=AVANS-1`, `paidamount=25.50 TRY`, `receiveddate=2026-01-15`. Diğer builder'lar `pass`. |
| 3 | `Item/StandardItemIdentification` | Geçti | `standarditemid` → `UBL TR ItemIdentification.id = 8690000000001` |
| 4 | `Price/BaseQuantity` | Geçti | `basequantity=1`, `basequantityunitcode=C62` |
| 5 | `Price/AllowanceCharge` | Geçti | `priceallowancecharge` ayrı çocuk. Gerekçe "Birim fiyat iskontosu" (2.00). Satır `AllowanceCharge` ayrı: "Satir iskontosu" (1.00). |
| 6 | `InvoiceLine/FreeOfChargeIndicator` | Geçti | Check `freeofchargeindicator=1` (`true`) |
| 7 | `PaymentMeans/PaymentID` | Geçti | `paymentid=REF-99` |

`CreditNoteLine` yazılmadı; `build_creditnoteline` `pass` kaldı.

Round-trip fark listesi: yok. trebelge XML üretmiyor (read path only).

## C. Kod listeleri

Test: `trebelge.tests.test_codelists.TestCodeLists.test_read_warns_and_production_throws` — **OK** (0,10 s).

Okuma: bilinmeyen kod `frappe.logger("trebelge").warning`, ayrıştırma durmaz. Bilinmeyen ödeme şekli veya birim kodu Link doğrulamasını da kesmez (`flags.ignore_links`). Üretim: `trebelge.codelists.validate_for_production(kind, code)` `frappe.throw` eder. XML üretici olmadığı için bu fonksiyon üretim yoluna bağlanacak yer; birim test throw ve warn'ı kanıtlar.

Kaynak kod listesi: `/home/tufankaynak/Documents/e-FaturaPaketi (29)/e-FaturaPaketi/schematron/UBL-TR_Codelist.xml`. Sitedeki `UBL TR Paymentmeanscode`, `UBL TR Unitcodes` ve `UBL TR TaxExemptionReasonCode` tabloları boştu; üzerine yazılacak kayıt yoktu.

| Liste | Sonuç | Ne yüklendi |
|---|---|---|
| ProfileID | Geçti | Yönergedeki 7 kod: TEMELFATURA, TICARIFATURA, EARSIVFATURA, IHRACAT, YATIRIMTESVIK, SGK, TEMELIRSALIYE |
| InvoiceTypeCode | Geçti | Yönergedeki 10 kod: SATIS, IADE, TEVKIFAT, ISTISNA, OZELMATRAH, IHRACKAYITLI, YTBSATIS, YTBISTISNA, YTBIADE, SGK |
| PaymentMeansCode | Geçti | Şematron `PaymentMeansCodeTypeList`: 75 kod (1…53, 60…67, 70, 74…78, 91…97, ZZZ). Açıklama metni dosyada yok, alan boş. |
| KDV istisna | Geçti, adlar TODO | 113 kod (`TaxExemptionReasonCodeType` birleşimi + 308/339). `list` / `invoicetypecode` şematron alt kümelerinden (ISTISNA, OZELMATRAH, IHRACKAYITLI, YATIRIMTESVIK). `taxexemptionreasoncodename` boş. |
| KDV tevkifat | Geçti, adlar TODO | `WithholdingTaxTypeWithPercent`: 53 kod, 64 satır. Oranlar kodun sonundaki yüzdeden: 2/10, 3/10, 4/10, 5/10, 7/10, 9/10, 10/10. 601 için 3/10 ve 4/10; 650 için 2/10, 3/10, 5/10, 7/10, 9/10. Açıklama boş. |
| Birim | Geçti | C62 Adet, KGM Kilogram, MTR Metre, LTR Litre (UNECE Rec.20). Tabloda eski kayıt yoktu, silinen birim yok. Tam UNECE listesinin adları pakette yok, yüklenmedi. |

### TODO

- KDV istisna kodlarının resmi adları (`taxexemptionreasoncodename`) yerel e-Fatura paketinde yok. Kodlar yüklü, adlar boş.
- Tevkifat kodlarının işlem adları yerel dosyada yok. Kod ve oran şematrondan; açıklama boş.
- Ödeme şekli kodlarının UN/EDIFACT açıklamaları pakette yok. Kodlar yüklü, `description` / `explanation` boş.
- Şematron ProfileID / InvoiceTypeCode listesi yönergedekinden geniş (ör. YOLCUBERABERFATURA, KAMU, HKS, ENERJI, TEVKIFATIADE, YTBTEVKIFAT). Yönergedeki tam liste yüklendi; fazlası eklenmedi.
- Şematronda SGK bir ProfileID değil, InvoiceTypeCode. Yönerge her iki listede de saydığı için SGK ProfileID kaydı da var.

## Commit'ler

- `4fa67d6` streaming (önceden)
- `16f6fb9` okuma eksikleri
- `6dd8529` kod listeleri ve doğrulama
- sonuç dosyaları (`STREAMING_TEST_SONUCU.md`, `UYUMLULUK_TEST_SONUCU.md`) ayrı commit
