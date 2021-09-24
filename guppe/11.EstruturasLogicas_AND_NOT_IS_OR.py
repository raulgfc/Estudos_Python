"""
Estruturas logicas: and (e), or (ou), not (nao), is (é)

OPERADORES UNÁRIOS:
    -not
OPERADORES BINÁRIOS:
    -and, or, is
"""
#PARA O and, AMBOS OS VALORES PRECISAM SER TRUE
#PARA O or, UM OU OUTRO VALOR PRECISAM SER TRUE
#PARA O not, O VALOR DO BOOLEANO É INVERTIDO, OU SEJA, TRUE vira FALSE, e, FALSE vira TRUE.


ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário :]')
else:
    print ('Voce precisa estar ativo e logado :[')

#Exemplo de is
#ativo é(is) falso?
print(ativo is False)