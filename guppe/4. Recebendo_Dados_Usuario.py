"""Recebendo dados de usuario"""


#Exemplo ANTIGO - Versao 2.x
#Entrada de dados
"""
print('Qual o seu nome?')
nome = input()

print("Qual a sua idade")
idade = input()
#Processamento

#Saida de dados
print('Seja bem vinda(o) %s' % nome, idade)
"""""

#Exemplo Moderno - Versao 3.x
"""

print('Qual o seu nome?')
nome = input ()
print('Seja Bem Vinda (o) {0}'.format(nome))

print ("Qual a sua idade?")
idade = input()

print('A(O) {0} tem {1} anos'.format(nome,idade))
"""


#Exemplo + Moderno - Versao 3.7

nome = input ('Qual o seu nome?')
print(f'Seja bem vinda(o) {nome}')

idade = int(input("Qual a sua idade?")) #Fazendo o CAST (Convertendo)
print(f'A(o) {nome} tem {idade} anos')

