text=input("Enter text: ").upper()
a=3
b=4
ainv=pow(a,-1,26)
enc=""
for i in text:
    enc+=chr((a*(ord(i)-65)+b)%26+65)
print("Encrypted:",enc)

dec=""
for i in enc:
    dec+=chr((ainv*(ord(i)-65-b))%26+65)
print("Decrypted:",dec)