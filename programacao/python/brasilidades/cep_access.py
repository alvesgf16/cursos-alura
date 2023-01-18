class AddressSearch:
    def __init__(self, cep):
        cep = str(cep)
        if not self.is_cep_valid(cep):
            raise ValueError("Invalid CEP!")
        self.cep = cep

    def is_cep_valid(self, cep):
        return len(cep) == 8
