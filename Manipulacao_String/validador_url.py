'''Exemplos de URLs válidas:

    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:

    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio'''

#https://www.bytebank.com.br/cambio
import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')   # exatamente igual, usa ().. pode conter,usa [] .. podemos usar um dentro do outro
match = padrao_url.match(url)  # estamos buscando se existe exatamente igual

if not match:
    raise ValueError('A URL não é válida')
else:
    print('A URL é válida')