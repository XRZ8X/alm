""" 
-------------------------------------------------------------------------
- Cod BY : SidraELEzz
- Github : https://github.com/SidraELEzz
- Telegram: https://t.me/SidraTools
- Telegram: https://t.me/tt_rq
-------------------------------------------------------------------------
      
""" 

try:
	import requests, os, sys, time,json,random,re
	import binascii
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
	
888      .d88888b.   .d8888b.  8888888 888b    888 
888     d88P" "Y88b d88P  Y88b   888   8888b   888 
888     888     888 888    888   888   88888b  888 
888     888     888 888          888   888Y88b 888 
888     888     888 888  88888   888   888 Y88b888 
888     888     888 888    888   888   888  Y88888 
888     Y88b. .d88P Y88b  d88P   888   888   Y8888 
88888888 "Y88888P"   "Y8888P88 8888888 888    Y888 
                                                                                                 
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


class Twitter():
	
	def __init__(self, username,password):
		self.username = str(username) 
		self.password = str(password)
		self.session = requests.Session()
		self.url = "https://mobile.twitter.com/sessions"
		self.home_url = 'https://mobile.twitter.com/session/new'
		self.url_cod = 'https://mobile.twitter.com/account/login_challenge'
		self.header = {
        'user-agent': 'Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3417; U; en) Presto/2.8.119 Version/11.10'}
		self.headers={
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
	    'Content-Length': '901',
	    'Content-Type': 'application/x-www-form-urlencoded',
		'Host': 'twitter.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
        'origin': 'https://mobile.twitter.com',
        'referer': 'https://mobile.twitter.com/login',
	    'TE': 'Trailers',
	    'Upgrade-Insecure-Requests': '1',}
		
	def get_token(self, size=16):
		token = random.getrandbits(size * 8).to_bytes(size, 'big')
		return binascii.hexlify(token).decode()
        
        
	def login(self):
		 
		"@SidraTools"
		try:
			respons = self.session.get(self.home_url, headers=self.header)
			token = re.findall(r'<input name="authenticity_token" type="hidden" value="(.*?)"', respons.text)[0]
			
		except:
			token = self.get_token()
			self.session.cookies.clear()
			self.session.cookies.update({'_mb_tk': token})
		
		data = {
        'authenticity_token': token,
        'session[username_or_email]': self.username,
        'session[password]': self.password,
        'remember_me': '1',
         'wfa': '1',
         'commit': 'Log in',
         'ui_metrics': ''}
		response = self.session.post(self.url, headers=self.headers, data=data,allow_redirects=True)
		#print (response.text)
		if ('/account/login_challenge?challenge_id') in str(response.text):
			print(H+" </>  LOGIN  ACCOUNT CHECKPOINT ")
			cod = input(E+"("+C+"⌯"+E+") "+C+"Enter The Code That You Sent To The Email : ")
			userld = re.findall(r'enc_user_id=(.*?)">', response.text)[0]
			check = re.findall(r'challenge_id=(.*?)&amp;', response.text)[0]
			data_cod = {
            'authenticity_token': token,
            'challenge_id': check,
            'enc_user_id': userld,
            'challenge_type': 'TemporaryPassword',
            'platform': 'web',
            'redirect_after_login': '/',
            'remember_me': 'true',
            'challenge_response': cod}
			response = self.session.post(self.url_cod, headers=self.headers, data=data_cod, allow_redirects=True)
			response_text = response.text.replace('&quot', '').replace(';', '')
			
			
		if response.status_code == 200:
			cookie = self.session.cookies.get_dict()
			cookies = json.dumps(cookie)
			print(E+" </>  LOGIN  ACCOUNT SUCCESSFUL ")
			print (H)
			print (cookies)
			
		else:
			print(A+" </>  LOGIN  ACCOUNT ERROR ")
			exit()
			
		
if __name__ == "__main__":
	clear();baner()
	username = input(E+"("+C+"⌯"+E+") "+C+" USERNAME "+A+" : "+E)
	password = input(E+"("+C+"⌯"+E+") "+C+" PASSWORD "+A+" : "+E)
	print ("")
 
	
		
		
	Sidra = Twitter(username,password)
	try:
		Sidra.login()
		
	except Exception as error:
		print(error)

