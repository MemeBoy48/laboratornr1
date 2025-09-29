alfabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTUVWXYZ"

def encrypt(text, key):
    r = ""
    for i, c in enumerate(text):
        r += alfabet[(alfabet.index(c) + alfabet.index(key[i % len(key)])) % len(alfabet)]
    return r

def decrypt(text, key):
    r = ""
    for i, c in enumerate(text):
        r += alfabet[(alfabet.index(c) - alfabet.index(key[i % len(key)])) % len(alfabet)]
    return r

while True:
    op = input("Alege (c=criptare, d=decriptare, x=exit): ").lower()
    if op == "x":
        break
    key = input("Cheia (min 7 litere): ").replace(" ", "").upper()
    if len(key) < 7:
        print("Cheia prea scurta")
        continue
    msg = input("Mesaj: ").replace(" ", "").upper()
    if op == "c":
        print("Criptat:", encrypt(msg, key))
    elif op == "d":
        print("Decriptat:", decrypt(msg, key))
    else:
        print("Optiune incorecta")
