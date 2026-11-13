# Twin Keys

| | |
|---|---|
| **Kategori** | Crypto |
| **Tingkat kesulitan** | Medium |
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

| No. | Isi hint |
|---|---|
| 1 | Buka kedua public key dan bandingkan isinya. Apa yang sama? Apa yang berbeda? |
| 2 | Identitas Bézout: `a·e1 + b·e2 = gcd(e1, e2)`. Hitung `gcd`-nya, apakah benar bernilai 1? |
| 3 | Jika `gcd = g`, hasil serangan bukan `m` melainkan `m^g mod N`. Kapan `m^g mod N` sama dengan `m^g` biasa? |
| 4 | Kalau kamu sudah menemukan idenya tapi bingung merangkainya, pakai script bantu ini dan simpan di folder yang sama dengan `pub1.pem`, `pub2.pem`, `ct1.txt`, dan `ct2.txt`, lalu jalankan dengan `python helper.py`. Note: Kamu butuh Python 3.8+ dan `pip install pycryptodome` |

## Script helper.py
```python
import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long

# 1. Baca kunci dan ciphertext (jalankan di folder yang sama dengan file soal)
k1 = RSA.import_key(open("pub1.pem", "rb").read())
k2 = RSA.import_key(open("pub2.pem", "rb").read())
N, e1, e2 = k1.n, k1.e, k2.e
print("Modulus sama :", k1.n == k2.n)
print("e1, e2       :", e1, e2)

c1 = bytes_to_long(base64.b64decode(open("ct1.txt").read()))
c2 = bytes_to_long(base64.b64decode(open("ct2.txt").read()))

# 2. Euclid diperluas: a*e1 + b*e2 = g
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

g, a, b = xgcd(e1, e2)
print("g, a, b      :", g, a, b)

# 3. Gabungkan kedua ciphertext (eksponen negatif = invers modular, perlu Python 3.8+)
hasil = (pow(c1, a, N) * pow(c2, b, N)) % N
print("hasil        :", hasil)
print("bit(hasil)   :", hasil.bit_length())
print("bit(N)       :", N.bit_length())

# Selanjutnya, apakah hasil sudah berupa pesan asli?
```
