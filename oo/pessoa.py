class Pessoa:
    olhos=2
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
    deividi.sobrenome ="Pinheiro"
    del deividi.filhos
    print(deividi.__dict__)
    print(bernardo.__dict__)
    print(Pessoa.olhos)
    print(deividi.olhos)
    print(bernardo.olhos)
    print(id(Pessoa.olhos), id(deividi.olhos), id(bernardo.olhos))

