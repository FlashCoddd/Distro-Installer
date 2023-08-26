import os,sys,time

os.system("clear")
updating_packages = "apt update -y"
upgrading_packages = "apt upgrade -y"
time.sleep(2)
os.system("clear")
installing_proot_distro = "apt install proot-distro"
time.sleep(2)
os.system("clear")
print("\t===============UPDATE-UPGRADE===============\n")
os.system(updating_packages)
os.system(upgrading_packages)
os.system("figlet Alpine Linux Installer")
print("\tby irsyad\n\n")
time.sleep(3)
print("\t===============INSTALLING-PROOT===============")
os.system(installing_proot_distro)
print("\t===============INSTALLING-PROOT===============\n")
time.sleep(2)
print("\t===============INSTALLING-ALPINE===============")
os.system("proot-distro install alpine")
print("\t===============INSTALLING-ALPINE===============\n")
time.sleep(2)
os.system("clear")
print("\t===================SUCESS======================\n")
print("\t===================LOGIN=======================\n")
print("\t login or exit ?")
print("\t===================LOGIN=======================\n")
input_y_n = input("Do You Want To Log in? (y/n) = ")
print("\n")
if input_y_n == "y" :
  os.system("proot-distro login alpine")
else:
  os.system("cd ..")
  os.system("python main.py")