#!/bin/python3

#a) Escreva código que, utilizando o módulo ipadress, imprima todos os endereços IP de uma rede com o prefixo 192.168.3.x

import ipaddress
IPs=[]

for ip in ipaddress.IPv4Network('192.168.3.0/24'):
    print(f'{ip}')


print("__________________________________________________________")
#b) O módulo os do Python permite executar funções que estejam dependentes do sistema operativo. Utilizando esse módulo e o módulo ipaddress, escreva código para executar
#um ping a toda a sua rede doméstica  
import os
total=0
online=0

for host in ipaddress.IPv4Network('192.168.56.0/24'):
  response = os.system("ping -c 1 " + str(host) + " > /dev/null 2>&1")
  if response == 0:
    print (str(host)+ " está online!")
    online=online+1
    total=total+1
  else:
    print (str(host)+ " está offline!")
    total=total+1
print("Estão " + str(online) + " dispostivos online, que representam " +str(online/total*100) + "% do total de dispositivos analisados.")


print("____________________________________________________________")
 #c) Adicione agora uma linha de código para que, no início da execução do programa, seja mostrado o nome de utilizador atualmente com sessão iniciada. Esta funcionalidade
 # é possível através do módulo os.

username = os.getenv('LOGNAME')
print(username)


print("____________________________________________________________")
#d) O MAC Adress de um dispostivo é o identificador único da placa de rede com que este se encontra ligado. Utilize agora o módulo adicional 
# get-mac (https://pypi.org/project/get-mac/), desenvolvido pelo MIT, para obter e imprimir o MAC Adress dos dispositivos que estejam online.

from getmac import get_mac_address

for host in ipaddress.IPv4Network('192.168.56.0/24'):
    response = os.system("ping -c 1 " + str(host) + " > /dev/null 2>&1")
  if response == 0:
    print (str(host)+ " está online!" + get_mac_address(ip=host))
    online=online+1
    total=total+1
    