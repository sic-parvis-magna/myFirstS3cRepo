#!/bin/python3

#a) Usando o módulo glob do Python, escreva código para listar todos os ficheiros de um directório.
import glob
ficheiros=[]

for x in glob.glob("/home"):
    ficheiros.append(x)
    break
print(ficheiros)

#b) Altere o código para listar apenas ficheiros com a extensão .py(Python)
import glob
ficheiros=[]

for py in glob.glob("*.py"):
    ficheiros.append(py)
    print(ficheiros)
    
#C) Altere o código para gravar o output num ficheiro de texto, para além de a imprimir no terminal.
import sys
sys.stdout = open('Output Desafio_1', 'w')
print('ficheiros')
sys.stdout.close()
