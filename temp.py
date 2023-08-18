"""
    DOBRANDO UM NÚMERO
num_1 = input('Digite o primeiro número: ')

try:
    num_1_int = int(num_1)
    
    print(f'o número dobrado é {num_1_int * 2}')
    
except:
    print('Digite corretamente')"""
    
"""
    SOMANDO UM NÚMERO
def soma_numero():
    num_1 = float(input('Digite o primeiro número: '))
    num_2 = float(input('Digite o segundo número: '))
    resultado = num_1 + num_2
    return resultado

print('A soma dos dois números é: ', soma_numero())"""

"""
    MODULO DO NÚMERO
def modulo_numero():
     num_1 = float(input('Digite o número: '))
     modulo = (num_1 ** 2) ** (1/2)
     return modulo

print('o módulo é: ', modulo_numero())"""

"""
    NUMERO AO QUADRADO
def quadrado_numero():
    num_1 = float(input('Digite um número: '))
    resultado = num_1 ** 2
    return resultado

print('O número ao quadrado é:', quadrado_numero())"""

"""
    CALCULAR O FATORIAL
num_1 = int(input('fatorial de: '))

resultado = 2
count = 2

while count <= num_1:
    resultado *= count
    count += 1

print(resultado)"""

"""
    NUMERO MAIOR
def busca_maior():
    num_1 = float(input('Digite o primeiro número: ')) 
    num_2 = float(input('Digite o segundo número: ')) 
    if num_1 > num_2:
        return num_1
    else:
        return num_2
    
print('O maior número é: ', busca_maior())"""

"""
    BUSCAR ANTECESSOR
def buscar_antecessor():
    num = float(input('Digite o número: '))
    resultado = num - 1
    return resultado

print('O antecessor é: ', buscar_antecessor())"""

"""
    BUSCAR MENOR
def busca_menor():
    num_1 = float(input('Digite o primeiro número: ')) 
    num_2 = float(input('Digite o segundo número: ')) 
    if num_1 < num_2:
        return num_1
    else:
        return num_2
    
print('O maior número é: ', busca_menor())"""


"""
    NUMERO PAR
def numero_par():
    num_1 = int(input('Digite o número: '))
    resultado = num_1 % 2
    
    if resultado == 0:
        resultado = "par"
        return resultado
    
    else: 
        resultado = "impar"
        return resultado
    
print("O número digitado é: ", numero_par())"""

"""
    CALCULAR RAIZ QUADRADA
import math

def calcular_raiz_quadradra():
    numero = float(input('Digite um número: '))
    raiz_quadrada = math.sqrt(numero)
    return raiz_quadrada

print('A raiz quadrada é: ', calcular_raiz_quadradra())"""

"""
    EQUAÇÃO DE SEGUNDO GRAU / TESTE
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    c = int(input('Digite o terceiro número: '))
    
    delta = (b**2)-4*a*c
    
    if a == 0:
        print('Digite um número diferente de zero.')
        
    elif delta < 0:
        print('Sem raízes reais.')    
        
    else:
        x1 = (-b + delta ** (1/2)) / (2*a)
        x2 = (-b - delta ** (1/2)) / (2*a)
        
        print(f'x1: {x1}, x2: {x2}')"""
 
    
    
    
    
    
    
    
    
    
    