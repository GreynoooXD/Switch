# coding=utf-8
# created scrypt by Lukman-xd
# scrypt update tanggal 26-november-2023

import os, sys
try:
	import requests
except (ModuleNotFoundError, ImportError):
	print("\n [!] sedang menginstall module requests!")
	os.system("pip install requests")
try:
	import concurrent.futures
except (ModuleNotFoundError, ImportError):
	print("\n [!] sedang menginstall module futures!")
	os.system("pip install futures")
try:
	import bs4
except (ModuleNotFoundError, ImportError):
	print("\n [!] sedang menginstall module bs4!")
	os.system("pip install bs4")

import requests, re, bs4, os, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as Lukman_XD
from bs4 import BeautifulSoup as parser
from datetime import datetime
ses=requests.Session()

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI :V
xrom = random.choice([P,O,M,K,H])

dic = {"1": "january","2": "february","3": "march","4": "april","5": "may","6": "june","7": "july","8": "august","9": "september","10": "october","11": "november","12": "december"}
dic2 = {"01": "january","02": "february","03": "march","04": "april","05": "may","06": "june","07": "july","08": "august","09": "september","10": "october","11": "november","12": "december"}
hari_ini = (f"{datetime.now().day}-{dic[(str(datetime.now().month))]}-{datetime.now().year}")

def banner():
	os.system("clear")
	print('''%s_______  ______ _______ _______ _     _
|       |_____/ |_____| |       |____/
|_____  |    \_ |     | |_____  |    \_ %s
____________________________________________%s
 [%s•%s] Author   : Lukman-xd
 [%s•%s] Github   : github.com/Lukman-xd-404
 [%s•%s] Facebook : arkanbigal.alkan
 [%s•%s] Suport   : axis, xl, my3%s
____________________________________________%s'''%(xrom,O,P,O,P,O,P,O,P,O,P,O,N))

def login():
	banner()
	print(' %s(%s+%s) Pastikan kamu menggunakan akun tumbal, bukan pribadi'%(P,H,P))
	cookies = {"cookie": input(f' (%) Masukan cookie : {K}')}
	if "" in cookies['cookie'] or " " in cookies['cookie']:
		print(' %s(%s!%s) Masukan cookie akun facebook tumbal dengan benar'%(P,M,P))
		time.sleep(2);login()
	else:
		try:
			for titik in['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']:
				print(" %s(%s*%s) Sedang proses convert cookie ke token, mohon tunggu%s"%(P,O,P,titik), end="\r");sys.stdout.flush()
			token = convert_cookie('EAAM', cookies)
			if 'EAA' not in token:token = convert_cookie('EAAT', cookies)
			open("data/.token.txt","w").write(token);open("data/.cookie.txt","w").write(cookies['cookie'])
			print('\n %s(%s•%s) Token : %s%s'%(P,H,P,H,token))
			print('\n %s(%s+%s) Login cookie berhasil'%(P,H,P))
#			followmy("100022219411831", cookies)
			sys.exit()
		except Exception as e:
			token = '-'
			print('\n %s(%s•%s) Token : %s%s'%(P,H,P,H,token))
			print(' %s(%s!%s) Error : %s%s'%(P,M,P,M,e))
			print('\n %s(%s!%s) Login cookie gagal'%(P,M,P))
			exit()
	
