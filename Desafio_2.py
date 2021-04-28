#!/bin/python3

#a) Utilizando listas e um ciclo for, escreva código que guarde numa lista o endereço IP dos primeiros 50 dispositivos numa rede. No fim, imprima a lista de IPs
import ipaddress
lista_IP=[]
    
ip_inicial = ipaddress.IPv4Address('192.168.68.0')
ip_final = ipaddress.IPv4Address('192.168.68.50')

for ip_int in range(int(ip_inicial), int(ip_final)):
    print(ipaddress.IPv4Address(ip_int))

#b)Escreva agora uma função para imprimir um IP por linha. Para o efeito, utilize um ciclo for. A lista deverá receber a variável a variável ListaIPs como input.
print("__________________________________________________________________")

Lista_IPs=input("ListaIPs: ")

ips=Lista_IPs.split('.')
lista=open('ListaIPs.txt', 'w')

for x in range(0,256):
    print(ips[0] + "." + ips[1] + "." + ips[2] + "." + str(x))
    lista.write(ips[0] + "." + ips[1] + "." + ips[2] + "." + str(x) + '\n')
    
lista.close()