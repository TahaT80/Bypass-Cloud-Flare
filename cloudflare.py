"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN
        creat by Amir Hossein Tadas & TAHA
"""
import os
import socket
import sys
import time
from colorama import Fore
def __start__():

    print(Fore.RED+"\n [!] Plase Enter The Target Website Address")
    print(Fore.RED+"\n [!] for exampel : test.com\n")
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost','news','resources','insights','articles', 'local','landing', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+">> ")
    if site == "":
        try:
            print(Fore.RED+" [!] "+Fore.BLUE+"Please Enter Address :) \n")
            time.sleep(5)
            sys.exit()
        except:
            return
    for sub in subdom:
        time.sleep(5)
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (Fore.BLUE+" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            print (Fore.RED+" [!] NOT FIND " + str(bypass) + ' | ' + str(hosts))

    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()

if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()