url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

# Sanitizar a URL

url = url.strip()

# Validar URL
if url == '':
    raise ValueError('A URL está vazia')


# Separa base e os parâmetros
indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


parametro_busca = 'moedaDestino'

# Busca o valor do parâmetro
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)


# Se não tiver o & na url, quer dizer que é o último parâmetro
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
print(url_parametros)
