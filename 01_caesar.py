text=input("Enter text: ").upper()
key=3

enc=""
for i in text:
    enc+=chr((ord(i)-65+key)%26+65)
print("Encrypted:",enc)

dec=""
for i in enc:
    dec+=chr((ord(i)-65-key)%26+65)
print("Decrypted:",dec)