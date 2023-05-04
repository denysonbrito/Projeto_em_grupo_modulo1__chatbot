
def entradaEtela (tela,od=3,cor1='\033[38;2;255;255;255m',cor2='\033[38;2;255;255;255m'):
    resposta=(input((tela+'{0}digite a opção desejada{1}:').format(cor1,cor2)))
    while resposta.isnumeric()==False or int(resposta)>od:
        resposta=(input("\033[38;2;255;0;0m"+"erro digite novamente:"+"\033[0m"))
    return int(resposta)

"""
A função 'entradaEtela' é responsável por imprimir a tela inicial e retornar o input do usuário. 
Ela recebe os parâmetros 'tela', 'od(opções do usuário)', 'cor1' e 'cor2'. O parâmetro 'tela' é obrigatório, já os outros são opcionais e possuem valor padrão. 
O input dentro da variável resposta apresenta o parâmetro 'tela' que é concatenado com a string 'digite a opção desejada', dentro do input. Essa string recebe formatação (.format) de 'cor1' e 'cor2'.
Na linha 4 inicia-se um laço de repetição 'while'. A variável 'resposta' é submetida ao método 'isnumeric' que retorna um valor booleano; avaliando se a string é ou não um valor numérico apontando 'True' ou 'False'. Se o retorno do método for 'False' ou o retorno da variável 'resposta' transformada em um numero inteiro (int) for maior que o parâmetro 'od', o programa inicia o looping. 
Caso o looping se inicie, a variável resposta imprime um novo input 'erro digite novamente' na cor vermelha. O looping continua até que a variável resposta contenha um valor numérico inteiro menor ou igual ao parâmetro 'od'. Assim que é terminado a função retorna a variável resposta em um numero inteiro (int). 
"""

def tInicial(telas,cor1):
    pi=entradaEtela(telas[0],len(telas)-1,cor1)
    if pi>0:
        return [telas,pi,cor1]
    
""" 
A função 'tInicial' é responsável por imprimir a tela inicial e retornar o valor a partir desta tela.
Ela recebe dois parâmetros 'telas' e 'cor1'. O primeiro é uma lista, já o segundo parâmetro é um código de cor no formato 'ansi' para estilização do texto.
A variável 'pi(parâmetro inicial)' chama a função 'entradaEtela' dando como primeiro parâmetro para a função o primeiro item da lista 'telas' indexado com valor [0]. O segundo parâmetro usa a função 'len' para retornar o numero de itens na lista 'telas' e o subtrai por -1 para que possa ser usado como um numero de escolha. O ultimo parâmetro 'cor1' é para estilização do texto. 
Na linha 18 usamos 'if' para determinar uma condição: Se a variável 'pi' for maior que 0, então ela retorna uma lista contendo a lista 'telas', a variável 'pi' e o parametro 'cor1'. Se a variável 'pi' for igual a 0 a função se encerra pois na tela inicial se abre a possibilidade de fechar o programa utilizando a opção 0. 

"""
         
def tdois(pg):
    telas,pi,cor1=pg
    i=True
    while i==True:
        ps=(entradaEtela(telas[pi][0],len(telas[pi])-1,cor1))
        if ps>0:
            i=False
            return [telas,pi,ps,cor1] 
        else:
            telas,pi,cor1=tInicial(telas,cor1)

"""
A função 'tdois' é responsável por receber o retorno da função 'tInicial' e a partir disso imprimir o valor escolhido pelo cliente em 'tInicial' e receber um novo valor para prosseguir para a próxima tela ou retornar para a tela inicial. 
Essa função recebe o parâmetro 'pg(parâmetros gerais) ' que é uma lista, que contém: 'telas', 'pi' e 'cor1'. Na linha 30 o parâmetro pg é desempacotado com nas variaveis 'telas' 'pi' e 'cor1'. 
Na linha 31 a variável 'i' recebe o valor 'True' para que na linha seguinte possa iniciar o laço de repetição 'while'. Dentro do looping, a variável 'ps' recebe a função entradaEtela contendo os parâmetros 'telas'(com indexação [pi][0]), len(telas[pi])-1 e 'cor1'. A condicionante if determina que se a variável 'ps' for maior que 0, então a variável 'i' é atribuída ao valor 'False', sendo assim retornando '[telas,pi,ps,cor1]'. Caso contrário (else), ou seja, a variável 'ps' for igual a 0, as variáveis 'telas', 'pi' e 'cor1' chamam a função tInicial. Assim mantendo o looping até que 'ps' seja maior que 0. 

"""

def tfinal(pg):
    telas,pi,ps,cor1=pg
    i=True
    while i==True:
        pf=(entradaEtela(telas[pi][ps],1,cor1))
        if pf>0:
            i=False
            return pf 
        else:
            telas,pi,ps,cor1=tdois([telas,pi,cor1])

"""

A função 'tfinal' é responsável por finalizar o atendimento ou retornar a tela anterior. Ela recebe o parâmetro 'pg'. Que é desempacotado por 'telas','pi','ps','cor1' na linha 48. 
A variável 'i' é atribuída ao valor "True" para que na linha 50 inicie-se o looping em 'while'. No looping, enquanto "i" for igual a "True", a variável 'pf(parâmetro final)' recebe a função entradaEtela com os parâmetros: 'telas'(indexado por [pi]e[ps]),'1' e 'cor1'. O parâmetro 1 é usado para limitar as alternativas do usuário em 1 ou 0. Ainda dentro do looping, temos a condição 'if', que determina que, se a variável 'pf' for maior que 0, então a variável 'i' é igual a "False", sendo assim se retorne a variável "pf". Caso contrário (else), ou seja se 'pf' for igual a 0, as variáveis 'telas','pi','ps','cor1' chamam a função 'tdois'. Assim retornando a tela a tela anterior.


"""