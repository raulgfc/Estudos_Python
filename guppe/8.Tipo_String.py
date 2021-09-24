"""
TIPO STRING
Em Python, um dado é considerado do tipo string sempre que:
- Estiver entres aspas simples. Exemplo:
'uma string, '234', 'True', '42.3'
Alem das seguintes combinacoes:
Estiver entre aspas duplas, aspas triplas,aspas duplas triplas,

"""

nome = 'teste' #Mais Comum
nome2 = "Teste's" #Exemplo de uso com apas duplas
nome3= 'Teste \n' #-> /n PULANDO LINHA
nome5 = 'Raul'
print(nome, nome2,nome3)ome = 'teste' #Mais Comum
nome2 = "Teste's" #Exemplo de uso com apas duplas
nome3= 'Teste \n' #-> /n PULANDO LINHA
nome5 = 'Raul'
print(nome, nome2,nome3)

#Arrays de string
#[0,1,2,3,4,5,6,7,8,9,10]
#[R,A,U,L, ,C,O,R,R,E,A]
nome4 = 'RAUL CORREA'
print(nome4[5:11])

print(nome5.split()[0])

"""
[:: -1] -> comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome5[::-1])

print(nome5.replace('R','S')) #funcão replace