from url_extractor import URLExtractor


url = "bytebank.com/cambio?quantity=100&moedaOrigem=dolar&moedaDestino=real"
url_extractor = URLExtractor(url)

original_currency = url_extractor.get_parameter_value("moedaOrigem")
new_currency = url_extractor.get_parameter_value("moedaDestino")
quantity = url_extractor.get_parameter_value("quantity")
DOLLAR_VALUE = 5.50  # 1 dollar = 5.50 reais

if original_currency == "real" and new_currency == "dolar":
    conversion_value = int(quantity) / DOLLAR_VALUE
    print(f"R$ {quantity} equals US$ {str(conversion_value)}.")
elif original_currency == "dolar" and new_currency == "real":
    conversion_value = int(quantity) * DOLLAR_VALUE
    print(f"$ {quantity} equals R$ {str(conversion_value)}")
else:
    print(
        f"Exchange from {original_currency} to {new_currency} is not "
        + "available."
    )
