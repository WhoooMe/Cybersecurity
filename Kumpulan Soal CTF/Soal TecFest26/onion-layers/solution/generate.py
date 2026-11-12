import base64, binascii, os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "chall.txt")

flag = b"TecFest26{l4y3r5_0f_enc0d1ng_x0r_m4st3r}"
key = b"Unkn0wn"

x  = bytes(b ^ key[i % len(key)] for i, b in enumerate(flag))
l1 = base64.b64encode(x)
l2 = l1[::-1]
l3 = binascii.hexlify(l2)
l4 = base64.b32encode(l3)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    f.write(l4.decode() + "\n")

print("chall.txt dibuat di:", OUT)
print(l4.decode())