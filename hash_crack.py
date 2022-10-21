import pyfiglet
import hashlib
from colorama import Fore

# hash = ("mustafa")
# result = hashlib.md5(hash.encode())

# print("md5 ciktisi => ",result.hexdigest())


def hash_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.md5(hash.encode()).hexdigest()
    print(Fore.GREEN+"CİKTİ =>",result)
def hash_decode():
    
    hash = input("MD5 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.md5(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)
                    break

def sha1_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.sha1(hash.encode()).hexdigest()
    print(Fore.RED+"CİKTİ => ",result)
def sha1_decode():
    hash = input("SHA1 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.sha1(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)

def sha224_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.sha224(hash.encode()).hexdigest()
    print(Fore.GREEN+"CİKTİ =>",result)
def sha224_decode():
    hash = input("SHA224 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.sha224(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)

def sha256_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.sha256(hash.encode()).hexdigest()
    print(Fore.GREEN+"CİKTİ =>",result)
def sha256_decode():
    hash = input("SHA256 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.sha256(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)

def sha384_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.sha384(hash.encode()).hexdigest()
    print(Fore.GREEN+"CİKTİ =>",result)
def sha384_decode():
    hash = input("SHA384 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.sha384(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)

def sha512_encode():
    hash = input("KELİME GİRİNİZ => ")
    result = hashlib.sha512(hash.encode()).hexdigest()
    print(Fore.GREEN+"CİKTİ =>",result)
def sha512_decode():
    hash = input("SHA512 HASH GİRİNİZ => ")
    wordlist = input("WORDLİST YOLUNU GİRİNİZ => ")

    with open(wordlist,"r",encoding="utf-8") as file:
        url_list = file.readlines()
        for i in url_list:
            for x in i.split():
                if (hashlib.sha512(x.encode()).hexdigest() == hash):
                    print(Fore.GREEN+"ŞİFRE BULUNDU :) =>",x)
                    return x
                else:
                    print(Fore.RED+"BULUNAMADI =>",x)

figlet = pyfiglet.figlet_format("HASH - CRACK ** MUSTAFA **")
print(Fore.GREEN+figlet)
islem = input(Fore.BLUE+"1  =>  MD5 ENCODE\n2  =>  MD5 DECODE\n3  =>  SHA1 ENCODE\n4  =>  SHA1 DECODE\n5  =>  SHA224 ENCODE\n6  =>  SHA224 DECODE\n7  =>  SHA256 ENCODE\n8  =>  SHA256 DECODE\n9  =>  SHA384 ENCODE\n10 => SHA384 DECODE\n11 => SHA512 ENCODE\n12 => SHA512 DECODE\n13 => ÇİKİŞ\nYapilacak işlemi seçiniz => ")
if islem == "1":
    hash_encode()
elif islem == "2":
    hash_decode()
elif islem == "3":
    sha1_encode()
elif islem == "4":
    sha1_decode()
elif islem == "5":
    sha224_encode()
elif islem == "6":
    sha224_decode()
elif islem == "7":
    sha256_encode()
elif islem == "8":
    sha256_decode()
elif islem == "9":
    sha384_encode()
elif islem == "10":
    sha384_decode()
elif islem == "11":
    sha512_encode()
elif islem == "12":
    sha512_decode()
else:
    exit
                           
                
                    
            

            







