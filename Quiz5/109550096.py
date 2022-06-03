from hashlib import md5

def encrypt(s):
    cipher = md5()
    cipher.update(s)
    return cipher.hexdigest()
   
cin=input()
bcin=bytes.fromhex(str(cin))
four_char=encrypt(bcin)[0:4]
print(four_char,end=' ')

for i in range(10000000000000000000000000000000,100000000000000000000000000000000):
    cipher_text=md5()
    cipher_text=bytes.fromhex(str(i))
    cipher_text=encrypt(cipher_text)
    if cipher_text[0:4]==four_char:
        print(str(i))
        break