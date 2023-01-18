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