#Module completed on Tue Apr 17 at 00:30
import os, re, json
import time, subprocess
from urllib2 import urlopen

def locate():
	try:
		os.system("clear; tset")
		print("""[**]This query's phone location from it's Ip or Mac address[**]\n\033[3;33mDisclaimer: Not very accurate\033[1;m\n\n1.) Mac address\n2.) Ip address""")
		print("*" * 18)
		addr = raw_input("> ")
		while addr == "":
			addr = raw_input("> ")
		if addr == "1":
			mac_addr = raw_input("Input MAC address: ")
			if mac_addr == '':
				pass
			else:
				print("User Location :)")
				subprocess.Popen('ruby /usr/share/metasploit-framework/tools/recon/ad_support.rb ' + mac_addr, shell=True).wait()
				#raw_input("Press Enter to continue")
		if addr == "2":
			ip_addr = raw_input("Input Ip address: ")
		if addr == "back":
			pass
		else:
			print("No data")
			time.sleep(2)
			
		#Declaring variables
		url = 'http://ipinfo.io/json'
		data = json.load(response)

		IP=data['ip']
		response = urlopen(url)
		org=data['org']
		city = data['city']
		country=data['country']
		region=data['region']
		
		print "Your Details: "
		print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nISP : {0}'.format(org,region,country,city,IP)
		
	except Exception:
		print("No internet connection\nPress a key to continue")
		raw_input()
