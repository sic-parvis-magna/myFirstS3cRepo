#!/bin/python3

#a) Utilizando listas e um ciclo for, escreva código que guarde numa lista o endereço IP dos primeiros 50 dispositivos numa rede. No fim, imprima a lista de IPs
import ipaddress
lista_IP=[]
    
ip_inicial = ipaddress.IPv4Address('192.168.68.0')
ip_final = ipaddress.IPv4Address('192.168.68.50')

for ip_int in range(int(ip_inicial), int(ip_final)):
    print(ipaddress.IPv4Address(ip_int))

#b)

lista_IP = open("Lista IPs", 'w') 
lista_IP.write('/n')
lista_IP.close()