url = (
    "bytebank.com/cambio?moedaOrigem=real"
)

question_mark_index = url.find("?")

if question_mark_index == -1:
    base_url = url
else:
    base_url = url[:question_mark_index]
    url_parameters = url[question_mark_index + 1:36]
