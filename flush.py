import subprocess
import sys
import os
import pyuac
from pyuac import main_requires_admin
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@main_requires_admin
def main():
    nbtstat_command = 'nbtstat -rr'
    netsh_reset_all = 'netsh int ip reset all'
    netsh_winsock_reset = 'netsh winsock reset'
    try:
        print("ipconfig/release") 
        subprocess.call(["ipconfig", "/release"], shell=True)

        print("ipconfig/renew") 
        subprocess.call(["ipconfig", "/renew"], shell=True)

        print("ipconfig/flushdns") 
        subprocess.call(["ipconfig", "/flushdns"], shell=True)

        print("ipconfig/registerdns") 
        subprocess.call(["ipconfig", "/registerdns"], shell=True) 

        print(nbtstat_command)        
        result_nbt = os.popen(nbtstat_command).read()
        print(result_nbt)

        print(netsh_reset_all)
        resut_netsh_int_ip = os.popen(netsh_reset_all).read()

        print(resut_netsh_int_ip)
        resut_netsh_winsock_reset = os.popen(netsh_winsock_reset).read()
        print(resut_netsh_winsock_reset)

        print("ip local: " + local_ip)
        input("Press enter to close the window. >")
    except Exception:
        print("error")

if __name__ == "__main__":
    main()


