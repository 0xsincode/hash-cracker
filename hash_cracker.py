import hashlib
from colorama import init, Fore
import urllib.request


init()

GREEN = Fore.GREEN
RED   = Fore.RED
RESET = Fore.RESET
BLUE  = Fore.BLUE

hash_supported = """
                    > sha224
                    > sha512
                    > sha1
                    > sha256
                    > md5
"""


def sha256(hash,wordlist):
    wordlist = open(wordlist).read().splitlines()
    for password in wordlist:
        hash_ = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        if hash_ == hash:
            password = str(password)
            print(f"{GREEN}Found : {password}{RESET}")
            exit()
        else:
            password = str(password)
            print(f'{RED}Invalid Password : {password}{RESET}')

def md5(hash,wordlist):
    wordlist = open(wordlist, encoding='latin-1').read().splitlines()
    for password in wordlist:
        hash_ = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        if hash_ == hash:
            password = str(password)
            print(f"{GREEN}Found : {password}{RESET}")
            exit()
        else:
            password = str(password)
            print(f'{RED}Invalid Password : {password}{RESET}')
def sha512(hash,wordlist):
    wordlist = open(wordlist).read().splitlines()
    for password in wordlist:
        hash_ = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
        if hash_ == hash:
            password = str(password)
            print(f"{GREEN}Found : {password}{RESET}")
            exit()
        else:
            password = str(password)
            print(f'{RED}Invalid Password : {password}{RESET}')

def sha1(hash,wordlist):
    wordlist = open(wordlist).read().splitlines()
    for password in wordlist:
        hash_ = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
        if hash_ == hash:
            password = str(password)
            print(f"{GREEN}Found : {password}{RESET}")
            exit()
        else:
            password = str(password)
            print(f'{RED}Invalid Password : {password}{RESET}')

def sha224(hash,wordlist):
    wordlist = open(wordlist).read().splitlines()
    for password in wordlist:
        hash_ = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
        if hash_ == hash:
            password = str(password)
            print(f"{GREEN}Found : {password}{RESET}")
            exit()
        else:
            password = str(password)
            print(f'{RED}Invalid Password : {password}{RESET}')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SSH Bruteforce")
    parser.add_argument("hash", help="hash to crack it.")
    parser.add_argument("-w", "--wordlist", help="password wordlist.")
    parser.add_argument("-t", "--type", help="hash type.")

    args = parser.parse_args()
    hash = args.hash
    type = args.type
    wordlist = args.wordlist
    if type == "md5":
        md5(hash,wordlist)
    elif type == "sha224":
        sha224(hash,wordlist)
    elif type == "sha1":
        sha1(hash,wordlist)
    elif type == "sha512":
        sha512(hash,wordlist)
    elif type == "sha256":
        sha256(hash,wordlist)
    else:
        print("Invalid Hash Type Or Not Supported")
        print(f"Hash Supported :\n{hash_supported}")
        exit(0)