def convert_cookie(main, cookies):
	try:
		if 'EAAM' in main:
			ses.headers.update({"content-type": "application/x-www-form-urlencoded",})
			response = json.loads(ses.post("https://graph.facebook.com/v2.6/device/login/", data={"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038","scope": ""}).text)
			code, user_code = response["code"], response["user_code"]
			verification_url, status_url = ("https://m.facebook.com/device?user_code=%s"%(user_code)), ("https://graph.facebook.com/v2.6/device/login_status?method=post&code=%s&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback"%(code))
			ses.headers.pop("content-type");ses.headers.update({"sec-fetch-mode": "navigate","user-agent": "Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36","sec-fetch-site": "cross-site","Host": "m.facebook.com","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-dest": "document",})
			response2 = ses.get(verification_url, cookies=cookies).text
			if "Bagaimana Anda ingin masuk ke Facebook?" in str(response2) or "/login/?next=" in str(response2):pass
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
				data = {"fb_dtsg": fb_dtsg,"jazoest": jazoest,"qr": 0,"user_code": user_code,}
				ses.headers.update({"origin": "https://m.facebook.com","referer": verification_url,"content-type": "application/x-www-form-urlencoded","sec-fetch-site": "same-origin",})
				response3 = ses.post("https://m.facebook.com{}".format(action), data=data, cookies=cookies)
				if "https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=" in str(response3.url):
					ses.headers.pop("content-type");ses.headers.pop("origin")
					response4 = ses.post(response3.url, data=data, cookies=cookies).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
					scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
					display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
					user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
					logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
					auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
					encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
					return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
					ses.headers.update({"origin": "https://m.facebook.com","referer": response3.url,"content-type": "application/x-www-form-urlencoded",})
					data = {"fb_dtsg": fb_dtsg,"jazoest": jazoest,"scope": scope,"display": display,"user_code": user_code,"logger_id": logger_id,"auth_type": auth_type,"encrypted_post_body": encrypted_post_body,"return_format[]": return_format,}
					response5 = ses.post("https://m.facebook.com{}".format(action), data=data, cookies=cookies).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					ses.headers.pop("content-type");ses.headers.pop("origin");ses.headers.update({"referer": "https://m.facebook.com/",})
					response6 = ses.get(windows_referer, cookies=cookies).text
					if "Sukses!" in str(response6):
						ses.headers.update({"sec-fetch-mode": "no-cors","referer": "https://graph.facebook.com/","Host": "graph.facebook.com","accept": "*/*","sec-fetch-dest": "script","sec-fetch-site": "cross-site",})
						response7 = ses.get(status_url, cookies=cookies).text
						token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						return token
		else:
			post = ses.post("https://graph.facebook.com/v18.0/device/login/", data={"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038", "scope": ""}).json()
			code, user_code = post["code"], post["user_code"]
			get = parser(ses.get("https://mbasic.facebook.com/device", cookies=cookies).content, "html.parser")
			form = get.find('form',{'method':'post'})
			post1 = parser(ses.post("https://mbasic.facebook.com"+form["action"], data={"jazoest": re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),"fb_dtsg": re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),"qr": "0","user_code": user_code}, cookies=cookies).content, "html.parser")
			data2 = {}
			form1 = post1.find('form',{'method':'post'})
			for x in form1('input',{'value':True}):
				try:
					if x["name"] == "__CANCEL__" :pass
					else:data2.update({x["name"]:x["value"]})
				except Exception as e:pass
			pos = parser(ses.post("https://mbasic.facebook.com"+form1["action"], data=data2, cookies=cookies).content, "html.parser")
			token = ses.get("https://graph.facebook.com/v18.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038"%(code), cookies=cookies).json()["access_token"]
			return token
	except:pass

def check_info(token, cookies):
	try:
		link = ses.get("https://graph.facebook.com/me?fields=id,name&access_token=%s"%(token), cookies=cookies)
		uid = json.loads(sy.text)["id"]
		nama = json.loads(sy.text)["name"]
		return nama, uid
	except KeyError:
		banner()
		os.system('rm -rf data/.cookie.txt & data/.token.txt')
		print(' %s(%s!%s) Maaf, cookie akun tumbal kamu sudah kadaluarsa'%(P,M,P))
		time.sleep(2);login()
	except requests.exceptions.ConnectionError:
		banner()
		print(' %s(%s!%s) Maaf, koneksi internet anda terputus'%(P,M,P))
		time.sleep(2);login()

def menu():
	try:cookies = {"cookie": open('data/.cookie.txt','r').read()};token = open('data/.token.txt','r').read()
	except IOError:login()
	user = check_info(token, cookies)
	banner()
	print('\n %s(%s+%s) Nama : %s%s'%(P,H,P,H,user[0]))
	print(' %s(%s+%s) Uid  : %s%s'%(P,H,P,H,user[1]))
	print('\n   %s(%s1%s) %sCrack dari teman publik'%(P,H,P,O))
	print('   %s(%s2%s) %sCrack dari teman massal'%(P,H,P,O))
	print('   %s(%s3%s) %sCrack dari total pengikut'%(P,H,P,O))
	print('   %s(%s4%s) %sCrack dari member group'%(P,H,P,O))
	print('   %s(%s5%s) %sCrack dari search name'%(P,H,P,O))
	print('   %s(%s6%s) %sCrack dari sesrch email'%(P,H,P,O))
	print('   %s(%s7%s) %sCheck result crack %sok%s/%scp'%(P,H,P,O,H,P,K))
	print('   %s(%s8%s) %sCheckpoint dectetor %sok%s/%scp'%(P,H,P,O,H,P,K))
	print('   %s(%s9%s) %sInformasi Tools crack facebook'%(P,H,P,O))
	print('   %s(%s0%s) %sExit Tools %s(hapus cookie)'%(P,H,P,O,P))
	pilih()

def pilih():
	menu = input(f' (%) Pilih : {K}')
	if menu in('',' '):
		print(' %s(%s!%s) Pilih asu jangan kosong'%(P,M,P))
		time.sleep(2);menu()
	elif menu in('1','01'):
		print('\n %s(%s+%s) Ketik %s`me` %suntuk crack dari daftar teman sendiri'%(P,H,P,O,P))
		uid = input(f' (%) Masukan username/uid : {K}')
		
menu()