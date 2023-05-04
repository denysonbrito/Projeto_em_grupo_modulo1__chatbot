from enderecosacademias import localizacaoacademias
from planosacademia import tiposDeplanos
from TelaInicialAcademia import telaInicial
from horariodasmodalidades import modalidadesPorHorario
from cores import vermelho
from funcoes import tInicial,tdois,tfinal 

"""
Acima, foi feito a importação dos módulos para o código principal ('main'). Importamos as variáveis, funções, listas e cores usando a modularização 'from' e 'import'.
"""

telas=[telaInicial,modalidadesPorHorario,tiposDeplanos,localizacaoacademias,]
"""
Aqui encadiamos todas as telas em uma única lista de nome "telas". 

"""

try:
   print(tfinal(tdois(tInicial(telas,vermelho))))
except :
    print('')
finally:
    print('espero ter ajudado!!!\n\nfim do programa muito obrigado')

"""

Na linha 19 iniciamos o uso do tratamento de erro.
Na linha 20 é usada a função print para chamar as telas. Começando por 'tfinal' que recebe 'tdois' como parâmetro. 'Tdois' recebe 'tInicial' com parâmetros 'telas' e 'vermelho'. 


"""