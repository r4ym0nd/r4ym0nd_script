import os

token = True
while (token):
    
    #os.system('clear')

    banner  = " __________________________________________________\n"
    banner += "||       _  _                    ___            _ ||\n"
    banner += "||      | || |                  / _ \          | |||\n"
    banner += "||  _ __| || |_ _   _ _ __ ___ | | | |_ __   __| |||\n"
    banner += "|| | '__|__   _| | | | '_ ` _ \| | | | '_ \ / _` |||\n"
    banner += "|| | |     | | | |_| | | | | | | |_| | | | | (_| |||\n"
    banner += "|| |_|     |_|  \__, |_| |_| |_|\___/|_| |_|\__,_|||\n"
    banner += "||               __/ |                            ||\n"
    banner += "||              |___/                             ||\n"  
    banner += "||   My facebook: www.facebook.com/               ||\n"
    banner += "||   My youtube channel: www.youtube.com/         ||\n"
    banner += "||____________r4ym0nd_Script_v0.1_beta____________||\n"
    print banner
    
    print 'Wellcome to r4ymond script v0.1\n'
    print '########################################################\n'
    print '1)Config kali network connection (kali: 192.168.137.3)\n'
    print '2)Fix defualt repositoriy\n'
    print '3)update,upgrade and distupgrade kali\n'
    print '4)Install Ddos Script version 3.0\n'
    print '99)Exit program\n'
    print '#? '

#===================Config kali network connection==================
    def config_kali_networking():
        print 'setting dns server to 8.8.8.8\n'
        print 'writing in resolv.conf\n'
        file_object = open("/etc/resolv.conf","w")
        file_object.write("nameserver 4.2.2.4\n")
        file_object.close()
        print 'Done!!!'
        print 'setting eth0 address to 192.168.137.3\n'
        print 'writing in interfaces\n'
        file_object = open("/etc/network/interfaces","w")
        file_object.write('''
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

auto eth0
iface eth0 inet static
address 192.168.137.3
network 192.168.137.0
netmask 255.255.255.0
broadcast 192.168.137.255
gateway 192.168.137.1

# The loopback network interface
auto lo
iface lo inet loopback''')
        file_object.close()
        os.system('service networking restart')
        os.system('service network-manager restart')
        os.system('ifconfig eth0 down')
        os.system('ifconfig eth0 up')
        print 'Done!!!'
        
        return 0

#===================update_kali==================================
    def update_kali():
        print 'updating kali'
        os.system('apt-get clean')
        os.system('apt-get update')
        os.system('apt-get upgrade')
        os.system('apt-get dist-upgrade')
        os.system('apt-get autoclean')
        os.system('apt-get autoremove')
        return 0

#===================fix defualt repositoriy=======================
    def defualt_repositoriy():
        print 'Fixing defualt repositories for kali:\n'
        file_object = open("/etc/apt/sources.list","w")
        file_object.write('''
# 

# deb cdrom:[Debian GNU/Linux 2.0 _Sana_ - Official Snapshot amd64 LIVE/INSTALL Binary 20150811-08:02]/ sana contrib main non-free

#deb cdrom:[Debian GNU/Linux 2.0 _Sana_ - Official Snapshot amd64 LIVE/INSTALL Binary 20150811-08:02]/ sana contrib main non-free

#deb http://security.kali.org/kali-security/ sana/updates main contrib non-free
#deb-src http://security.kali.org/kali-security/ sana/updates main contrib non-free

# Regular repositories
deb http://http.kali.org/kali sana main non-free contrib
deb http://security.kali.org/kali-security sana/updates main contrib non-free
# Source repositories
deb-src http://http.kali.org/kali sana main non-free contrib
deb-src http://security.kali.org/kali-security sana/updates main contrib non-free''')
        file_object.close()
        print 'Done!!!'
        return 0
#===================ddos_script===================================
    def ddos_script():
        print 'this section is under construction\n'
        input()
        return 0
#===================terminal_main_script==========================
    option = input()
    if option == 1:
        r = config_kali_networking()    
    elif option == 2:
        r = defualt_repositoriy()
    elif option == 3:
        r = update_kali()
    elif option == 4:
        r = ddos_script()
    elif option == 99:
        break
    else:
        print 'invalid input! put a valid number.'




        
        
        
