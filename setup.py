#! /usr/bin/python
# coding=utf-8
#
#
# Python installer
#
#
import sys
import os
import subprocess
import platform
import time
from src import banner

if platform.system() == 'Linux':
	installer = False
	#Request root Permission
	if os.getuid() != 0:
		os.system("resize -s 7 47 > /dev/null")
		print("To complete installation Please run as root")
		time.sleep(2)
		exit()

	try:
		if sys.argv[1] == 'install':
			installer = True
	except IndexError:
		os.system("resize -s 26 64 > /dev/null")
		print banner.banner5
		print("""
		\033[1;31m[***]\033[1;32mAndspoilt Installer\033[1;31m[***]\033[1;m
	  \033[1;31m[**]\033[1;35mUse Agument \033[1;33m'install'\033[1;35m to install\033[1;31m[**]""")
		raw_input()
		print("\033[1;m Id est: [\033[1;31mroot@" + platform.node() +"\033[1;m] $ ./setup.py install")
		sys.exit()

	#initialise Process
	if installer is True:
		#Check if path already exists
		if os.path.isdir('/usr/share/andspoilt'):
			print("""
			\033[1;31m[***]\033[1;32mAndspoilt Installer\033[1;31m[***]\033[1;m
	           It seems Andspoilt is already installed""")
			time.sleep(2)
			remove = raw_input("""\033[1;31mDo you wish to clean Install? (y/n)
			\033[1;30mDefault \033[1;31m'yes'\033[1;m""")
			if remove == 'no' or remove == 'n':
				sys.exit()
			else:
				os.system('rm -rf /usr/share/andspoilt')
		os.system("clear")
		print("\033[1;31m\n[***]\033[1;32mAndspoilt Installer\033[1;31m[***]\033[1;m\n" + ""*8 + "Installing.......")
        cwdpath = os.getcwd()
        subprocess.Popen("cd ..;cp -rf %s /usr/share/andspoilt" % cwdpath, shell=True).wait()
        subprocess.Popen("echo #!/bin/bash > /usr/bin/andspoilt", shell=True).wait()
        subprocess.Popen("echo cd /usr/share/andspoilt >> /usr/bin/andspoilt", shell=True).wait()
        subprocess.Popen("echo exec python2 andspoilt $@ >> /usr/bin/andspoilt", shell=True).wait()
        subprocess.Popen("chmod +x /usr/bin/andspoilt", shell=True).wait()
        subprocess.Popen("chmod +x %s/src/run.sh" % cwdpath, shell=True).wait()
        subprocess.Popen("cp %s/src/ad_support.rb /usr/share/metasploit-framework/tools/recon/ad_support.rb" % cwdpath, shell=True).wait()
        subprocess.Popen("chmod +x /usr/share/metasploit-framework/tools/recon/ad_support.rb", shell=True).wait()
        subprocess.Popen("%s/src/run.sh" % cwdpath, shell=True).wait()
        time.sleep(2)
        os.system("clear")
        print ("\033[1;31m                  [**]\033[1;33mFinished installing\033[1;31m[**]")
        print ("\033[1;37mUsage :\033[1;m")
        time.sleep(1)
        print(" [\033[1;31mroot@" + platform.node() +"\033[1;m]─[\033[1;34m" + os.getcwd() + "\033[1;m] $ andspoilt")
        print("""\n\n\n\n\n""")
        
if platform.system() not in  ["Linux", "Darwin"]:
	print("Andspoilt is not designed for " + platform.system())
