# expreoçoes regurales (ReegEx)
# são padrões na codificação que queremos encontrar

# Usando a biblioteca 're' conseguimos encontar o padrao independende da posição na string, sem usar muito codigo

import re

endereco = "Rua da Flores 72, apartamento 1002, Rio de Janeiro, RJ, 23440-120"

#padrão -> 5 digitos +hifen(opcional) + 3 digitos
'''padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")'''# vamos passar os caracteries validos para o padrão (o ponto"?" após o "-" indica uma opção, assim ele retorna o padrão com ou sem o ifem
'''padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")'''
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # re.compile('[intervalo de caracter]{vezes}  [caracter]{vezes que pode aparecer}  [intervalo de caracter]{vezes}')
busca = padrao.search(endereco) # Match ou None

if busca:
    cep = busca.group()
    print(cep)


