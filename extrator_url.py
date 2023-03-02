class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not bool(self.url):
            raise ValueError('A URL está vazia')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao+1:]

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            return self.get_url_parametros()[indice_valor:]
        else:
            return self.get_url_parametros()[indice_valor:indice_e_comercial]


valor = ExtratorURL(None)
quantidade = valor.get_valor_parametro('quantidade')

print(quantidade)
