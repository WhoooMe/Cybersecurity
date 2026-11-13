# Writeup: Twin Keys (Crypto, TecFest26)

**Flag:** `TecFest26{c0mm0n_m0dulus_sh4r3d_n_br34ks_rs4}`

## 1. Ringkasan

Satu plaintext yang sama dienkripsi dengan RSA memakai **modulus N yang sama** tetapi **dua eksponen publik berbeda** (`e1`, `e2`). Kondisi ini membuat plaintext bisa dipulihkan tanpa memfaktorkan N: itulah **Common Modulus Attack**.

Twist soal: `gcd(e1, e2) = 3`, bukan 1. Serangan standar akan menghasilkan `m³ mod N`, sehingga peserta harus melakukan satu langkah tambahan, yaitu **mengambil akar pangkat tiga** (bulat).

## 2. Langkah penyelesaian

### Langkah 1: Baca kedua public key

```
openssl rsa -pubin -in pub1.pem -text -noout
openssl rsa -pubin -in pub2.pem -text -noout
```

Hasilnya:

| | pub1.pem | pub2.pem |
|---|---|---|
| Modulus `N` | sama | sama |
| Eksponen `e` | `196611` (`0x30003`) | `771` (`0x303`) |

Modulus identik, eksponen berbeda. Ciphertext `ct1` dan `ct2` adalah enkripsi dari **plaintext yang sama**:

```
c1 = m^e1 mod N
c2 = m^e2 mod N
```

### Langkah 2: Ide serangan

Dengan algoritma Euclid diperluas, cari `a`, `b` sehingga:

```
a·e1 + b·e2 = gcd(e1, e2) = g
```

Maka:

```
c1^a · c2^b = m^(a·e1) · m^(b·e2) = m^(a·e1 + b·e2) = m^g   (mod N)
```

Jika `g = 1`, langsung didapat `m`. Itulah isi `attack.py` dari repositori referensi.

### Langkah 3: Hitung gcd dan koefisien Bézout

```
e1 = 196611 = 3 × 65537
e2 =    771 = 3 × 257
gcd(e1, e2) = 3

a = -128,  b = 32641
check: 196611·(-128) + 771·32641 = -25166208 + 25166211 = 3  ✓
```

Karena gcd bukan 1, hasil serangan adalah `m³ mod N`. Script bawaan repositori (`attack.py`) yang langsung memanggil `long_to_bytes` pada hasilnya akan mengeluarkan data acak, bukan flag.

### Langkah 4: Hitung `m³ mod N`

Salah satu koefisien negatif (`a = -128`), sehingga `c1^a` berarti **invers modular** dari `c1` pangkat 128. Python 3.8+ menangani ini langsung lewat `pow(c1, -128, N)`:

```python
m3 = (pow(c1, a, N) * pow(c2, b, N)) % N
```

### Langkah 5: Ambil akar pangkat 3

Flag pendek (sekitar 45 byte ≈ 360 bit), sedangkan N 2048 bit. Maka `m³` hanya sekitar 1080 bit dan **lebih kecil dari N**. Artinya `m³ mod N = m³` sebagai bilangan bulat biasa, tanpa efek modulo. Cukup ambil akar pangkat 3 bulat:

```python
m = iroot(m3, 3)
```

### Langkah 6: Ubah ke teks

```
long_to_bytes(m) = TecFest26{c0mm0n_m0dulus_sh4r3d_n_br34ks_rs4}
```

## 3. Script solver

Hanya butuh `pycryptodome` (tanpa Sage):

```python
import os, base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def iroot(n, k):
    lo, hi = 0, 1 << ((n.bit_length() // k) + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo

k1 = RSA.import_key(open(os.path.join(DIST, "pub1.pem"), "rb").read())
k2 = RSA.import_key(open(os.path.join(DIST, "pub2.pem"), "rb").read())
assert k1.n == k2.n
N, e1, e2 = k1.n, k1.e, k2.e
c1 = bytes_to_long(base64.b64decode(open(os.path.join(DIST, "ct1.txt")).read()))
c2 = bytes_to_long(base64.b64decode(open(os.path.join(DIST, "ct2.txt")).read()))

g, a, b = xgcd(e1, e2)
mg = (pow(c1, a, N) * pow(c2, b, N)) % N     # m^g mod N
m = iroot(mg, g)
assert pow(m, g) == mg
print(long_to_bytes(m).decode())
```

Output:

```
e1 = 196611 | e2 = 771
gcd = 3 | a = -128 | b = 32641
Flag : TecFest26{c0mm0n_m0dulus_sh4r3d_n_br34ks_rs4}
```
