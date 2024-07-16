class Log:
    def __init__(self, *args, **kwargs):
        self.escreva = kwargs.get('escreva')
        self.pAL = kwargs.get('pAL')

    def ler(self):
        with open(self.pAL, 'r', encoding='utf-8') as arquivo:  # type: ignore
            return arquivo.read()

    def limpar(self):
        with open(self.pAL, 'w') as arquivo:  # type: ignore
            arquivo.write('')

    def escrever(self):
        try:
            with open(self.pAL, 'a') as arquivo:  # type: ignore
                arquivo.write('\n' + self.escreva)  # type: ignore
        except TypeError as e:
            print(f'LOG o erro: (({e})) o pAL é: (({self.pAL})) ')


if __name__ == '__main__':
    escreva = 'Davi'
    pAL = 'Select/DISAL/log.txt'
    Log(pAL=pAL).limpar()
    # Log(pAL=pAL, escreva=escreva).escrever()
    print(Log(pAL=pAL).ler())
