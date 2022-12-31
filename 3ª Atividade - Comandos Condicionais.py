##--Maria Edivânia--##

import random
lista = ('Pedra', 'Papel', 'Tesoura')
jogada = random.randint(0,2)

print('')

print('==x=='*22)

print('')

player1 = input("Qual será o seu nome de jogador? ")
player2 = 'PC'
print("Olá, {}. Eu serei o player dois e veremos quem de nós têm mais sorte! E bem... eu sou muito competitivo kkkkk\nSuas opções de jogada são:\n[0] Pedra\n[1] Papel\n[2] Tesoura".format (player1))

print('')

pc = '\033[32mEu ganhei! B)\033[m'
eu = '\033[32mVocê ganhou -_-\033[m'
em = '\033[32mOpa! Deu empate kkkkk\033[m'

print('==x=='*22)

print('')

print('\033[1;34mRodada Única\033[m')

print('')

j1 = int(input ('{}: '.format (player1)))
j2 = print('{}: {} '.format (player2, jogada))

print('')

if j1 == 0 :
    if jogada == 1 :
        print(pc)
        print('\033[32mPapel cobre  pedra.\033[m')
        print('')
    if jogada == 2 :
        print(eu)
        print('\033[32mPedra quebra tesoura.\033[m')
        print('')
    if j1 == jogada :
        print (em)
        print('')


if j1 == 1 :
    if jogada == 2 :
        print('\033[32mTesoura corta papel.\033[m')
        print(pc)
        print('')
    if jogada == 0 :
        print(eu)
        print('\033[32mPapel cobre a pedra\033[m')
        print('')
    if j1 == jogada :
        print (em)
        print('')

if j1 == 2 :
    if jogada == 0 :
        print(pc)
        print('\033[32mPedra quebra tesoura.\033[m')
        print('')
    if jogada == 1 :
        print(eu)
        print('\033[32mTesoura ganha do papel.\033[m')
        print('')
    if j1 == jogada :
        print (em)
        print('')

print('\033[36mAté a próxima, {}. Quem sabe não jogamos mais depois ;)\033[m'.format(player1))

print('==x=='*22)
print('')

##--Edivânia--##


#== Identificação ==#
print("Aluna: Maria Edivânia\nCurso: Engenharia Elétrica, 2020.2")