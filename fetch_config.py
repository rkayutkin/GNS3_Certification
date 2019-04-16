import sys
import napalm
    
if len(sys.argv) != 5:
   print("You supplied ", len(sys.argv)-1, " arguments but 4 are needed")
   print("fetch_config.py requires: OS, IP, USER and PW of device")
   print("example: python3  fetch_config.py  eos  a.b.c.d  username  password)"
   sys.exit()
os = sys.argv[1]
ip = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]
from napalm import get_network_driver
import pprint as pp
driver = get_network_driver('eos')
device = driver('172.16.2.10', 'admin', 'alta3')
device.open()
device.get_facts()
pp.pprint(device.get_interfaces())
config = device.get_config()
running_config = config['running']
print(running_config)
path = "/home/student/sw1.conf"
sw1_conf_file = open(path, "w")
sw1_conf_file.write(running_config)
sw1_conf_file.close()
