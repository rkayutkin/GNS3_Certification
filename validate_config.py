import sys
import napalm
    
if len(sys.argv) != 5:
   print("You supplied ", len(sys.argv)-1, " arguments but 4 are needed")
   print("validate_config.py requires: OS, IP, USER and PW of device")
   print("example: python3  validate_config.py  eos  a.b.c.d  username  password)"
   sys.exit()
os = sys.argv[1]
ip = sys.argv[2]
user = sys.argv[3]
passwd = sys.argv[4]
from napalm import get_network_driver
from pprint import pprint as pp
driver = get_network_driver('eos')
device = driver('172.16.2.10', 'admin', 'alta3')
device.open()
pp.pprint(device.compliance_report("/home/student/file.yml"))
