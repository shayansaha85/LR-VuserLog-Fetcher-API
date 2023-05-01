import random
import uuid

def gen_apiKey():
    
    keyFileName = str(uuid.uuid4())
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#=*&1234567"
    enc_key = {}
    alphabets_distorted = ""
    i = 0
    while i<len(alphabets):
        rch = alphabets[random.randint(0, (len(alphabets)-1))]
        if alphabets_distorted.count(rch) == 0:
            alphabets_distorted += rch
            i = i+1
    i=0
    file = open(f"./apiKeys/{keyFileName}.pem", "w")
    file.write(alphabets_distorted)
    file.close()

i=0
while i<10:
    gen_apiKey()
    i=i+1