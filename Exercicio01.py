#Exercicio01: Número de pessoas na loja

total_pessoas= int(input("Quantas pessoas estão na loja? "))
x = total_pessoas

if x < 5:
    print("Nível Baixo")
elif x >= 5 and x <= 10:
    print("Nível Médio")
elif x >=11 and x < 15:
    print("Nível Elevado")
else:
    print("Extremo")
    
print("Total de pessoas na loja: ", x)        