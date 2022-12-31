print('=x='*26)

from time import sleep

s = str ( (input ('Informe o seu sexo [M]/[F]: ').strip().upper()))
while s != 'M' and s != 'F' :
    s = str ((input ('Por favor, informe uma opção válida para o seu sexo [M]/[F]: ').strip().upper()))
print('\033[33mInformação salva com sucesso!\033[m')

print('')

if s == 'M' :
    i = int( input ('Informe a sua idade: ').strip())
    c = int( input ('Informe o seu tempo de contribuição: ').strip())
    while c >= i :
        i = int( input ('Por favor, informe uma opção válida para a sua idade: ').strip())
        c = int( input ('Por favor, informe uma opção válida para o seu tempo de contribuição: ').strip())
    print('\033[33mInformação salva com sucesso!\033[m')
    sleep(1)
    print('')
    if (i >= 65 and  c >=10) or (i >= 63 and c >= 15) :
        print ('\033[32;1mAPOSENTÁVEL\033[m')
    else :
        print ('\033[31;1mNÃO APOSENTÁVEL\033[m')

else :
    i = int( input ('Informe a sua idade: ').strip())
    c = int( input ('Informe o seu tempo de contribuição: ').strip())
    while c >= i :
        print('','\n\033[91mDados inconsistentes\033[m')
        i = int( input ('Por favor, informe uma opção válida para a sua idade: ').strip())
        c = int( input ('Por favor, informe uma opção válida para o seu tempo de contribuição: ').strip())
    print('\033[33mInformação salva com sucesso!\033[m')
    sleep(1)
    print('')
    if (i >= 63 and  c >=10) or (i >= 61 and c >= 15) :
        print ('\033[32;1mAPOSENTÁVEL\033[m')
    else :
        print ('\033[31;1mNÃO APOSENTÁVEL\033[m')

print('=x='*26)