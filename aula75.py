
# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplica(x):
    # return x * 2
# 
# def triplica(x):
    # return x * 3
# 
# def quadruplica(x):
    # return x * 4
# 
# print(duplica(2))
# 
# print(triplica(2))
# 
# print(quadruplica(2))

# Crie uma função fala se um número é par ou ímpar.

def par_ou_impar(num):
    if num % 2 == 0:
        return f'{num} é par'
    return f'{num} é ímpar'

primeiro_numero = input('primeiro numero: ')
segundo_numero = input('segundo numero: ')

print(par_ou_impar(int(primeiro_numero)))

print(par_ou_impar(int(segundo_numero)))

# Crie uma função fala se um número é positivo ou negativo.
# 
# def positivo_ou_negativo(num):
    # if num > 0:
        # return f'{num} é positivo'
    # return f'{num} é negativo'
# 
# print(positivo_ou_negativo(2))
# 
# print(positivo_ou_negativo(-2))

