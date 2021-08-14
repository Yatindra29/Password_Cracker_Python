import os
import hashlib

input_hash=input("Enter md5 hash of victim: ")
try:
    pass_file=open("10-million-password-list-top-1000000.txt","r")
except:
    print("password file not opened")
    quit()

for password in pass_file:
    password=password.replace("\n","")
    enc=password.encode("utf-8")
    digits=hashlib.md5(enc.strip()).hexdigest()

    if input_hash==digits:
        print("Password is found")
        print("Password is:"+ password)
        break