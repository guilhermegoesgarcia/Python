#criando uma classe para tornar o código mais legivel e funcional
import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url) # tratamento da variavel
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url)==str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia !")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')  # exatamente igual, usa ().. pode conter,usa [] .. podemos usar um dentro do outro
        match = padrao_url.match(self.url)  # estamos buscando se existe exatamente igual
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[7:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&',indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parametros: " + self.get_url_parametro() + "\n" + "Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other

extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print('O tamanho da URL:',len(extrator_url))
print(extrator_url)
print(valor_quantidade)
