text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

enc =""
for i in range(len(text)):
    p=ord(text[i])-65
    k=ord(key[i%len(key)])-65
    enc+=chr((p+k)%26+65)
print("Encrypted:",enc)

dec=""
for i in range(len(enc)):
    c=ord(enc[i])-65
    k=ord(key[i%len(key)])-65
    dec+=chr((c-k)%26+65)
print("Decrypted:",dec)