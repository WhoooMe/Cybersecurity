# The Web Trail

| Komponen | Isi |
|---|---|
| Kategori | OSINT |
| Kesulitan | Medium |
| Poin | 200 |
| Estimasi waktu | 20-40 menit |
| Attachment | Tidak ada |
| Format flag | `TecFest26{kata_kode_namajalan}` |

## Deskripsi (untuk peserta)

> Seorang kolektor jejak digital menyimpan catatan perjalanannya di internet. Ia tidak pernah menyebut namanya sendiri. Satu-satunya petunjuk yang ia tinggalkan adalah sebuah akun Instagram milik aktor yang dikenal lewat peran ikoniknya: **`@tomholland2013`**.
>
> Mulailah dari akun itu. Pelajari siapa dia dan peran apa yang membuatnya terkenal. Dari sana, cari tahu di mana sang kolektor menyimpan catatannya. Gali apa yang pernah ia tulis lalu hapus, dan cari tahu di jalan mana ia berdiri saat memotret tujuan akhirnya.
>
> Susun tiga potongan yang kamu temukan menjadi satu flag.
>
> **Format flag:** `TecFest26{kata_kode_namajalan}`
> - **`kata`**: kata kode (*codename*) yang ditemukan di catatan.
> - **`kode`**: kode tiket angka yang ditemukan di catatan.
> - **`namajalan`**: nama jalan tempat fotografer berdiri saat mengambil foto (huruf kecil semua, tanpa spasi, tanpa tanda aksen/diakritik, gunakan underscore `_`).
> - Contoh format penulisan nama jalan: `rue_de_rivoli` (bukan `Rue de Rivoli`) atau `quai_branly` (bukan `Quai Branly`).
>
> *Catatan: Akun Instagram tersebut hanya titik awal. Kamu tidak perlu follow, DM, atau berinteraksi dengannya dalam bentuk apa pun. Semua informasi yang dibutuhkan bersifat publik. Akun GitHub yang terlibat adalah akun fiktif buatan panitia dan tidak berafiliasi dengan tokoh mana pun.*

## Hint (opsional)

| Hint | Isi | Pengurangan poin |
|---|---|---|
| 1 | "Cari handle Instagram tadi di GitHub. Ada akun yang namanya mirip." | -10 |
| 2 | "Nama repo merujuk julukan karakter ikoniknya, bukan judul filmnya." | -15 |
| 3 | "Sesuatu yang dihapus belum tentu hilang. Periksa riwayat commit." | -20 |
| 4 | "Yang ditanyakan adalah jalan tempat fotografer berdiri, bukan nama monumennya." | -30 |

## Flag Final (Catatan Panitia)

Berdasarkan setup repositori yang sudah kamu jalankan (`CODENAME="webslinger"` dan `TICKET="0417"`), struktur flag finalnya adalah:

```text
TecFest26{webslinger_0417_<namajalan>}
```

**Contoh jika titik foto berada di Quai Branly:**
```text
TecFest26{webslinger_0417_quai_branly}
```

> **Penting:** Ganti `<namajalan>` dengan nama jalan resmi di Google Maps tempat sudut foto `venue_final.jpg` milikmu diambil (gunakan huruf kecil semua, ganti spasi dengan `_`, dan hilangkan tanda aksen Prancis seperti `é` menjadi `e`).