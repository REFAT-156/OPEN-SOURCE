#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo ="""\033[92;1m   
\033[92;1m╭───────────────────────────────────────────────────────────╮
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│        \033[91;1m██████╗  \033[92;1m███████╗ \033[93;1m███████╗  \033[94;1m█████╗  \033[96;1m████████╗      \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔════╝ \033[93;1m██╔════╝ \033[94;1m██╔══██╗ \033[96;1m╚══██╔══╝      \033[92;1m│
\033[92;1m│       \033[91;1m ██████╔╝ \033[92;1m█████╗   \033[93;1m█████╗   \033[94;1m███████║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m██╔══██╗ \033[92;1m██╔══╝   \033[93;1m██╔══╝   \033[94;1m██╔══██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│       \033[91;1m ██║  ██║ \033[92;1m███████╗ \033[93;1m██║      \033[94;1m██║  ██║    \033[96;1m██║         \033[92;1m│
\033[92;1m│        \033[91;1m╚═╝  ╚═╝ \033[92;1m╚══════╝ \033[93;1m╚═╝      \033[94;1m╚═╝  ╚═╝    \033[96;1m╚═╝         \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m│           \x1b[1;33m╔══════════════════════════════════╗\033[1;91m            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╔══════════════════════════════╗\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] TOOL NAME : BYPASS TOOL   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] AUTHOR    : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GITHUB    : REFAT-156     \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] FACEBOOK  : REFAT SHAHRIAR\033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] GROUP     : TERMUX LOVER  \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m║\033[92;1m[\033[91;1m●\033[92;1m] WHATSAPP  : 01613732902   \033[91;1m║ \x1b[1;33m║            \033[92;1m│
\033[92;1m│           \x1b[1;33m║ \x1b[1;91m╚══════════════════════════════╝\033[1;33m ║            \033[92;1m│
\033[92;1m│           \x1b[1;33m╚══════════════════════════════════╝\033[1;91m            \033[92;1m│
\033[92;1m│\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m─────────────────────\033[91;1m●\033[96;1m●\033[93;1m●\033[94;1m●\033[95;1m●\033[96;1m●\033[92;1m│
\033[92;1m╰───────────────────────────────────────────────────────────╯
""" 

def refat():

    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('───────────────────────────────────────────────────────────')
    print(' \033[33;1m[1] BYPASS MKDIR')
    print(' \033[32;1m[2] BYPASS 4MBF ')
    print(' \033[34;1m[3] BYPASS AEROC')
    print(' \033[31;1m[4] BYPASS FILE MAKING')
    print(' \033[35;1m[5] BYPASS ELITE')
    print(' \033[36;1m[6] BYPASS AKING')
    print(' \033[37;1m[7] BYPASS KRISHNA')
    print(' \033[31;1m[8] BYPASS ALVINO')
    print(' \033[32;1m[9] BYPASS AZIM ')
    print(' \033[33;1m[10] BYPASS BFF DEC')
    print(' \033[34;1m[11] BYPASS ENC PY3')
    print(' \033[35;1m[12] BYPASS HAMZA ')
    print(' \033[36;1m[13] BYPASS INDO ')
    print(' \033[37;1m[14] BYPASS JEWEL ')
    print(' \033[32;1m[15] BYPASS SSB ')
    print('\033[31;1m [E] EXIT ')
    print('───────────────────────────────────────────────────────────')
    print('')
    refat_brand = input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
    if refat_brand in ('1', '01'):
        os.system(' python 2008.py')
    if refat_brand in ('2', '02'):
        os.system('python 4mbf_dec.py')
    if refat_brand in ('3', '03'):
        os.system('python Aeroc4Mbf_dec.py')
    if refat_brand in ('4', '04'):
        os.system('python2 Dump.py')
    if refat_brand in ('5', '05'):
        os.system('python Elitedec.py')
    if refat_brand in ('6', '06'):
        os.system('python FUCK-AKING.py')
    if refat_brand in ('7', '07'):
        os.system('python FUCK-KRISHNA.py')
    if refat_brand in ('8', '08'):
        os.system('python alvino_dec.py')
    if refat_brand in ('9', '09'):
        os.system('python azim.py')
    if refat_brand in ('10', '10'):
        os.system('python bff_dec.py')
    if refat_brand in ('11', '11'):
        os.system('python encrypt3.py')
    if refat_brand in ('12', '12'):
        os.system('python hamza_dec.py')
    if refat_brand in ('13', '13'):
        os.system('python indo_dec.py')
    if refat_brand in ('14', '14'):
        os.system('python dec_jewel.py')
    if refat_brand in ('15', '15'):
        os.system('python ssb_dec.py')
    if refat_brand in ('E', 'ee'):
        pass

refat()
