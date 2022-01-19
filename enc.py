import os, base64, sys, time
from pprint import pformat
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]
def em():
    B="\033[1;30m" # Black
    R="\033[1;31m" # Red
    G="\033[1;32m" # Green
    Y="\033[1;33m" # Yellow
    Bl="\033[1;34m" # Blue
    P="\033[1;35m" # Purple
    C="\033[1;36m" # Cyan
    W="\033[1;37m" # White 
	
    
    in_file= input(W+ "Input File  > "+R )
    if not os.path.isfile(in_file):
            print(R+' File not found')
            os.system("sleep 2")
            import UAP_TEAM
            UAP_TEAM.start()
    out_file= input(W+ "Output File  > " + G)
    with open(in_file) as in_f, open(out_file, "w") as out_f:
        out_f.write("# - Encrypted By:UAP-TEAM\n\n")
        out_f.write(encode_string(in_f.read(), alphabet))
        print(G+out_file+" saved in ")
def vr():
	B="\033[1;30m" # Black
	R="\033[1;31m" # Red
	G="\033[1;32m" # Green
	Y="\033[1;33m" # Yellow
	Bl="\033[1;34m" # Blue
	P="\033[1;35m" # Purple
	C="\033[1;36m" # Cyan
	W="\033[1;37m" # White 
	var= input(C + "Variable to be used(Must Required)  > " + G)
	if (var==""):
		print(R + " No variable")
		os.system("sleep 3")
		import UAP_TEAM
		UAP_TEAM.start()
	if (var.find(" ")!= -1):
		print(R+" Only one word!")
		os.system("sleep 3")
		import UAP_TEAM
		UAP_TEAM.start()
	VARIABLE_NAME = var * 100
	in_file = input(Y+ "Input file  > "+G)
	if not os.path.isfile(in_file):
		print(R+' File not found')
		os.system("sleep 2")
		import UAP_TEAM
		UAP_TEAM.start()
	out_file = input(W + "Output file  > " + R)
	with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f,open(out_file, 'w') as out_f:
		file_content = in_f.read()
		obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
		out_f.write("# - Encrypted By: UAP-TEAM\n\n"+obfuscated_content)
	sprint(G + out_file + " saved in ")






def la():
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
	    from random import random
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
	        from random import random
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
	
	try:
		import pathlib
	except:
		os.system('pip install pathlib')
	try:
	    code='# Enc by :UAP-TEAM\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"exec"))(%s,compile))'
	    computer=0
	    file=input(f'\n{R}File : {G}')
	    count=int(input(f'\n{R}Count : {G}'))
	    if(count<300):
	        out=input(f'\n {R}Output : {G}')
	        read1=open(file).read()
	        repr1=repr(zlib.compress(read1.encode('utf-8')))
	        new1=open(out, 'w')
	        new1.write(code % repr1)
	        new1.close()
	        while(count>=computer):
	        	read2=open(out).read()
	        	repr2=repr(zlib.compress(read2.encode('utf-8')))
	        	new2=open(out, 'w')
	        	new2.write(code % repr2)
	        	new2.close()
	        	computer+=1
	        	print('\n\033[1;97mobfuscating file at | '+Y+f'{computer}')
	        	print(f'\n\033[1;92mencrypt success | '+Y+f'{out}')
	except ValueError:
	    print('\033[1;31mEnter a number in the count')
	except KeyboardInterrupt:
		print('\n\033[1;31mBe stopped')
	import UAP_TEAM
	UAP_TEAM.start()
def c():	
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
	    from random import random
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
	        from random import random
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
	
	try:
		import pathlib
	except:
		os.system('pip install pathlib')
	nice=("")
	import os, sys, time, base64, marshal, zlib, py_compile
	R = '\x1b[1;31m'
	G = '\x1b[1;32m'
	Y = '\x1b[1;33m'
	B = '\x1b[1;34m'
	C = '\x1b[1;36m'
	W = '\x1b[1;37m'
	def slowprint(s):
		for c in s + '\n':
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.01)
	try:
		print('')
		slowprint(G + ' Launching Encryption Tool...')
		time.sleep(2)
		print('')
		file = input(G + 'File name' + C + ' > ' + Y)
		print('')
		c = input(G + ' Output File Name' + C + ' > ' + Y)
		print('')
		slowprint(G + ' Encrypting...')
		print('')
		fileopen = open(file).read()
		sa = compile(fileopen, 'dg', 'exec')
		sb = marshal.dumps(sa)
		sc = zlib.compress(sb)
		sd = base64.b85encode(sc)
		b = '#https://t.me/U_A_P_TEAM\nimport marshal,zlibbase64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
		d = open(c, 'w')
		d.write(b)
		d.close()
		time.sleep(3)
		slowprint(G + ' Encryption Completed...')
		time.sleep(3)
		print('')
		print(G + ' Output File Name: ' + Y, c)
		print('')
		print(W)
	except :
		import UAP_TEAM
		UAP_TEAM.start()
