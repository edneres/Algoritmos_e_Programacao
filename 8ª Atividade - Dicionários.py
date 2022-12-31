professor = {
            'id1':
            {'nome': ['José'],
            'disciplina': ['algoritmo', 'programação', 'introdução']},
            'id2':
            {'nome': ['Torres'],
            'disciplina': ['cálculo', 'programação', 'compiladores']},
            'id3':
            {'nome': ['José'],
            'disciplina': ['algoritmo', 'programação', 'introdução']}
            }

lista_de_valores = []
lista_das_chaves_principais = []
professor_sem_duplicados = {} 

print ()
for k, v in professor.items () :    # 'k' são as chaves principais (id1, id2, id3) e 'v' são os seus respectivos valores.

    if v not in lista_de_valores :    # como o que intereça é a eliminação dos duplicdos, vai-se levar em consideração apenas os valores 'v' na análise,
        lista_de_valores.append (v)        # guardando cada valor EM ORDEM em uma lista separada
        lista_das_chaves_principais.append (k)  # da lista da sua respectiva chave, ou seja, a posição 0, por exemplo - em ambas as listas - estão relacionadas, sendo uma chave e valor da outra.

for n in range (0, len (lista_de_valores)) :    # como ambas as listas tem o mesmo tamanho, tanto faz qual terá o seu tamanho lido pela função.
    professor_sem_duplicados [lista_das_chaves_principais [n]] = lista_de_valores [n]   # vai adicionando ao novo dicionário, NA ORDEM, as chaves e valores guardados nas listas.
    
print (professor_sem_duplicados)
print ()

#EDIVÂNIA