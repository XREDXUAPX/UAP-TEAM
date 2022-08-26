#################
from time import *
import socket
import os
from datetime import datetime
##################
os.system ('clear') 
P='\033[1;37m'
O='\033[1;36'
def nmap()
	print(P+"""     _____   _____       ___   _____  
	    |  _  \ | ____|     /   | |  _  \ 
	    | | | | | |__      / /| | | | | | 
	    | | | | |  __|    / / | | | | | | 
	    | |_| | | |___   / /  | | | |_| | 
	    |_____/ |_____| /_/   |_| |_____/ """)
	print(P+'\t----'+O+'----'+P+'----'+O+'----'+P+'----'+O+'---') 
	def slowprint(s):
	    for c in s + '\n' :
	         sys.stdout.write(c)
	         sys.stdout.flush()
	         time.sleep(5. / 100)
	logo ='~])» Welcome to with Dead in life Dark'
	print ('\033[1;35m'+logo) 
	##################
	ip=input ("\033[1;35m===> ENTER YOUR IP TO START:  \033[1;37m") 
	t1=datetime.now() 
	print ("------------------------------------------------") 
	print("\033[1;32m~» Scaning Start.. \033[1;37m%s \033[1;32m Please Wait.. "%ip) 
	sleep(1)
	print ("------------------------------------------------") 
	##################
	try:
	   for port in range(1,4553): 
	       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	       s.settimeout(0.004)
	       dead= s.connect_ex((ip,port))
	       if dead==0:
	          s=socket.getservbyport(port) 
	          print(P+" [+]"+"\033[1;32m PORTS IS OPEN===> \033[1;31m{} \033[1;32mSERVICE IS==>  \033[1;31m{} ".format(port,s))
	          t2=datetime.now() 
	          t3=t2-t1
	          print(" \033[94m --------------------Welcom---------------------")
	          print(" \033[1;36mScaning Resume On %s"%t3) 
	   os.system('UAP')          
	except:
	    pass
	    print("\033[2;31m «~~~~No Any Ports !??~~~~» ") 
	    os.system('UAP')  
################################