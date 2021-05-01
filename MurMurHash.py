import mmh3
import requests
import codecs
import os, sys
#from shodan import Shodan
#import json

def logo():
	banner = '''
___  ___          ___  ___           _   _           _     
|  \/  |          |  \/  |          | | | |         | |    
| .  . |_   _ _ __| .  . |_   _ _ __| |_| | __ _ ___| |__  
| |\/| | | | | '__| |\/| | | | | '__|  _  |/ _` / __| '_ \ 
| |  | | |_| | |  | |  | | |_| | |  | | | | (_| \__ \ | | |
\_|  |_/\__,_|_|  \_|  |_/\__,_|_|  \_| |_/\__,_|___/_| |_|
Author: Viral Maniar
Twitter: @ManiarViral
Org: Preemptive Cyber Security Pty Ltd
Description: This tool is to calculate a MurmurHash value of 
a favicon to hunt phishing website on Shodan.
 '''
	return banner
	
def cmd_HashGenerator():
	
	URL = input('\nEnter Favicon URL to generate Hash:')
	response = requests.get(URL)
	#response = requests.get(URL, verify=False)
	favicon = codecs.encode(response.content,"base64")
	print('\n')
	hash = mmh3.hash(favicon)
	print('----------')
	print(hash)
	print('----------')
	print('\n')
	print('Tip: Use http.favicon.hash:<hash> on Shodan to hunt phishing sites.')
	
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? y/n\n> ')).lower()
			if choice[0] == 'y':
				return cmd_HashGenerator()
			if choice[0] == 'n':
				sys.exit(0)
				break
			else:
				print('Invalid Input')
		except KeyboardInterrupt:
			print ('[!] Ctrl + C detected\n[!] Exiting')
			sys.exit(0)
		except EOFError:
			print ('[!] Ctrl + D detected\n[!] Exiting')
			sys.exit(0)

def main():
	print (logo())
	cmd_HashGenerator()
	
if __name__ == "__main__":
	main()	