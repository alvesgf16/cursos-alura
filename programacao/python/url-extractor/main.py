url = (
    "bytebank.com/cambio?moedaOrigem=real"
)

question_mark_index = url.find("?")

if question_mark_index == -1:
    base_url = url
else:
    base_url = url[:question_mark_index]
    url_parameters = url[question_mark_index + 1:36]

    search_parameter = "moedaOrigem"
    parameter_index = url_parameters.find(search_parameter)
    value_index = parameter_index + len(search_parameter) + 1
    ampersand_index = url_parameters.find("&", value_index)

    value = (
        url_parameters[value_index:]
        if ampersand_index == -1
        else url_parameters[value_index:ampersand_index]
    )
