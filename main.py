import os,sys,time

os.system("clear")
print("\n\t===========================================================")
print("\t\t\t\t\b\b\b\bDistroInstaller v0.3\n")
print("\t Author       = Ahmad Ali Alirsyadi")
print("\t Jenis Script = Script Linux Distro Installer")
print("\t Fungsi       = Dapat Menginstall Distro via Proot")
print("\t Distro List  = ubuntu,arch,debian,manjaro,fedora,opensuse.")
print("\t Distro List  = pardus,alpine,void.\n")
print("\t\t\t\t*copyright 2023-NoLimit by irsyad'\n")
print("\t===========================================================\n")
print("\tAnda Ingin Menginstall Distro Jenis apa?")
print("\tSilahkan Pilih Salah Satu dari yang diatas\n")
wich_one_distrolist = input("\tDistro Jenis Ini! = ")


if wich_one_distrolist == "arch":
  os.system("python arch.py")
elif wich_one_distrolist == "debian":
  os.system("python debian.py")
elif wich_one_distrolist == "ubuntu":
  os.system("python ubuntu.py")
elif wich_one_distrolist == "manjaro":
  os.system("python manjaro.py")
elif wich_one_distrolist == "pardus" :
  os.system("python pardus.py")
elif wich_one_distrolist == "alpine" :
  os.system("python alpine.py")
elif wich_one_distrolist == "fedora" :
  os.system("python fedora.py")
elif wich_one_distrolist == "opensuse" :
  os.system("python opensuse.py")
else:
  print("\n\tMaaf Distro Yang kamu maksud tidak ada :(")
  sys.exit(1)