# Writeup: The Web Trail

**Kategori:** OSINT | **Kesulitan:** Medium | **Flag:** `TecFest26{webslinger_0417_quai_branly}` *(contoh, sesuaikan)*

## Alur Singkat

```
IG @tomholland2013 ─► Spider-Man / "Friendly Neighborhood" ─► GitHub repo ─► Commit history ─► Foto + kode ─► Street View ─► Flag
   (titik awal)             (pivot lewat peran ikonik)         (tahap 2)      (file terhapus)     (venue)       (nama jalan)
```

## Tahap 1: Instagram (titik awal dan pivot)

1. Peserta membuka `https://instagram.com/tomholland2013`.
2. Dari profil, peserta mencatat **handle** (`tomholland2013`) dan **nama tampilan** (Tom Holland).
3. Peran paling ikonik aktor ini adalah **Spider-Man / Peter Parker**. Deskripsi menyebut "peran ikonik" dan "julukan karakter", jadi peserta mengarah ke tema Spider-Man.
4. Akun IG **tidak menyimpan fragmen flag**. Fungsinya hanya menjadi jembatan ke GitHub.

**Pivot ke GitHub:**
- Cari `tomholland2013` di GitHub (Search → Users), lalu ketemu akun fiktif `tomholland2013-archive`.
- Akun ini punya dua repo bertema Spider-Man:

| Repo | Peran |
|---|---|
| `homecoming-notes` | **Decoy.** Judul film. Isi dan commit biasa, tanpa file tersembunyi. |
| `friendly-neighborhood-notes` | **Repo benar.** Julukan karakter ("Friendly Neighborhood Spider-Man"). |

- Peserta memilih repo yang cocok dengan petunjuk "julukan karakter, bukan judul film" (Hint 2). Di sinilah tahap kedua dimulai.

## Tahap 2: GitHub, riwayat commit

Repo `friendly-neighborhood-notes` terlihat biasa: hanya `README.md` dan `schedule.md`. Kuncinya ada di **commit history**.

| # | Commit message | Perubahan |
|---|---|---|
| 1 | `init notes` | `README.md` |
| 2 | `add codename note` | `codename.txt` berisi `webslinger` |
| 3 | `add visitor ticket` | `ticket.txt` berisi `0417` |
| 4 | `add reference photo` | `venue_final.jpg` |
| 5 | `cleanup (oops)` | menghapus `codename.txt`, `ticket.txt`, `venue_final.jpg` |
| 6 | `update schedule` | `schedule.md` |

Langkah peserta:
1. Buka tab **Commits**.
2. Buka commit 2, 3, dan 4 untuk membaca isi file sebelum dihapus.
3. Unduh `venue_final.jpg` dari commit 4.

**Fragmen didapat:** `webslinger` dan `0417`, plus foto venue.

## Tahap 3: Geolocation

1. Peserta melihat foto: Menara Eiffel dari sudut tertentu (Paris, Prancis). Lokasi umumnya mudah ditebak, tetapi **yang ditanya adalah nama jalan tempat fotografer berdiri**.
2. Buka Google Maps / Street View di sekitar menara, lalu cocokkan:
   - sudut pandang dan jarak ke menara,
   - bangunan, pohon, tiang, atau rambu di sisi foto,
   - tepi sungai atau jembatan bila terlihat.
3. Titik berdiri dikonfirmasi di **Quai Branly** → `quai_branly`.

> Ganti jalan ini dengan titik foto aslimu. Pastikan titik itu berada jelas di satu jalan, bukan persimpangan.

## Flag

```
TecFest26{webslinger_0417_quai_branly}
```

---

## Catatan Panitia (jangan dibagikan ke peserta)

**Setup GitHub**
- Akun: `tomholland2013-archive`. Bio **wajib** berbunyi: *"Fan-made CTF challenge. Not affiliated with Tom Holland."* Jangan pakai foto profil asli, nama asli, atau klaim bahwa akun ini milik tokoh.
- Pastikan akun muncul di pencarian GitHub Users untuk kata `tomholland2013` (tes dari browser tanpa login).

```bash
# Repo benar
git init friendly-neighborhood-notes && cd friendly-neighborhood-notes
echo "# Friendly Neighborhood Notes" > README.md
git add . && git commit -m "init notes"
echo "webslinger" > codename.txt
git add . && git commit -m "add codename note"
echo "ticket: 0417" > ticket.txt
git add . && git commit -m "add visitor ticket"
cp ../venue_final.jpg . && git add . && git commit -m "add reference photo"
git rm codename.txt ticket.txt venue_final.jpg
git commit -m "cleanup (oops)"
echo "schedule" > schedule.md
git add . && git commit -m "update schedule"
git remote add origin <url> && git push -u origin main

# Repo decoy
git init ../homecoming-notes && cd ../homecoming-notes
echo "# Homecoming Notes" > README.md
git add . && git commit -m "init"
echo "todo: nothing here" > todo.md
git add . && git commit -m "add todo"
git remote add origin <url> && git push -u origin main
```
Jangan force-push atau squash.

**Akun Instagram tokoh**
- Aku memverifikasi lewat pencarian bahwa handle resminya adalah `@tomholland2013`. Handle `tomholland` tanpa angka kemungkinan akun lain, jadi jangan dipakai.
- Soal hanya bergantung pada **handle** dan **nama tampilan**, bukan bio atau postingan, karena keduanya bisa berubah. Ambil screenshot profil pada hari lomba sebagai backup.
- Instagram sering meminta login bagi pengunjung anonim. Siapkan screenshot atau halaman statis cadangan, dan tulis di deskripsi bahwa akunnya publik.
- Pastikan tidak ada instruksi yang menyuruh peserta berinteraksi dengan akun tokoh (follow, komentar, DM).

**Foto venue**
- Menara Eiffel sangat umum, jadi reverse image search akan mudah menemukan foto stok. Gunakan foto orisinal dengan sudut tidak biasa, atau foto lisensi bebas yang kamu crop dan ubah sudutnya.
- Pastikan ada satu petunjuk visual yang membuat nama jalan bisa ditentukan (rambu, bentuk bangunan, tepian sungai).
- Hapus EXIF: `exiftool -all= venue_final.jpg`, lalu cek ulang dengan `exiftool venue_final.jpg`.
- Tanpa wajah orang atau plat nomor yang terbaca.

**Uji alur**
- Minta 1-2 teman mencoba hanya dengan deskripsi. Catat di mana mereka macet, terutama di pemilihan antara repo decoy dan repo benar.
- Tes foto di Google Lens untuk memastikan tidak langsung ketemu.
- Tentukan format jalan yang diterima (`quai_branly`, tanpa aksen).
