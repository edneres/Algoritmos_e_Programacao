professor = {'id1':  
            {'nome': ['José'],  
            'disciplinas': ['algoritmos, programação, introdução']}, 

            'id2':  
            {'nome': ['Rodrigues'],  
            'disciplinas': ['calculo, programação, compiladores'] }, 

            'id3':  
            {'nome': ['Torres'],  
            'disciplinas': ['IHC, programação, introdução'] }, 

            'id4':  
             {'nome': ['Neto'],  
             'disciplinas': ['banco de dados, redes, inteligência artificial'] }, 
            } 

lista_chaves = []

print ('='*90)
print ('ATUALIZAÇÃO DE DISCIPLINAS'.center (90))
print ()
print ('Esse é o dicionário "professor" atualmente:')
print ()

for c, v in professor.items () :
    print (c)
    lista_chaves.append (c)
    for cc, vv in v.items () :
        print (f'{cc}: {vv}')
    print ()

print ()
print ('='*90)
número_id = int (input ('Escolha qual "id" você deseja alterar as disciplinas\n[1] id1\n[2] id2\n[3] id3\n[4] id4\n ')) # número a ser utilizado na localização da chave na lista 
print ('=-'*45)
disciplina = str (input ('Quais as novas disciplinas para a atualização? [AS SEPARE COM ","]\n')).split (',') # formação de uma lista de disciplinas
print ('='*90)
print ('ATUALIZAÇÃO CONCLUÍDA'.center (90))
print ()

id = str (lista_chaves [número_id - 1]) # localização da chave na lista ("-1" porque a lista começa do 0)
professor [id] ['disciplinas'] = disciplina # atualização do valor da chave pela nova lista informada pelo usuário

print ('Esse é o dicionário "professor" atualizado:')
print ()

for k, s  in professor.items () :
    print (k)
    for kk, ss in s.items () :
        print (f'{kk}: {ss}')
    print ()

print ('='*90)

# EDIVÂNIA