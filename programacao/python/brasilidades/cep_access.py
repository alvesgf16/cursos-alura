import requests


class AddressSearch:
    def __init__(self, cep):
        cep = str(cep)
        if not self.is_cep_valid(cep):
            raise ValueError("Invalid CEP!")
        self.cep = cep

    def __str__(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def is_cep_valid(self, cep):
        CEP_LENGTH = 8

        return len(cep) == CEP_LENGTH

    def access_via_cep(self):
        address_data = self.retrieve_address_data_from_cep()
        return (
            address_data["bairro"],
            address_data["localidade"],
            address_data["uf"],
        )

    def retrieve_address_data_from_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json"
        address_data = requests.get(url).json()
        if "erro" in address_data:
            raise requests.exceptions.HTTPError("CEP not found!")
        return address_data
