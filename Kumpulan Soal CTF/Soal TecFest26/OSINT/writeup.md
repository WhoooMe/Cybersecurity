# Writeup: The Iron Trail

**Kategori:** OSINT | **Kesulitan:** Medium | **Flag:** `TecFest26{damedefer_0417_quai_branly}` *(contoh, sesuaikan)*

## Alur Singkat

```
Instagram tokoh ──► GitHub (username hasil pivot) ──► Commit history ──► Foto + kode ──► Street View ──► Flag
 (titik awal)         (cari handle/nama)               (file terhapus)     (venue)        (nama jalan)
```

## Tahap 1: Instagram (titik awal / pivot)

1. Peserta membuka `https://instagram.com/[HANDLE_IG_TOKOH]`.
2. Dari profil, peserta mencatat **handle** dan **nama tampilan** (`[NAMA_TOKOH]`).
3. Keduanya dipakai sebagai kata kunci pencarian di GitHub. Akun IG ini **tidak menyimpan fragmen flag**, hanya menjadi jembatan.

**Pivot:** cari `[HANDLE_IG_TOKOH]` di GitHub (Search → Users) dan ketemu akun `[HANDLE_IG_TOKOH]-archive`. Bio akun itu menyebut repo `eiffel-notes`.

## Tahap 2: GitHub, riwayat commit

Repo `eiffel-notes` terlihat biasa: hanya `README.md` dan `schedule.md`. Kuncinya ada di **commit history**.

| # | Commit message | Perubahan |
|---|---|---|
| 1 | `init notes` | `README.md` |
| 2 | `add codename note` | `codename.txt` berisi `damedefer` |
| 3 | `add visitor ticket` | `ticket.txt` berisi `0417` |
| 4 | `add reference photo` | `venue_final.jpg` |
| 5 | `cleanup (oops)` | menghapus `codename.txt`, `ticket.txt`, `venue_final.jpg` |
| 6 | `update schedule` | `schedule.md` |

Langkah peserta:
1. Buka tab **Commits**.
2. Buka commit 2, 3, dan 4 untuk membaca isi file sebelum dihapus.
3. Unduh `venue_final.jpg` dari commit 4.

**Fragmen didapat:** `damedefer` dan `0417`, plus foto venue.

## Tahap 3: Geolocation

1. Peserta melihat foto: Menara Eiffel dari sudut tertentu. Menaranya mudah dikenali (Paris, Prancis), tetapi **yang ditanya adalah nama jalan tempat fotografer berdiri**.
2. Buka Google Maps / Street View di sekitar menara, cocokkan:
   - sudut pandang dan jarak ke menara,
   - bangunan, pohon, tiang, atau rambu di sisi foto,
   - tepi sungai atau jembatan bila terlihat.
3. Titik berdiri dikonfirmasi di **Quai Branly** → `quai_branly`.

> Ganti jalan ini dengan titik foto aslimu. Pastikan titik itu berada jelas di satu jalan, bukan persimpangan.

## Flag

```
TecFest26{damedefer_0417_quai_branly}
```

---

## Catatan Panitia (jangan dibagikan ke peserta)

**Setup repo GitHub**
```bash
git init eiffel-notes && cd eiffel-notes
echo "# Eiffel Notes" > README.md
git add . && git commit -m "init notes"
echo "damedefer" > codename.txt
git add . && git commit -m "add codename note"
echo "ticket: 0417" > ticket.txt
git add . && git commit -m "add visitor ticket"
cp ../venue_final.jpg . && git add . && git commit -m "add reference photo"
git rm codename.txt ticket.txt venue_final.jpg
git commit -m "cleanup (oops)"
echo "schedule" > schedule.md
git add . && git commit -m "update schedule"
git remote add origin <url> && git push -u origin main
```
Jangan force-push atau squash.

**Foto venue**
- Menara Eiffel sangat umum, jadi **reverse image search akan mudah menemukan foto stok**. Gunakan foto orisinal dengan sudut tidak biasa, misalnya dari bantuan teman yang ada di Paris atau foto lisensi bebas yang kamu crop dan ubah sudutnya.
- Pastikan ada satu petunjuk visual yang membuat nama jalan bisa ditentukan (rambu, bentuk bangunan, tepian sungai).
- Hapus EXIF: `exiftool -all= venue_final.jpg`, lalu cek ulang dengan `exiftool venue_final.jpg`.
- Tanpa wajah orang atau plat nomor yang terbaca.

**Akun tokoh di Instagram**
- Bio dan nama tampilan tokoh bisa berubah kapan saja, jadi alur ini hanya bergantung pada **handle** (stabil) sebagai kata kunci pencarian. Simpan screenshot profil pada hari lomba sebagai backup.
- Instagram sering meminta login bagi pengunjung anonim. Cantumkan di deskripsi bahwa akunnya publik, dan siapkan screenshot atau halaman statis cadangan.
- Akun GitHub `[HANDLE_IG_TOKOH]-archive` **bukan milik tokoh itu**. Tulis jelas di bio GitHub: *"Fan-made CTF challenge, not affiliated with [NAMA_TOKOH]"*, supaya tidak terlihat seperti peniruan identitas. Jangan pakai foto profil asli tokoh.
- Pilih tokoh yang profilnya stabil dan tidak sedang kontroversial.

**Uji alur**
- Minta 1-2 teman mencoba hanya dengan deskripsi. Catat di mana mereka macet dan berapa lama.
- Tes juga foto di Google Lens untuk memastikan tidak langsung ketemu.
- Pastikan format jalan yang diterima jelas (`quai_branly`, tanpa aksen).
