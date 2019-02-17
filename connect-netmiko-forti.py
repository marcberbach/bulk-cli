#
# Créer un fichier paramètre "connect-forti.txt" contenant par ligne, l'ip, user, pass et les commandes à passer séparées par une virgule
# exemple :
# 192.168.153.254,admin,fortinet,conf vdom,edit root,get antivirus settings
# 192.168.153.252,admin,fortinet,get system status
#
# un fichier "result-forti.txt" collecte les résultats des commandes passées
#
from netmiko import ConnectHandler
import sys
import csv
       
devices=[]
file = open('result-forti.txt', "w")
with open ('connect-forti.txt') as csvfile:
	devices = csv.reader(csvfile, delimiter=',')
	for row in devices:
		device = {
		'device_type': 'fortinet',
		'ip': row[0],
		'username': row[1],
		'password': row[2]
		} 
		net_connect = ConnectHandler(**device)
		net_connect.find_prompt()
		print(row)
		max=str(row).count(',')
		i = 3
		while i <= max :
			output = net_connect.send_command_timing(row[i])
			print ('device: ' + row[0] + '  commande : ' + row[i])
			file.write('=====================================================================================================\r\n')
			file.write('device: ' + row[0])
			file.write('\r\n')
			file.write('commande : ' + row[i]) 
			file.write('\r\n')		
			file.write('=====================================================================================================\r\n')
			file.write(output)
			i += 1
file.close()
