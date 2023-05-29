'''
Meu instagram: @teuzonrails_
'''

import random

#Declarando função gerar_cpf()
def gerar_cpf():

    # Gerando os 9 primeiros dígitos do CPF de forma aleatória

    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calculando o primeiro dígito verificador

    soma = sum([cpf[i] * (10 - i) for i in range(9)])
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0
    cpf.append(digito1)

    # Calculando o segundo dígito verificador

    soma = sum([cpf[i] * (11 - i) for i in range(10)])
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0
    cpf.append(digito2)

    # Formatando o CPF

    cpf_formatado = ''.join(map(str, cpf))
    cpf_formatado = cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]

    return cpf_formatado

# Saída de dados
cpf_gerado = gerar_cpf()
print('O CPF {} foi gerado com sucesso!'.format(cpf_gerado))
