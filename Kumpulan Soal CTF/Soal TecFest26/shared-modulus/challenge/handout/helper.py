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