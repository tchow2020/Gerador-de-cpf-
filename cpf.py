"""
Calculo do segundo dígito do CPF
CPF: 143.762.994-64
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  143.762.994-64 (143762994-6)
   11 10  9  8  7  6  5  4  3  2
*  1   4  3  7  6  2  9  9  4  6 <-- PRIMEIRO DIGITO
   11 40 27 56 42 12 45 36  12 12
Somar todos os resultados:
11+40+27+56+42+12+45+36+12+12 = 293
Multiplicar o resultado anterior por 10
293 * 10 = 2930
Obter o resto da divisão da conta anterior por 11
2930 % 11 = 4
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""
import sys

#Primeiro digito do CPF
cpf_primeiro = input('digite os nove primeiros digitos do seu cpf: ')
num_soma = 11
soma = 0
soma_result = 0

if len(cpf_primeiro) > 9 or len(cpf_primeiro) < 9:
    print('Pfvr informe nove digitos.')
    sys.exit()
for digitos in cpf_primeiro: 
    if num_soma > 2:
        num_soma -= 1
        mult = num_soma * int(digitos)
        soma += mult
soma_result = soma * 10
result_primeiro = soma_result % 11
if result_primeiro > 9:
    print(0)

#Segundo digito do CPF
cpf_segundo = '143.762.994-6'.replace('.', '').replace('-', '') 
quant_digitos = 11
soma_mult = 0

for digitos in cpf_segundo:
    mult = quant_digitos * int(digitos)
    quant_digitos -= 1
    soma_mult += mult
mult_result = soma_mult * 10
result_segundo = mult_result % 11

#Resultado final do cpf 
cpf_formatado = f'{cpf_primeiro[:3]}.{cpf_primeiro[3:6]}.{cpf_primeiro[6:9]}'

cpf_final_usuario = f'{cpf_formatado}' + f'-{result_primeiro}' + f'{result_segundo}'
print(cpf_final_usuario)
# print(f'o seu cpf é 143762994' + f'-{result_primeiro}'+f'{result_segundo}')