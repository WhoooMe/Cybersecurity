# Writeup: Onion Layers (Crypto, TecFest26)

**Flag:** `TecFest26{l4y3r5_0f_enc0d1ng_x0r_m4st3r}`

## 1. Ringkasan

Flag dibungkus dengan satu layer enkripsi (XOR) dan empat layer encoding/transformasi. Soal ini menguji dua kemampuan:

1. **Mengenali encoding dari karakteristik charset-nya**, lalu membukanya satu per satu.
2. **Memanfaatkan sifat XOR** lewat *known-plaintext attack*, karena awalan flag sudah diketahui.

Urutan pembungkusan oleh pembuat soal:

```
Flag → XOR (repeating key) → Base64 → Reverse → Hex → Base32 → chall.txt
```

Peserta harus membukanya dengan urutan terbalik:

```
chall.txt → Base32 → Hex → Reverse → Base64 → XOR → Flag
```

## 2. Langkah penyelesaian

### Langkah 1: Identifikasi layer terluar (Base32)

Isi `chall.txt` hanya terdiri dari huruf kapital `A-Z`, angka `2-7`, dan padding `=` di akhir:

```
GNSDGZBVGE2TINRTGY3TMYZUG43GINTG...GQYQ====
```

Itu ciri khas **Base32** (tidak ada angka 0, 1, 8, 9 dan tidak ada huruf kecil). Setelah di-decode didapat:

```
3d3d515463676c476d6f6c4776787857576f51435a4567436231774f4c67695665527a576e306c444549414559646d474555464b49735141
```

### Langkah 2: Layer berikutnya (Hex)

Hasilnya hanya berisi `0-9` dan `a-f` dengan panjang genap. Itu **hexadecimal**. Setelah di-decode didapat:

```
==QTcglGmolGvxxWWoQCZEgCb1wOLgiVeRzWn0lDEIAEYdmGEUFKIsQA
```

### Langkah 3: Layer yang tidak berlabel (Reverse)

String ini terlihat seperti Base64, tetapi aneh karena padding `==` berada di **awal**, padahal di Base64 padding selalu di akhir. Itu petunjuk bahwa string-nya **terbalik**. Setelah dibalik:

```
AQsIKFUEGmdYEAIEDl0nWzReVigLOw1bCgEZCQoWWxxvGlomGlgcTQ==
```

### Langkah 4: Base64

Sekarang formatnya valid Base64 (ada huruf besar, huruf kecil, angka, dan padding `==` di akhir). Setelah di-decode didapat byte yang tidak terbaca (non-printable). Ini adalah data hasil XOR:

```
01 0b 08 28 55 04 1a 67 58 10 02 04 0e 5d 27 5b ...
```

Karena bukan teks yang bermakna, kita tahu masih ada layer enkripsi, bukan sekadar encoding.

### Langkah 5: Known-plaintext attack pada XOR

Sifat penting XOR:

```
P ⊕ K = C   →   C ⊕ P = K
```

Peserta tahu semua flag di event ini diawali `TecFest26{` (10 karakter). Dengan meng-XOR 10 byte pertama ciphertext dengan awalan tersebut, didapat potongan *key stream*:

| Posisi | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Ciphertext (hex) | 01 | 0b | 08 | 28 | 55 | 04 | 1a | 67 | 58 | 10 |
| Plaintext (`TecFest26{`) | 54 | 65 | 63 | 46 | 65 | 73 | 74 | 32 | 36 | 7b |
| Hasil XOR | 55 | 6e | 6b | 6e | 30 | 77 | 6e | 55 | 6e | 6b |
| Karakter | `U` | `n` | `k` | `n` | `0` | `w` | `n` | `U` | `n` | `k` |

Key stream-nya `Unkn0wnUnk`. Terlihat pola berulang: setelah 7 karakter (`Unkn0wn`), urutan kembali ke `Unk`. Jadi:

```
Key = Unkn0wn   (panjang 7, berulang)
```

### Langkah 6: Dekripsi XOR penuh

XOR seluruh ciphertext dengan key `Unkn0wn` yang diulang:

```
TecFest26{l4y3r5_0f_enc0d1ng_x0r_m4st3r}
```

## 3. Script solver

```python
import base64, binascii, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "dist", "chall.txt")

c = open(PATH).read().strip()
c = base64.b32decode(c)             # Base32
c = binascii.unhexlify(c)           # Hex
c = base64.b64decode(c[::-1])       # Reverse + Base64

crib = b"TecFest26{"
ks = bytes(c[i] ^ crib[i] for i in range(len(crib)))   # known-plaintext attack
print("Key stream:", ks)

# cari panjang key dari pola pengulangan
for L in range(1, len(ks)):
    if all(ks[i] == ks[i - L] for i in range(L, len(ks))):
        key = ks[:L]
        break

print("Key  :", key, f"(panjang {len(key)})")
print("Flag :", bytes(b ^ key[i % len(key)] for i, b in enumerate(c)).decode())
```

Output:

```
Key stream: b'Unkn0wnUnk'
Key  : b'Unkn0wn' (panjang 7)
Flag : TecFest26{l4y3r5_0f_enc0d1ng_x0r_m4st3r}
```

## 4. Alternatif: CyberChef

Recipe berurutan:

1. `From Base32`
2. `From Hex`
3. `Reverse` (By Character)
4. `From Base64`
5. `XOR` dengan key `Unkn0wn` (format UTF8)

Kunci XOR di langkah 5 didapat dari known-plaintext attack di atas (misalnya dengan menjalankan `XOR` dulu pada potongan awal, atau menghitung manual).
