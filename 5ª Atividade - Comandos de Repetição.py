print ('')
print('=x='*18)
print('')

# Escreva um programa que calcule a média de n valores.

n = float (input ('Número: '))
n2 = float (input ('Número: '))
c = str (input ('Mais um número ? \033[92m[S]\033[m/\033[91m[N]\033[m ')).strip().upper()
s = n + n2
q = 2
print('')
if c == 'S':
    while c == 'S':
        n = float (input ('Número: '))
        s += n
        q = q + 1
        c = str (input ('Mais um número ? \033[92m[S]\033[m/\033[91m[N]\033[m ')).strip().upper()
        print('')

print('A média dos números é {}'.format (s/q))

print ('')
print('<>'*26)
print('')

# Escreva um programa que calcule o fatorial de um número.
n = int( input('Número: '))
f = 1 
if n == 0 :
    print('O fatorial de 0 é, por definição, igual à 1.')
else:   
    for c in range (n,1,-1) :
        f = f*c
    print('O fatorial de {} é {}'.format (n,f))

print ('')
print('<>'*26)
print('')

# Escreva um programa que determina se um número inteiro positive n é primo

n = int (input ('Número: '))
q = 0

for c in range (n, 0, -1):
    if n%c == 0 :
        q += 1
if q == 2 :
    print('O número {} \033[92mÉ PRIMO\033[m!'.format (n))
else :
    print('O número {} \033[91mNÃO É PRIMO\033[m!'.format (n))

print ('')
print('=x='*18)
print('')


#== Identificação ==#
print("Aluna: Maria Edivânia\nCurso: Engenharia Elétrica, 2020.2")