# import code needed for our script
from napalm import get_network_driver
from pprint import pprint as pp
import sys

# import the driver via napalm
driver = get_network_driver('eos')

# set our variables from arguments passed
myip = (sys.argv[1])
user = (sys.argv[2])
password = (sys.argv[3])

# add the creds to the device attribute
device = driver(myip, user, password) # This password could easily be a private-key
device.open()
facts = device.get_facts()

# return facts to the user
print(facts)
