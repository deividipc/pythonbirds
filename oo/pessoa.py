class Pessoa:
    def __init__(self,*filhos,nome=None,idade=39):
        self.idade = idade
        self.nome =nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return  f'Olá{id(self)}'
if __name__ == '__main__':
    bernardo = Pessoa(nome='Bernardo')
    #mariana = Pessoa(nome ="Mariana")
    deividi = Pessoa(bernardo, nome="Deividi")
    #deividi = Pessoa(mariana, nome="Deividi")
    print(Pessoa.cumprimentar(deividi))
    print(id(deividi))
    print(deividi.cumprimentar())
    print(deividi.nome)
    print(deividi.idade)
    for filho in deividi.filhos:
        print(filho.nome)