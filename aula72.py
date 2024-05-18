
# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1
    for mult in args:
       total *= mult
    return total

multiplicacao = mult(1, 2, 3, 4, 5)
print (multiplicacao)       

# print(1*2*3*4*5)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(num):
    if num % 2 == 0:
        return f'{num} é par'
    return f'{num} é ímpar'

