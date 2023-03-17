import random

#Gerador de nove digitos aleatórios
cpf_nove_digitos = ''
for digitos_gerados in range(9):
    cpf_nove_digitos += str(random.randint(0, 9))

#Primeiro digito do CPF 
num_soma = 11
soma = 0
soma_result = 0
for digitos in cpf_nove_digitos: 
    if num_soma > 2:
        num_soma -= 1
        mult = num_soma * int(digitos)
        soma += mult
soma_result = soma * 10
result_primeiro = soma_result % 11
if result_primeiro > 9:
    print(0)

#Segundo digito do CPF
cpf_nove_digitos = cpf_nove_digitos.replace('.', '').replace('-', '') 
quant_digitos = 11
soma_mult = 0

for digitos in cpf_nove_digitos:
    mult = quant_digitos * int(digitos)
    quant_digitos -= 1
    soma_mult += mult
mult_result = soma_mult * 10
result_segundo = mult_result % 11

#Resultado final do cpf 
cpf_formatado = f'{cpf_nove_digitos[:3]}.{cpf_nove_digitos[3:6]}.{cpf_nove_digitos[6:9]}'
cpf_final_usuario = f'{cpf_formatado}' + f'-{result_primeiro}' + f'{result_segundo}'
print(f'Seu cpf é: {cpf_final_usuario}')