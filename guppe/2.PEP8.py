"""
PEP8

PEP 8 - PYTHON ENCHACEMENTE PROPOSAL
Sao propostas de melhorias para a linguagem Python
The Zen of Python
import this 
A ideia do PEP8 é que possamos escrever códigos Python de forma Pythonica.

IDEIAS PRINCIPAIS:

[1] -  Utilize camel case para nomes de classes

[2] -  Utilize nomes em minúsculo, separados por underline para funcoes ou variaveis

[3] - Utileze 4 espaços par identaçao (NAO USE TAB) !!!!!

[4] - Linhas em branco

[5] - Imports devem ser feitos em linhas separadas

[6] - Espaços em expressoes e instrucoes

[7] - Termine sempre uma instrucao com uma nova linha   
"""""

"""Exemplo [1]"""
class Calculadora:
    pass


"""Exemplo [2]"""
def soma():
    pass


def soma_dois():
    pass


"""Exemplo [3]"""

if 'a' in 'banana':
    print('tem')


"""Exemplo [4]
- Separar funções e definicoes de classe com duas linhas em branco
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco"""

"""Exemplo [5]
-- imports devem ser feitos em linhas separadas

#Errado
import sys, os

#Correto
import sys
import os

#Porem nao ha problemas em utilizar:
from types import StringType, ListType

#Caso tenha muitos imoports de um mesmo pacote, recomenda-se fazer:
from types_import (
   StringType,
   ListType,
   SetType,
   OutroType
)


#Imports devem ser colocados no topo do arquivo, logo depois de qualquer comentario
#...ou docstrings e antes de quaisquer variaves globais
"""


"""Exemplo [6]
#Nao faca: funcao (algo [ 1 ], { outro: 2 })
#Faca funcao (algo[1], {outro:2 })

#Nao faca: algo (1) 
#Faca: algo(1)

NAO COLOQUE ESPAÇOS!

"""

"""EXEMPLO [7]
import this 
print('algo')
"""