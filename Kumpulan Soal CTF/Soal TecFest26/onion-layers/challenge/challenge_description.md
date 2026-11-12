# Onion Layers

| | |
|---|---|
| **Event** | TecFest26 |
| **Kategori** | Crypto |
| **Tingkat kesulitan** | Easy – Medium |
| **Poin** | 100 |
| **File** | `chall.txt` |
| **Format flag** | `TecFest26{...}` |

## Deskripsi

> Seorang admin paranoid menyembunyikan flag-nya dengan membungkusnya
> berlapis-lapis, seperti bawang. Ia yakin tidak akan ada yang sabar
> mengupasnya satu per satu.
>
> Buktikan dia salah.

## Attachment

`chall.txt`

```
GNSDGZBVGE2TINRTGY3TMYZUG43GINTGGZRTINZXGY3TQNZYGU3TKNZWMY2TCNBTGVQTINJWG42DGNRSGMYTONZUMY2GGNRXGY4TKNRWGU2TEN3BGU3TMZJTGA3GGNBUGQ2TIOJUGE2DKNJZGY2DMZBUG42DKNJVGQ3DIYRUHE3TGNJRGQYQ====
```

## Hint

| # | Biaya | Isi hint |
|---|---|---|
| 1 | 10 poin | Tidak semua layer berupa encoding. Ada satu layer yang hanya membalik urutan. |
| 2 | 20 poin | Semua flag di event ini diawali `TecFest26{`. Apa yang terjadi jika kamu XOR ciphertext dengan teks yang sudah kamu ketahui? Perhatikan juga bahwa key-nya berulang. |

## Flag

```
TecFest26{l4y3r5_0f_enc0d1ng_x0r_m4st3r}
```

> Catatan panitia: bagian **Flag** dan **Hint** tidak ditampilkan ke peserta.
