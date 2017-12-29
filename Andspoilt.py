#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
      aaaa\                  dd|    ssss| ppppp\    00000\   ii|  ll|   tt|
     aa  aa\    _____        dd|  ss|     pp   pp| 00    00|      ll|   tt|
    aa    aa\  nnnnn \   dd  dd|  ss|     pp   pp|00      00|ii|  ll| ttt|ttt
   aa$$$$$$aa| nn   nn|dd    dd|   sssss\ pp pp/  00      00|ii|  ll|   tt|
   aa      aa| nn   nn|dd    dd|       ss|pp|      00    00| ii|  ll|   tt|
   aa      aa| nn   nn|dd____dd|  ssssss/ pp|        0000/   ii|  ll|    ttt

            [**********]Android Exploit Toolkit[*********]
              [***]Developed by Sunday Joel Philemon[***]
               [**]Mail: philemonsunday202@gmail.com[**]


		''')
		def inicio1():
			while True:
				print ('''
1) Create Android apk payload
2) Start exploit
3) Update Andspoilt
4) Credits and About
5) Help
6) Exit Andspoilt

			''')

				opcion0 = raw_input("\033[1;36muse > \033[1;m")

				while opcion0 == "1":
					print ('''''')
