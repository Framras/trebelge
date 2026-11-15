# Streaming testi — newUserPkList (sentetik)

Tarih: 2026-11-15. Dal: `version-16`. Gerçek GİB dosyası kullanılmadı.

## Dosya

`EbelgeUsers` sınıfının okuduğu yapıda sentetik XML üretildi: `User` / `Identifier` / `Documents` / `Document type=Invoice|DespatchAdvice` / `CreationTime` / `DeletionTime`.

| | |
|---|---|
| Kullanıcı sayısı | 500_000 |
| Dosya boyutu | 98_333_345 bayt (~93,8 MiB) |
| Akış | `api.get_ebelge_users` ile aynı, 1 MiB `parser.feed` |
| Karşılaştırılan VKN | `0000000000`, `0000000001`, `0000000002`, `0000001000`, `0000250000`, `0000499999` |

Üç desen var: yalnız e-Fatura, e-Fatura + e-İrsaliye, e-Fatura kaydı silinmiş + e-İrsaliye.

## Sonuç

Aynı altı vergi numarası için `wanted=None` (eski tam sözlük) ve `wanted={altı VKN}` çıktıları birebir aynı.

| VKN | is_efatura_user | is_eirsaliye_user |
|---|---|---|
| 0000000000 | true | false |
| 0000000001 | true | true |
| 0000000002 | false | true |
| 0000001000 | true | true |
| 0000250000 | true | true |
| 0000499999 | true | true |

Filtrelenmiş sözlükte başka anahtar yok (6 kayıt). Tam sözlükte 500_000 kayıt var.

## Bellek

Ölçüm ayrı süreçlerde, `tracemalloc` ve `resource.ru_maxrss` (Linux, KB).

| Mod | Süre | tracemalloc tepe | tracemalloc son | ru_maxrss |
|---|---|---|---|---|
| Filtreli (`wanted` = 6 VKN) | 5,64 s | 4,14 MB | 2,01 MB | 18_232 KB (~17,8 MB) |
| Tam liste (`wanted=None`) | 7,64 s | 130,64 MB | 128,73 MB | 307_392 KB (~300 MB) |

Yönergedeki bant (~310 MB tam liste, ~15 MB filtreli) ile uyumlu. `ru_maxrss` yorumlayıcıyı da içerir; Python tahsisinin tepesi filtreli tarafta 4 MB.

**Geçti.**
