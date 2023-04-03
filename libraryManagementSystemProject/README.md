+--------------------------------------+
|                Kütüphane              |
+--------------------------------------+
| - kitaplar: List[Kitap]               |
| - kullanıcılar: List[Kullanıcı]       |
| - ödunc_kitaplar: List[OduncKitap]    |
+--------------------------------------+
| + kitap_ekle(kitap: Kitap)            |
| + kitap_kaldir(kitap_id: int)         |
| + kitap_ara(kitap_adi: str) -> List   |
| + kullanici_ekle(kullanici: Kullanıcı)|
| + kullanici_sil(kullanici_id: int)    |
| + kullanici_ara(kullanici_adi: str) -> List|
| + odunc_ver(kullanici_id: int, kitap_id: int, odunc_tarihi: datetime.date) -> bool|
| + odunc_alinan_kitaplar(kullanici_id: int) -> List|
| + odunc_iade_et(kullanici_id: int, kitap_id: int, iade_tarihi: datetime.date) -> bool|
| + geciken_odunc_kitaplar() -> List[OduncKitap]|
+--------------------------------------+

+--------------------------------------+
|                 Kitap                |
+--------------------------------------+
| - kitap_adi: str                      |
| - yazar: str                          |
| - yayinevi: str                       |
| - basim_tarihi: datetime.date         |
| - kitap_id: int                       |
| - odunc: bool                         |
+--------------------------------------+
| + __str__() -> str                    |
+--------------------------------------+

+--------------------------------------+
|               Kullanıcı              |
+--------------------------------------+
| - ad_soyad: str                       |
| - kullanici_id: int                   |
| - odunc_kitaplar: List[OduncKitap]    |
+--------------------------------------+
| + __str__() -> str                    |
+--------------------------------------+

+--------------------------------------+
|               OduncKitap              |
+--------------------------------------+
| - kitap: Kitap                        |
| - kullanici: Kullanıcı                |
| - odunc_tarihi: datetime.date         |
| - iade_tarihi: datetime.date          |
+--------------------------------------+
| + gecikme_suresi() -> int             |
| + __str__() -> str                    |
+--------------------------------------+
