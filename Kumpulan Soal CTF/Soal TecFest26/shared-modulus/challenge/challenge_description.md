# Twin Keys

| | |
|---|---|
| **Event** | TecFest26 |
| **Kategori** | Crypto |
| **Tingkat kesulitan** | Medium |
| **Poin** | 250 |
| **File** | `handout.zip` (`pub1.pem`, `pub2.pem`, `ct1.txt`, `ct2.txt`) |
| **Format flag** | `TecFest26{...}` |

## Deskripsi

> Panitia TecFest26 mengirim pesan rahasia yang sama ke dua cabang panitia.
> Agar "praktis", kedua cabang diberi public key yang berbeda, tetapi
> dibuat dari modulus yang sama. Toh, private key-nya tetap tersimpan aman, bukan?
>
> Dua ciphertext berhasil kamu sadap dari jaringan. Bisakah kamu membaca
> pesan yang mereka kirim?

## Attachment

`handout.zip`:

```
pub1.pem   ← public key cabang 1
pub2.pem   ← public key cabang 2
ct1.txt    ← ciphertext untuk cabang 1 (Base64)
ct2.txt    ← ciphertext untuk cabang 2 (Base64)
```

## Hint

| # | Biaya | Isi hint |
|---|---|---|
| 1 | 10 poin | Buka kedua public key dan bandingkan isinya. Apa yang sama? Apa yang berbeda? |
| 2 | 20 poin | Identitas Bézout: `a·e1 + b·e2 = gcd(e1, e2)`. Hitung `gcd`-nya, apakah benar bernilai 1? |
| 3 | 30 poin | Jika `gcd = g`, hasil serangan bukan `m` melainkan `m^g mod N`. Kapan `m^g mod N` sama dengan `m^g` biasa? |

## Flag

```
TecFest26{c0mm0n_m0dulus_sh4r3d_n_br34ks_rs4}
```

> Catatan panitia: bagian **Flag** dan **Hint** tidak ditampilkan ke peserta.
