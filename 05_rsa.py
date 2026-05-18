from sympy import gcd, mod_inverse

p=int(input("Enter p:"))
q=int(input("Enter q:"))

n=p*q
phi=(p-1)*(q-1)

possible_e=[]
for i in range(2,phi):
    if gcd(i,phi)==1:
        possible_e.append(i)
print(possible_e)
e=int(input("Select e:"))

d=mod_inverse(e,phi)
print("Private key:",(d,n))
print("Public key:",(e,n))

m=int(input("Enter message:"))
c=pow(m,e,n)
print("Encrypted",c)
dec=pow(c,d,n)
print("Decrypted",dec)