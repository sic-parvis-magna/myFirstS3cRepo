#!/bin/python3
#coding: utf-8

#a) Usando o módulo glob do Python, escreva código para listar todos os ficheiros de um directório.
import glob
ficheiros=[]

for x in glob.glob("*"):
    ficheiros.append(x)
    print(x)

#b) Altere o código para listar apenas ficheiros com a extensão .py(Python)
print("________________________________________________________________")

for py in glob.glob("*.py"):
    ficheiros.append(py)
    print(py)
    
#C) Altere o código para gravar o output num ficheiro de texto, para além de a imprimir no terminal.

file = open("Output Desafio_1.txt", "w")
for y in ficheiros:
    print(y)
    file.writelines(y + "\n")
    
file.close()

