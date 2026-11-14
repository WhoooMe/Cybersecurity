# Writeup: The Web Trail

**Kategori:** OSINT | **Kesulitan:** Medium | **Format Flag:** `TecFest26{kata_kode_namajalan}`

## Alur Singkat

```text
IG @tomholland2013 ─► Spider-Man / "Friendly Neighborhood" ─► GitHub (tomholland2013-fan) ─► Commit history ─► Foto + kode ─► Street View ─► Flag
   (titik awal)             (pivot lewat peran ikonik)                  (tahap 2)             (file terhapus)     (venue)       (nama jalan)
```

## Tahap 1: Instagram (titik awal dan pivot)

1. Peserta membuka `https://instagram.com/tomholland2013`.
2. Dari profil, peserta mencatat **handle** (`tomholland2013`) dan **nama tampilan** (Tom Holland).
3. Peran paling ikonik aktor ini adalah **Spider-Man / Peter Parker**. Deskripsi menyebut "peran ikonik" dan "julukan karakter", sehingga peserta mengarah ke tema Spider-Man.
4. Akun IG **tidak menyimpan fragmen flag**. Fungsinya hanya menjadi jembatan (*pivot*) ke GitHub.

**Pivot ke GitHub:**
- Cari `tomholland2013` di GitHub (**Search → Users**), lalu ditemukan akun fiktif **`tomholland2013-fan`** (dengan bio disclaimer panitia).
- Akun ini memiliki dua repositori publik bertema Spider-Man:

| Repo | Peran |
|---|---|
| `homecoming-notes` | **Decoy.** Judul film. Isi dan 2 commit biasa, tanpa petunjuk tersembunyi. |
| `friendly-neighborhood-notes` | **Repo benar.** Julukan karakter (*"Friendly Neighborhood Spider-Man"*). |

- Peserta memilih repo yang cocok dengan petunjuk *"julukan karakter, bukan judul film"* (Hint 2).

## Tahap 2: GitHub, riwayat commit

Tampilan utama (*HEAD*) repo `friendly-neighborhood-notes` terlihat normal: hanya berisi `README.md` dan `schedule.md`. Kuncinya ada di tab **Commits** (6 commit):

| # | Commit message | Perubahan |
|---|---|---|
| 1 | `init notes` | `README.md` |
| 2 | `add codename note` | `codename.txt` berisi `webslinger` |
| 3 | `add visitor ticket` | `ticket.txt` berisi `ticket: 0417` |
| 4 | `add reference photo` | `venue_final.jpg` |
| 5 | `cleanup (oops)` | menghapus `codename.txt`, `ticket.txt`, `venue_final.jpg` |
| 6 | `update schedule` | `schedule.md` |

Langkah peserta:
1. Buka tab **Commits** pada `friendly-neighborhood-notes`.
2. Periksa diff pada commit 2 dan 3 untuk membaca isi file sebelum dihapus.
3. Buka commit 4 (`add reference photo`) dan unduh file **`venue_final.jpg`**.

**Fragmen didapat:**
- **`kata` (codename):** `webslinger`
- **`kode` (ticket):** `0417`
- **Aset visual:** `venue_final.jpg` (metadata EXIF sudah dibersihkan).

## Tahap 3: Geolocation

1. Peserta memeriksa foto `venue_final.jpg`: terlihat **Menara Eiffel (Paris, Prancis)** dari sudut pandang tertentu. Yang ditanyakan bukan nama monumennya, melainkan **nama jalan tempat fotografer berdiri**.
2. Buka **Google Maps / Street View** di sekitar Menara Eiffel, lalu cocokkan garis pandang ke arah menara, pepohonan, tepi jalan, dan bangunan di sekitarnya.
3. Konfirmasi nama jalan tempat titik berdiri fotografer di Google Maps, lalu ubah ke format flag (huruf kecil semua, tanpa tanda aksen, spasi diganti `_`).

## Flag Final

Menggabungkan ketiga bagian sesuai format `TecFest26{kata_kode_namajalan}`:

```text
TecFest26{webslinger_0417_<namajalan>}
```

*(Contoh jika lokasi foto berada di Quai Branly: `TecFest26{webslinger_0417_quai_branly}` — sesuaikan `<namajalan>` dengan lokasi asli `venue_final.jpg` milikmu).*

---

## Catatan Panitia (jangan dibagikan ke peserta)

**Setup GitHub (Sudah Dijalankan)**
- Akun aktif: **`tomholland2013-fan`** (email noreply: `356720087+tomholland2013-fan@users.noreply.github.com`).
- Bio profil **wajib** berbunyi: *"Fan-made CTF challenge. Not affiliated with Tom Holland."* Jangan gunakan foto profil asli, nama asli, atau interaksi ke akun tokoh asli.
- Pastikan akun `tomholland2013-fan` muncul di pencarian GitHub Users untuk kata kunci `tomholland2013` lewat jendela Incognito (tanpa login).
- Remote URL yang digunakan:
  - Repo benar: `https://github.com/tomholland2013-fan/friendly-neighborhood-notes.git`
  - Repo decoy: `https://github.com/tomholland2013-fan/homecoming-notes.git`
- Jangan lakukan `force-push`, `rebase`, atau `squash` setelah dipublikasikan agar hash commit tetap utuh.

**Akun Instagram Tokoh**
- Handle resmi yang dirujuk adalah `@tomholland2013`.
- Soal hanya bergantung pada **handle** dan **nama tampilan**, bukan bio atau postingan terbaru. Ambil screenshot profil pada hari lomba sebagai cadangan panitia.
- Pastikan tidak ada instruksi yang meminta peserta berinteraksi (follow, komentar, DM) dengan akun tokoh.

**Foto Venue (`venue_final.jpg`)**
- Pastikan file yang masuk ke commit 4 adalah `venue_final.jpg` yang sudah dikonversi dari PNG dan dibersihkan EXIF-nya (`exiftool -all= venue_final.jpg`).
- Tes gambar `venue_final.jpg` di Google Lens untuk memastikan tidak langsung terpecahkan secara instan lewat reverse image search.
- Pastikan titik jalan yang dipilih tidak berada di persimpangan ambigu sehingga hanya ada satu nama jalan yang valid untuk kunci jawaban.