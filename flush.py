import subprocess
import sys
import os
import pyuac
from pyuac import main_requires_admin

@main_requires_admin
def main():
    try:
        # subprocess.call(["ipconfig", "/release"], shell=True) # ok
        # subprocess.call(["ipconfig", "/renew"], shell=True) # ok  
        # subprocess.call(["ipconfig", "/flushdns"], shell=True) # ok  
        subprocess.call(["ipconfig", "/registerdns"], shell=True)
        # subprocess.call(["ipconfig", "/nbtstat -rr"], shell=True)
        # subprocess.call(["ipconfig", "/netsh int ip reset all"], shell=True)
        # subprocess.call(["ipconfig", "/netsh winsock reset"], shell=True)
        input("Press enter to close the window. >")
    except Exception:
        print("error")

if __name__ == "__main__":
    main()


