print('''   ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   ''')

print('''       _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    ''')


import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

def incheck(direction):
    if direction=='encode'or direction=='decode':
        return
    else:
        print("Wrong choice, check input")
        sys.exit()

incheck(direction)
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  word=""
  for i in range(0,len(text)):
    j=0
    while text[i]!=alphabet[j]:
      j=j+1;
    f=shift+j
    if f>25:
        f=f-26
    word=word+alphabet[f]
  return word

def decrypt(text,shift):
  word=""
  for i in range(0,len(text)):
    j=0
    while text[i]!=alphabet[j]:
      j=j+1;
    f=j-shift
    word=word+alphabet[f]
  return word


if direction=='encode':
        print("Encrypted word is "+encrypt(text,shift))
else :
        print("Decrypted word is "+decrypt(text,shift))





