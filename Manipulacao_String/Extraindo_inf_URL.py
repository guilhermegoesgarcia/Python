# extrator de informações contidas na URL

url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Sanitização da URL (removendo espaços em branco)
url = url.replace(" ","") # ou url.strip()

# Validando a Url
if url == "":
    raise ValueError(" A URL está vazia! ")

# Separa base e parâmetro
indice_interrogacao = url.find('?')
url_base = url[7:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]
indice_parametro_e = url_parametro.find('&')

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1

valor = url_parametro[indice_valor:indice_parametro_e]

if indice_parametro_e == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_parametro_e]

print(f'url_base => {url_base}')
print(f'url_parametro => {url_parametro}')
print(f'url_valor => {valor}')