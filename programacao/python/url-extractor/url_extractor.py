class URLExtractor:
    def __init__(self, url):
        self.url = url

    def get_base_url(self):
        question_mark_index = self.url.find("?")

        return (
            self.url
            if question_mark_index == -1
            else self.url[:question_mark_index]
        )

    def get_url_parameters(self):
        question_mark_index = self.url.find("?")

        return self.url[question_mark_index + 1:]

    def get_parameter_value(self, parameter_name):
        url_parameters = self.get_url_parameters()
        parameter_index = url_parameters.find(parameter_name)
        value_index = parameter_index + len(parameter_name) + 1
        ampersand_index = url_parameters.find("&", value_index)

        return (
            url_parameters[value_index:]
            if ampersand_index == -1
            else url_parameters[value_index:ampersand_index]
        )
