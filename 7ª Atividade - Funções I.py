def somaImposto (taxaImposto, custo) :
        print ()
        produto = input ('Nome do produto: ').title () .strip ()
        valor_final = custo * (1 + (taxaImposto/100))
        print ('O valor final do produto {}, após a aplicação do imposto sobre vendas de \033[31m{}%\033[m sobre o valor de custo de R$ {:.2f},'.format (produto, taxaImposto, custo), 'é: \033[32mR$ {:.2f}\033[m .'.format (valor_final))
        print ()
        
print ()
print ('=-'*70)
print ('CÁLCULO DE IMPOSTO SOBRE PRODUTO'.center (130))
print ('=-'*70)
somaImposto (1.5, 15.75) # COLOCAR OS PARÂMETROS "TAXAIMPOSTO" E "CUSTO"... esses são só um exemplo!
print ('=-'*70)
print ()

# EDIVÂNIA