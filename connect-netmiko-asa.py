#
# Créer un fichier paramètre "connect-asa.txt" contenant par ligne, l'ip, user, pass et les commandes à passer séparées par une virgule
# exemple :
# 192.168.153.254,cisco,cisco,show ver | inc Serial Number,show interface | inc GigabitEthernet
# 192.168.153.252,admin,password,name 1.1.1.1 test1,name 2.2.2.2 test2,show name,wr mem
#
# un fichier "result-asa.txt" collecte les résultats des commandes passées
#
from netmiko import ConnectHandler
import sys
import csv
       
devices=[]
file = open('result-asa.txt', "w")
with open ('connect-asa.txt') as csvfile:
	devices = csv.reader(csvfile, delimiter=',')
	for row in devices:
		cisco_asa = {
		'device_type': 'cisco_asa',
		'ip': row[0],
		'username': row[1],
		'password': row[2]
		} 
		net_connect = ConnectHandler(**cisco_asa)
		net_connect.find_prompt()
		print(row)
		max=str(row).count(',')
		i = 3
		while i <= max :
			output = net_connect.send_config_set(row[i])
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
