class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_requests_get(url, **kwargs):
    if url == "https://viacep.com.br/ws/49020050/json":
        return MockResponse(
            {"bairro": "Treze de Julho", "localidade": "Aracaju", "uf": "SE"},
            200,
        )
    else:
        return MockResponse({"erro": True}, 200)
