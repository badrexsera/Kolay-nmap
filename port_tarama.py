import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KOLAY NMAP KULLANIMI ")

print("""

─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
█░░░█░░░░░░░░░░▄▄░██░█
█░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█
█░░░▀░░░▄▄▄▄▄░░██░▀▀░█
─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀

1]Port tarama
2]Servis Ve Versiyon Tarama
3]Isletim Sistemi Tarama
4]Detayli Tarama
5]DNS Çözümlemesi -n
6]Daha hizli tarama
7]Sadece açik Portlar
8] Bir IP üzerinde bulunmasi muhteme 65535 portunu tarar.
9] Port tarama .

""")
islemno = input("Islem Numarasi Giriniz : ")

if(islemno=="1"):
         hedefip = input("Hedef IP Giriniz : ")
         os.system("nmap " + hedefip)
elif(islemno=="2"):
         hedefip = input("Hedef IP Giriniz : ")
         os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
         hedefip = input("Hedef IP Giriniz : ")
         os.system("nmap -o " + hedefip)
elif(islemno=="4"):
         hedefip = input("Hede IP Giriniz : ")
         os.system("nmap -A -sS -sV -vv -p- " + hedefip)
elif(islemno=="5"):
         hedefip = input("Hede IP Giriniz : ")
         os.system("nmap -n " + hedefip)
elif(islemno=="6"):
         hedefip = input("Hede IP Giriniz : ")
         os.system("nmap -F " + hedefip)
elif(islemno=="7"):
         hedefip = input("Hede IP Giriniz : ")
         os.system("nmap --open " + hedefip)
elif(islemno=="8"):
         hedefip = input("Hede IP Giriniz : ")
         os.system("nmap -p- " + hedefip)
elif(islemno=="9"):
	port = input("Bir Port Belirleyiniz : ")
	hedefip = input("Hede IP Giriniz : ")
	os.system("nmap " + hedefip + " -p " + port)





else:
	print("Oyle Bir Secenek Bulunmamaktadir.")








