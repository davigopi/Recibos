class MinhaClasse:
    def __init__(self):
        self.variavel = 0
        self.total = 0

    @property
    def atualizar_variavel(self):
        return None

    @atualizar_variavel.setter
    def atualizar_variavel(self, novo_numero):
        self.total = novo_numero + self.variavel
        print("Novo valor:", self.total)


minhaClasse = MinhaClasse()

minhaClasse.variavel = 10

minhaClasse.atualizar_variavel = 2
