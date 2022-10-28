from url_extractor import URLExtractor

url = (
    "https://bytebank.com/cambio?"
    + "quantidade=100&moedaOrigem=real&moedaDestino=dolar"
)

url_extractor = URLExtractor(url)
