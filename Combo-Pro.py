""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

try:
	import os, sys, requests, string, time,random
	from time import sleep
except ImportError:
	os.system("pip install requests")
	
	
	
	
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

def baner():
	banera =f"""{E}
	
     8888888b.       8888888b.        .d88888b.  
     888   Y88b      888   Y88b      d88P" "Y88b 
     888    888      888    888      888     888 
     888   d88P      888   d88P      888     888 
     8888888P"       8888888P"       888     888 
     888             888 T88b        888     888 
     888             888  T88b       Y88b. .d88P 
     888             888   T88b       "Y88888P"  
                                            
 \033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : SIDRA ELEZZ
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : SIDRATOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mYOUTUBE    : TERMUX TOOLS
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/SIDRAELEZZ\033[1;91m
  ---------------------------
"""     

	for sidra in banera.splitlines():
		time.sleep(0.05)
		print(sidra)
		
def clear():
	if os.name == 'nt':
		os.system('cls')
		os.system('title Cod BY SidraELEzz ')
	else:
		os.system('clear')


def COMBO():
	clear();baner()
	token = input(E+"("+C+"⌯"+E+") "+C+"TOKEN BOT DANE :"+B)
	ID = input(E+"("+C+"⌯"+E+") "+C+"ID TELEGRAM YOU :"+B)
	clear();baner()
	sn = int(input(E+"("+C+"⌯"+E+") "+C+"How Many Time (x2): "))
	print ("")
	os.system('rm -rf pro.txt')
	i=1
	for i in range (0,sn):
		i = 1+1
		USER = ''.join(random.choices( string.digits + string.ascii_letters, k = 4))
		PASA = USER+"12345",USER+"123","12345567890","1234512345","1122334455","1234554321","1234554321","1q2w3e4r5t","Aa123123","1111aaaa","20012001","19981998","1234qwer","10001000","19901990"
		PASS = random.choice(PASA)
		LISTA = USER+":"+PASS
		print (E+"["+C+"COMBO PRO "+E+"] "+str(LISTA))
		with open("pro.txt","a") as pro:
			pro.write(str(LISTA)+"\n")
			
	
	try:
		massage = ("➥ • Done Combo ✓\n\n➥• USER : PASS \n\n➥• Number : "+str(sn)+"\n\n. — — — — —  — — — — — . \n➥• @SidraTools")
		requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={ID}&caption={massage}', files={'document':open('pro.txt', 'rb')})
		print(E+" \n\nDone Combo ✓"+H+"save > pro.txt")
	except:pass
	sleep (10)
		


while True:
	COMBO()  
