print('='*100)
print('')
print ('Digite um número negativo para encerrar o programa')

n = int (input ('Digite um número: ') )
l1 = [] # l de lista
l2 = []
l3 = []
l4 = []
print ('')

while n >= 0 :
    if n in range (0,26) :
        l1.append(n)
    elif n in range (26,51) :
        l2.append(n)
    elif n in range (51,76) :
        l3.append(n)
    elif n in range (76,101) :
        l4.append(n)
    n = int (input ('Digite um número: ') )
    print ('')

print ('')
print ('Houveram {} no intervalo de 0-25, {} no intervalo de 26-50, {} no intervalo de 51-75 e {} no intervalo de 76-100.'. format (len(l1), len(l2), len(l3), len(l4)))
print ('')

print('='*100)

#Edivânia


#== Identificação ==#
print("Aluna: Maria Edivânia\nCurso: Engenharia Elétrica, 2020.2")