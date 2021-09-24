"""
Escopo de variaveis

Dois caso de escopo:
1 - Variaveis Globais
    Variavies globais sao reconhecidas, ou seja, seu escopo compreende todo o programa

2 - Variaveis Locais
    Variaveis locais sao reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escpo esta limitado
    ao bloco onde foi declaro

    Python é uma linguagem de ripagem dinamica. Isso sifnifica que ao
    declararmos uma variavel, nos nao colocamos o tipo de dado dela
    Este tipo é inferido ao atribuirmos o valor a mesma

"""

numero = 42
print(numero)
print (type(numero)) #Identifica de forma automatica o tipo de dado

numero2 = 'geek'
print (numero2)
print (type(numero2)) #Identifica de forma automatica o tipo de dado


#DEFINICAO DE ESCOPO


variavel_global = 'oi'
print(variavel_global)

variavel_local = 33

if variavel_local > 10:
    novo = numero + 10 # A variavel novo esta declarada localmente dentro do bloco IF. Portanto é local
    print(variavel_local)

print (novo)