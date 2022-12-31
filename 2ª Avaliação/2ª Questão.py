# CABEÇALHO #
print ('')
print ('='*50)
print ('')
print ('BASE DE DADOS'.center (50))
print ('')
print ('-'*50)
print ('')

# FORMAÇÃO PRIMEIRA LISTA #
print ('Lista do usuário 1')
print('')
l1 = []
for n in range (0, 10) :
    u1 = input ('Digite um único nome: ').strip().capitalize()
    l1.append (u1)
print('')
print ('Dados coletados com sucesso!')

print ('')
print ('-'*50)
print ('')

# FORMAÇÃO SEGUNDA LISTA #
print ('Lista do usuário 2')
print('')
l2 = []
for n in range (0, 10) :
    u2 = input ('Digite um único nome: ').strip().capitalize()
    l2.append (u2)
print('')
print ('Dados coletados com sucesso!')

print ('')
print ('-'*50)
print ('')
print ('FIM DA COLETA DE DADOS')
print ('')
print ('-'*50)
print ('')

# VERIFICAÇÃO DE ELEMENTOS IGUAIS NAS LISTAS #
lista_dos_iguais = []
for a in range (0,10) :
    if l1 [a] in l2 :
        lista_dos_iguais.append (l1 [a])
    
print ('Ambos os usuários possuem os seguintes amigos em comum: {}'.format (lista_dos_iguais))

print ('')
print ('='*50)
print ('')

# EDIVÂNIA #



#== Identificação ==#
print("Aluna: Maria Edivânia\nCurso: Engenharia Elétrica, 2020.2")