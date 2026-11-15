# GİB e-Fatura Paketi (local)

Local path: `/home/tufankaynak/Documents/e-FaturaPaketi (29)/e-FaturaPaketi`

This is the **GİB official document package** (format / envelope / validation), not the İzibiz özel entegratör API.

| Layer | Role |
|-------|------|
| This package | UBL-TR samples, zarf (envelope) XSDs, schematron, GİB merkez WSDL |
| İzibiz (`dev.izibiz.com.tr`) | Auth, send/status/inbox via `EInvoiceWS` / REST — we integrate here in trebelge |
| trebelge `TRUBLBuilder` | Build UBL that must match this package’s samples + schematron |

## Layout

| Dir | Contents |
|-----|----------|
| `wsdl/` | GİB merkez SOAP: `sendDocument`, `getApplicationResponse` |
| `xml/` | Sample invoices, zarflar, uygulama/sistem yanıtları, kullanıcı açma-silme |
| `xsd/Envelope` | StandardBusinessDocumentHeader / Package zarf şemaları |
| `xsd/Userlist` | NewUserList |
| `xsd/HRXML` | UserAccount + OAGIS deps |
| `schematron/` | `UBL-TR_Main_Schematron.xml`, Common, Codelist (`type=efatura\|earchive`) |
| `form/` | Test/canlı entegrasyon tanım formları |
| `bis raporu/` | BIS rapor şablonu |

## GİB merkez endpoints (package WSDL — not İzibiz)

- Test: `https://merkeztest.efatura.gov.tr/EFaturaMerkez/services/EFatura`
- Canlı: `https://merkez.efatura.gov.tr/EFaturaMerkez/services/EFatura`
- Ops: `sendDocument` (fileName + binaryData + hash) · `getApplicationResponse` (instanceIdentifier)

For **özel entegratör** mode, do **not** call these GİB merkez URLs from trebelge; call İzibiz. Still generate UBL/zarf content consistent with `xml/` + `schematron/`.

## Sample XML index (`xml/0_ACIKLAMALAR.txt`)

- `1_*` Temel fatura + zarf + sistem yanıtları (merkez / PK / GTB)
- `2_*` Ticari fatura + kabul uygulama yanıtı
- `3_*` Ticari fatura + red uygulama yanıtı
- `4_*` / `5_*` Kullanıcı açma / silme
- `6_*` KDV sıfır + istisna temel fatura
- `7_*` İade (temel/ticari) + iade uygulama yanıtı
- `8_*` / `9_*` Fatura saklama kullanıcı açma/silme

## Schematron note

Param `type`: empty/`efatura` = e-Fatura rules; `earchive` = ProfileID must be `EARSIVFATURA`.
