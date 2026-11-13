import os, base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")

def xgcd(a, b):
    """Return (g, x, y) sehingga a*x + b*y = g."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def iroot(n, k):
    """Akar pangkat k bulat (floor) dengan binary search."""
    lo, hi = 0, 1 << ((n.bit_length() // k) + 1)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo

# 1. Baca public key dan ciphertext
k1 = RSA.import_key(open(os.path.join(DIST, "pub1.pem"), "rb").read())
k2 = RSA.import_key(open(os.path.join(DIST, "pub2.pem"), "rb").read())
assert k1.n == k2.n, "modulus berbeda, bukan common modulus"
N, e1, e2 = k1.n, k1.e, k2.e
c1 = bytes_to_long(base64.b64decode(open(os.path.join(DIST, "ct1.txt")).read()))
c2 = bytes_to_long(base64.b64decode(open(os.path.join(DIST, "ct2.txt")).read()))
print("e1 =", e1, "| e2 =", e2)

# 2. Common modulus attack (generalisasi untuk gcd(e1, e2) = g >= 1)
g, a, b = xgcd(e1, e2)
print("gcd =", g, "| a =", a, "| b =", b)
mg = (pow(c1, a, N) * pow(c2, b, N)) % N      # = m^g mod N  (pow eksponen negatif = invers modular)

# 3. Ambil akar pangkat g
m = iroot(mg, g)
assert pow(m, g) == mg
print("Flag :", long_to_bytes(m).decode())
