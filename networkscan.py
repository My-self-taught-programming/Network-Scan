import scapy.all as scapy
import pyfiglet

def scan(ip):
	# PAcket Line code is asking usign the ARP request to find the Pdst(IP field/ip address of all answering devices)
	arp_request = scapy.ARP(pdst=ip)
	
	# creates a internet packet and sends it to broadcast mac address(all devices will recieve this)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

	# creates a new pack by combining both preivous packets 
	arp_request_broadcast = broadcast/arp_request
	
	# A list of all asnwered devices and removes additonal infomation (Emission start and packets sent)
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) [0]
	
	# iterating over the answered list to print all answered devices
	print("-- IP Address --------- MAC Address --")
	for i in answered_list:

		# This will print the IP address and the MAC Address of the devices in the answered list

		print(" " + i[1].psrc + "\t\t" + i[1].hwsrc)


banner = pyfiglet.figlet_format(" NETWORK\n SCAN")
while True:
	print(banner)
	print(" With GREAT power comes GREAT responsability!\n")

	user_input = input(" What network do you wish to scan? (e.g 0.0.0.0/?)\n The desired Network:")
	scan(user_input)
