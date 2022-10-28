url = (
    "https://bytebank.com/cambio?"
    + "quantidade=100&moedaOrigem=real&moedaDestino=dolar"
)

question_mark_index = url.find("?")

if question_mark_index == -1:
    base_url = url
else:
    # Separate base and parameters
    base_url = url[:question_mark_index]
    url_parameters = url[question_mark_index + 1:]

    # Look for the value of a parameter
    search_parameter = "moedaOrigem"
    parameter_index = url_parameters.find(search_parameter)
    value_index = parameter_index + len(search_parameter) + 1
    ampersand_index = url_parameters.find("&", value_index)

    value = (
        url_parameters[value_index:]
        if ampersand_index == -1
        else url_parameters[value_index:ampersand_index]
    )
