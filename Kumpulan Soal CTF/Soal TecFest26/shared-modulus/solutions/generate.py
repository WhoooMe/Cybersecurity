import os, base64
from Crypto.Util.number import getPrime, bytes_to_long, GCD
from Crypto.PublicKey import RSA

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "dist")
os.makedirs(DIST, exist_ok=True)

FLAG = b"TecFest26{c0mm0n_m0dulus_sh4r3d_n_br34ks_rs4}"
E1 = 3 * 65537      # 196611
E2 = 3 * 257        # 771   -> gcd(E1, E2) = 3 (twist soal)

def gen_prime():
    # p % 3 == 2 supaya 3 tidak membagi phi(N) -> E1 & E2 valid secara RSA
    while True:
        p = getPrime(1024)
        if p % 3 == 2:
            return p

while True:
    p, q = gen_prime(), gen_prime()
    if p == q:
        continue
    phi = (p - 1) * (q - 1)
    if GCD(E1, phi) == 1 and GCD(E2, phi) == 1:
        break

N = p * q
m = bytes_to_long(FLAG)
assert m < N and pow(m, 3) < N      # syarat agar akar pangkat 3 bisa diambil

c1 = pow(m, E1, N)
c2 = pow(m, E2, N)

def b64(x):
    return base64.b64encode(x.to_bytes((N.bit_length() + 7) // 8, "big")).decode()

with open(os.path.join(DIST, "pub1.pem"), "wb") as f:
    f.write(RSA.construct((N, E1)).export_key("PEM") + b"\n")
with open(os.path.join(DIST, "pub2.pem"), "wb") as f:
    f.write(RSA.construct((N, E2)).export_key("PEM") + b"\n")
with open(os.path.join(DIST, "ct1.txt"), "w") as f:
    f.write(b64(c1) + "\n")
with open(os.path.join(DIST, "ct2.txt"), "w") as f:
    f.write(b64(c2) + "\n")

print("Selesai. File ada di:", DIST)
