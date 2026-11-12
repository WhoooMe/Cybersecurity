import base64, binascii, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "chall.txt")   # sesuaikan lokasi

c = open(PATH).read().strip()
c = base64.b32decode(c)             # layer 1: Base32
c = binascii.unhexlify(c)           # layer 2: Hex
c = base64.b64decode(c[::-1])       # layer 3-4: Reverse + Base64

crib = b"TecFest26{"
ks = bytes(c[i] ^ crib[i] for i in range(len(crib)))   # potongan key stream
print("Key stream:", ks)

# cari panjang key: potongan terpendek yang berulang pada key stream
for L in range(1, len(ks)):
    if all(ks[i] == ks[i - L] for i in range(L, len(ks))):
        key = ks[:L]
        break

print("Key  :", key, f"(panjang {len(key)})")
print("Flag :", bytes(b ^ key[i % len(key)] for i, b in enumerate(c)).decode())