# -*- coding: utf-8 -*-
import random
banner1 ="""\033[1;29m
 ████   ███  ██ ████   ███  █▀▀▀█   ████    ██  ██   ██████
██  ██  ██ █ ██ █   █ █   ▀ █   █ ██    ██  ██  ██     ██
██████  ██  ███ █   █  ███  █▀▀▀▀ ██ ▀▀ ██  ██  ██     ██
██  ██  ██   ██ ████     █  █       ████    ██  █████  ██
     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   
\033[1;m"""
banner2 = """
            █████████████████████████████████████████████████████\033[1;34m
            ███████████████████████  ████████████████████████████\033[1;35m
            ██████████████████████ ██ ███████████████████████████\033[1;36m
            █████████████████████ ████ ██████████████████████████\033[1;37m
            █████████████████████      ██████████████████████████\033[1;38m
            █████████████████████ ████ ██████████████████████████\033[1;39m
            ████████████Android Exploit Toolkit██████████████████\033[1;33m
            █████████████████████████████████████████████████████\033[1;32m
\033[1;m"""
banner3 = """\033[1;31m

      aaaa\                  dd|    ssss| ppppp\    00000\   ii|  ll|   tt|
     aa  aa\    _____        dd|  ss|     pp   pp| 00    00|      ll|   tt|
    aa    aa\   nnnnn\   dd  dd|  ss|     pp   pp|00      00|ii|  ll| ttt|ttt \033[1;32m
   aa$$$$$$aa| nn   nn|dd    dd|   sssss\ pp pp/  00      00|ii|  ll|   tt|
   aa      aa| nn   nn|dd    dd|       ss|pp|      00    00| ii|  ll|   tt|
   aa      aa| nn   nn|dd____dd|  ssssss/ pp|        0000/   ii|  ll|    ttt

            [**********]Android Exploit Toolkit[*********] \033[1;36m
              [***]Developed by Sunday Joel Philemon[***]
               [**]Mail: philemonsunday202@gmail.com[**]

\033[1;m"""

banner4 = """
        \033[1;37m▒▒████  ▒███ ▒██▒████   ███ ▒█▀▀▀█  ▒████   ▒██ ▒██  ▒██████\033[1;m
        ▒\033[1;33m██  ██ ▒██▒█▒██▒█  ▒█▒█   ▀▒█  ▒█ ██   ▒██ ▒██ ▒██    ▒██\033[1;m
        \033[1;36m▒██████ ▒██ ▒███▒█  ▒█ ▒███ ▒█▀▀▀▀ ██ ▀▀▒██ ▒██ ▒██    ▒██\033[1;m
        ▒\033[1;33m██  ██ ▒██  ▒██▒████    ▒█ ▒█      ▒████   ▒██ ▒█████ ▒██
            ▒▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
\033[1;m
             [**********]Android Exploit Toolkit[*********] \033[1;36m
            [***]Developed by Sunday Joel Philemon[***]
             [**]Mail: philemonsunday202@gmail.com[**]
 \033[1;m                       
"""
banner5 = """
    \033[1;31m                       ..'''..              
                     .:d0NMMMMMMMMMXOo,         
                   :0WMMMMMMMMMMMMMMMMMWk,      ✨
                 cNMMMMMMWWNNNNNNNWWMMMMMMK,   
               .KMMMMMMWWNXc\033[1;m:::::\033[1;31mcXNWWMMMMMMk   
              ,WMMMMMMWWNXc\033[1;m ..... \033[1;31mcXNWWMMMMMMK. 
             .NMMMMMMMWNXx\033[1;m.........\033[1;31mxXNWMMMMMMMk 
             dMMMMMMMWNXO\033[1;m.....\033[1;31mo\033[1;m.....\033[1;31mOXNWMMMMMMM'
             KMMMMMMWNX0'\033[1;m... \033[1;31mlOl\033[1;m ...'\033[1;31m0XNWMMMMMMl
             XMMMMMWWNK;\033[1;m .. :\033[1;31mOOO\033[1;m: .. ;\033[1;31mKNWWMMMMMo
             xMMMMWWNXl\033[1;m ....;:::;.... \033[1;31mlXNWWMMMM,
             .WMMMWNXk\033[1;m.................\033[1;31mkXNWMMMK 
              cMMWNX0\033[1;m.... :\033[1;31modddddoc\033[1;m ....\033[1;31m0XNWMN. 
               cWWNX,\033[1;m  . ;\033[1;31mKXNNNNNXK\033[1;m; .  ,\033[1;31mXNWK.  
                .kWNKKKKKXNWWWMWWWNXKKKKKNNo.   
                  .xNWWWWWWMMMMMMMWWWWWWKo.     
                    .;xKWMMMMMMMMMMMN0o,.       
                        .';clooolc,.  .         
                Just created a dent in your screen .      .                                    .      .   \033[1;m     
          [**********]Android Exploit Toolkit[*********] \033[1;36m
            [***]Developed by Sunday Joel Philemon[***]
             [**]Mail: philemonsunday202@gmail.com[**]\033[1;m
"""
stream = (banner1, banner2, banner3, banner4, banner5)
def banner():
	print random.choice(stream)
	
def about():
	#print banner4
	print("""
						\033[1;31m
			[***]ABOUT[***]\033[1;m
			
\033[1;35m
    Andspoilt  Copyright (C) 2017  Philemon Sunday Joel
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    
Andspoilt V 1.1 is designed exploit Android Devices
It utilises Metaspoilt and other tools in a simple interactive User Interface

\033[1;31m                       [***]CREDITS[***]\033[1;m
\033[1;35m           
                    * Shalleen Baraka Happuch
                       * Lance Ezra Juma
						
\033[1;m""")
def help():
	print("""\033[1;31m                   [**]Report Bugs and ask questions[**]:\033[1;m
	                \033[1;35mphilemonsunday202@gmail.com
	                pythonofhades@programmer.net\033[1;m""")

def warranty():
	print("""\033[1;29m
  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\033[1;m""")

def copyright():
	print("""\033[1;29m
    Copyright (C)  2017    Philemon Sunday Joel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
\033[1;m
""")
