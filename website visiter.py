import webbrowser
from time import sleep
import os


os.system("sudo anonsurf start")
sleep(5)
loop = 'loop'
while loop == 'loop':
 import os
 os.system("sudo anonsurf restart")

 sleep(5)
 driver = webbrowser.open('www.dnsleaktest.com', new=0)
 sleep(10)    
 os.system("killall -9 'chrome'")


