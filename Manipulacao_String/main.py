from ExtratorArgumentosUrl import ExtratorArgumentosUrl
'''
argumento ="www.bytebank.com/cambio?moedaorigem=real"
index = argumento.find('=')
substring = argumento[index + 1:]
print(substring)
'''

url = 'https://www.bytebank.com.br/Cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500'
print(ExtratorArgumentosUrl.urlEhValida(url))

argumentosUrl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaOrigem, moedaDestino, valor)