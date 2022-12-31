from random import randint

# CABEÇALHO #
print ('')
print ('='*70)
print ('')
print ('JOGOS DA MEGA CENA'.center (70))
print ('')


jogada = []
jogadas_gerais = []
cont = 0

# CÓDIGO PRINCIPAL #
while True : 

        b1 = randint (1, 20) # sorteio números
        b2 = randint (1, 20)
        b3 = randint (1, 20)

        if b1 != b2 and b1 != b3 and b2 != b3 : # garante que os números sorteados sejam diferentes entre si
                jogada.append (b1) # colocação numa lista
                jogada.append (b2)
                jogada.append (b3)
                jogada.sort () # ordenamento da lista
                
                if jogada not in jogadas_gerais : # verificação de uma aparição ou não dessa sequência anteriormente
                        if b1 < 10 and b2 < 10 and b3 < 10 :
                                print ('0{} 0{} 0{}'.format (b1, b2, b3).center (70)) # organização visual 
                                cont += 1
                        elif b1 < 10 and b2 < 10 :
                                print ('0{} 0{} {}'.format (b1, b2, b3).center (70))
                                cont += 1
                        elif b1 < 10 and b3 < 10 :
                                print ('0{} {} 0{}'.format (b1, b2, b3).center (70))
                                cont += 1
                        elif b2 < 10 and b3 < 10 :
                                print ('{} 0{} 0{}'.format (b1, b2, b3).center (70))
                                cont += 1
                        elif b1 < 10 :
                                print ('0{} {} {}'.format (b1, b2, b3).center (70))
                                cont += 1
                        elif b2 < 10 :
                                print ('{} 0{} {}'.format (b1, b2, b3).center (70))
                                cont += 1
                        elif b3 < 10 :
                                print ('{} {} 0{}'.format (b1, b2, b3).center (70))
                                cont += 1
                        else :
                                print ('{} {} {}'.format (b1, b2, b3).center (70))
                                cont += 1                              
                        jogadas_gerais.append(jogada[:]) # colocação DE UMA CÓPIA em uma lista geral

                jogada.clear() # apaga todos os elementos da lista para ser refeita novamente 

                if cont == 1140 : # número de opções (combinação de 20, 3 a 3 = 1140)
                        break

print ('')
print ('ESTAS SÃO TODAS AS OPÇÕES POSSÍVEIS. BOA SORTE!'.center (70))
print ('')
print ('='*70)
print ('')

# EDIVÂNIA #

