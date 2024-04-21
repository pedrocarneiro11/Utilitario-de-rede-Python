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
    nbtstat_command = r'C:\Windows\Sysnative\nbtstat.exe'
    try:
        # subprocess.call(["ipconfig", "/release"], shell=True) # ok
        # subprocess.call(["ipconfig", "/renew"], shell=True) # ok  
        # subprocess.call(["ipconfig", "/flushdns"], shell=True) # ok  
        # subprocess.call(["ipconfig", "/registerdns"], shell=True) # ok 
        # print(local_ip)        
        # result = os.popen('nbtstat -rr').read() # ok
        # print(result) # ok
        # output, _ = p.communicate() # Erro
        # print(output.decode('utf-8'))
        # subprocess.call(["netsh int ip reset all"], shell=True)
        # subprocess.call(["netsh winsock reset"], shell=True)
        input("Press enter to close the window. >")
    except Exception:
        print("error")

if __name__ == "__main__":
    main()


