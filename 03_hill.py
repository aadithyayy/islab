text=input("Enter text: ").upper()
key=[[2,3],[3,4]]

enc=""
for i in range(0,len(text),2):
    p1=ord(text[i])-65
    p2=ord(text[i+1])-65

    c1=(key[0][0]*p1+key[0][1]*p2)%26+65
    c2=(key[1][0]*p1+key[1][1]*p2)%26+65

    enc+=chr(c1)+chr(c2)
print("Encrypted:",enc)