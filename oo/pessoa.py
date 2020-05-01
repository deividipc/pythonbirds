class Pessoa:
    olhos=2
    def __init__(self,*filhos,nome=None,idade=39):
        self.idade = idade
        self.nome =nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return  f'Olá{id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def metodo_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
class Homem(Pessoa):
    pass


if __name__ == '__main__':
    bernardo = Homem(nome='Bernardo')
    #mariana = Pessoa(nome ="Mariana")
    deividi = Homem(bernardo, nome="Deividi")
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
    print(Pessoa.metodo_estatico(), deividi.metodo_estatico())
    print(Pessoa.metodo_classe(), deividi.metodo_classe())
    pessoa = Pessoa("Anonimo")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(deividi, Pessoa))
    print(isinstance(deividi, Homem))