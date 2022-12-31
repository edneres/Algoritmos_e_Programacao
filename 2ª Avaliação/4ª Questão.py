# CABEÇALHO #
print ('='*50)
print ('QUESTIONÁRIO'.center (50))
print ('')

cont = 0

# PERGUNTAS #
a = input ('Telefonou para a vítima? [S][N] ').strip().upper()[0]
if a == 'S':
    cont += 1
b = input ('Esteve no local do crime? [S]/[N] ').strip().upper()[0]
if b == 'S' :
    cont += 1
c = input ('Mora perto da vítima? [S]/[N] ').strip().upper()[0]
if c == 'S' :
    cont += 1
d = input ('Devia para a vítima? [S]/[N] ').strip().upper()[0]
if d == 'S' :
    cont += 1
e = input ('Já trabalhou com a vítima? [S]/[N] ').strip().upper()[0]
if e == 'S' :
    cont += 1

print ('')

# VERIFICAÇÃO DE STATUS #
if cont >= 2 :
    if cont == 2 :
        print ('Pessoa classificada como: SUSPEITA!')
    if cont == 3 or cont == 4  :
        print ('Pessoa classificada como: CÚMPLICE!')    
    if cont == 5 :
        print ('Pessoa classificada como: ASSASSINA!')
else :
    print ('Pessoa classificada como: INOCENTE!')

print ('')
print ('='*50)

# EDIVÂNIA #
