
def encrypt():
    while True:
        message = input("Introdu un mesaj, sa contina doar litere din alfabetul englez: ")
        mes = message.replace(" ", "")
        if not mes.isalpha():
            print("Mesajul trebuie sa contina doar litere!")
            continue
        break
    
    MES = message.upper().replace(" ", "")
    alfabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_mod = len(alfabet1)
    key = int(input("Introdu cheia numerica: "))
    e = []
    
    # Sarcina 1
    # Criptarea mesajului cu cheia numerica PRIN CIFRA LUI CEZAR
    for char in MES:
        for index, letter in enumerate(alfabet1):
            if char == letter:
                encryption = (index + key) % num_mod
                e.append(encryption)
    
    # Sarcina 1.2
    # CRIPTAREA MESAJULUI CU CHEIA DE CRIPTARE PRIN SUBSTITUTIE LITERALA
    alfabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key2 = None
    while key2 is None or not key2.isalpha() or len(key2) < 7:
        key2 = input("Introdu cheia de criptare minim 7 caractere (doar cu litere): ")
        if not key2.isalpha() or len(key2) < 7:
            print("Cheia trebuie sa contina doar litere si sa aiba minim 7 caractere!")
            key2 = None
    
    k2alf = ''.join(dict.fromkeys(key2.upper() + alfabet2))
    
    encrypted_message = ""
    for i in range(len(MES)):
        for index, letter in enumerate(k2alf):
            if e[i] == index:
                encrypted_message += letter
    
    return encrypted_message

def decrypt():
    encrypted_message = input("introdu cuvantul criptat: ")
    ENCRY = encrypted_message.upper().replace(" ", "")
    e = []
    
    # Sarcina 1.2
    # Decriptarea mesajului cu cheia de criptare prin substitutie literala
    alfabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key2 = None
    while key2 is None or not key2.isalpha() or len(key2) < 7:
        key2 = input("Introdu cheia de criptare(doar cu litere): ")
        if not key2.isalpha() or len(key2) < 7:
            print("Cheia trebuie sa contina doar litere si sa aiba minim 7 caractere!")
            key2 = None
    
    k2alf = ''.join(dict.fromkeys(key2.upper() + alfabet2))
    for char in ENCRY:
        for index, letter in enumerate(k2alf):
            if char == letter:
                e.append(index)
    
    # Sarcina 1
    # Decriptarea mesajului cu cheia numerica prin cifra lui Cezar
    key = int(input("Introdu cheia numerica: "))
    alfabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_mod = len(alfabet1)
    
    decrypted_message = ""
    for index_value in e:
        decrypted_num = (index_value - key + num_mod) % num_mod
        decrypted_message += alfabet1[decrypted_num]
    
    return decrypted_message
while True:
    print("Meniu:")
    print("1. Criptare mesaj")
    print("2. Decriptare mesaj")
    choice = input("Alege optiunea (1 sau 2): ")
    if choice == '1':
        encrypted = encrypt()
        print("Mesaj criptat:", encrypted)
        break
    elif choice == '2':
        decrypted = decrypt()
        print("Mesaj decriptat:", decrypted)
        break
    else:
        print("Optiune invalida. Alege 1 sau 2.")