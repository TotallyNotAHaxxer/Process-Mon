import psutil
import time as t # somehow the datetime fucks it up ``
from datetime import datetime
from subprocess import call
from prettytable import PrettyTable
import fcntl
import socket
import struct
from getmac import get_mac_address


#TODO => Add Date and time 

def CFMMAIN():
    cpufreq = psutil.cpu_freq()
    print("CPU USAGE PER CORE")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"")

def CFM():
    cpufreq = psutil.cpu_freq()
    CPIFF = PrettyTable(['CPU USAGE PER CORE'])
    cpfi = psutil.cpu_percent(percpu=True, interval=1)
    CPIFF.add_row([
        cpfi
    ])
    print(cpfi)

def time():
    date_table = PrettyTable(['Date/Time Running/boot'])
    Datenow = str(datetime.now())
    date_table.add_row([Datenow])
    print(date_table)



def cpuinf():
    import psutil 
    cpufreq = psutil.cpu_freq()
    ccore = psutil.cpu_count(logical=False)
    clcore = psutil.cpu_count(logical=True)
    cpuinf = PrettyTable(["CPU Cores", "Total", "Frequency"])
    freqcc = f' {cpufreq.current:.2f}'
    cpuinf.add_row([
        ccore,
        clcore,
        freqcc
    ])
    print(cpuinf)

def tab_macPT2():
    I_mac = get_mac_address(interface="eth1")
    eth_mac = get_mac_address(interface="docker0")
    eth2_mac = get_mac_address(interface="vmnet8")
    eth1_mac = get_mac_address(interface="vmnet1")
    Ii_mac = get_mac_address(interface="eth0")
    eth11_mac = get_mac_address(interface="wlan0")
    eth21_mac = get_mac_address(interface="wlan2")
    eth91_mac = get_mac_address(interface="wlan1")
    eth911_mac = get_mac_address(interface="lo")
    Mac_table = PrettyTable(["Mac Addresses Tied To Interface"])
    Mac_table.add_row([I_mac])
    Mac_table.add_row([eth_mac])
    Mac_table.add_row([eth2_mac])
    Mac_table.add_row([eth1_mac])
    Mac_table.add_row([Ii_mac])
    Mac_table.add_row([eth11_mac])
    Mac_table.add_row([eth21_mac])
    Mac_table.add_row([eth91_mac])
    Mac_table.add_row([eth911_mac])
    print(Mac_table)    


def arp():
    from getmac import getmac
    getmac.PORT = 55555
    IPNET = getmac.get_mac_address(ip="10.0.0.1", network_request=True)
    tab = PrettyTable(['Network Mac'])
    tab.add_row([IPNET])
    print(tab)


def tab_uname():
    import platform 
    uname = platform.uname()
    uname_table = PrettyTable(['Platform information'])
    uname_table.add_row([
        uname.node,
    ])
    uname_table.add_row([
        uname.system,
    ])
    uname_table.add_row([
        uname.release,
    ])
    uname_table.add_row([
        uname.machine,
    ])
    print(uname_table)


def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])


def main():
    A = getHwAddr('eth0')
    B = getHwAddr('docker0')
    C = getHwAddr('wlan0')
    D = getHwAddr('wlan2')
    E = getHwAddr('wlan1')
    F = getHwAddr('eth1')
    G = getHwAddr('vmnet1')
    H = getHwAddr('vmnet8')
    table_mac2 = PrettyTable(['Macs In Range'])
    table_mac2.add_row([A, B, C, D, E, F, G, H])
    print(table_mac2)
    #TODO => FI~X THISSSS


def mac_sesh():
    import netifaces
    A = netifaces.interfaces()
    B = netifaces.ifaddresses('eth0')[netifaces.AF_LINK]
    print(B)


def main_main():
    while True:
        call("clear")
        table = PrettyTable(['Network', 'Status', 'Speed'])
        for key in psutil.net_if_stats().keys():
            name = key
            up = "Up" if psutil.net_if_stats()[key].isup else "Down"
            speed = psutil.net_if_stats()[key].speed
            table.add_row([name, up, speed])
        print(table)
        memory_table = PrettyTable(["Total", "Used", "Available", "Percentage"])
        vm = psutil.virtual_memory()
        memory_table.add_row([
            vm.total,
            vm.used,
            vm.available,
            vm.percent
        ])
        print(memory_table)
        process_table = PrettyTable(['PID', 'PNAME', 'STATUS',
                                    'CPU', 'NUM THREADS'])
        
        for process in psutil.pids()[-10:]:
            try:
                p = psutil.Process(process)
                process_table.add_row([
                    str(process),
                    p.name(),
                    p.status(),
                    str(p.cpu_percent())+"%",
                    p.num_threads()
                    ])
                
            except Exception as e:
                pass
        print(process_table)
        tab_uname()
        tab_macPT2()
        cpuinf()
        t.sleep(1)

if __name__ == "__main__":
    main_main()




# items and tests that ruined the entire script or didnt fit within tabulates data struct 

#tabuname
#main
#mac_shesh
#tab_macPT2
#CPUINFO
#ARP
