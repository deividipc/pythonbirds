class Pessoa:
    olhos=2
    def __init__(self,*filhos,nome=None,idade=39):
        self.idade = idade
        self.nome =nome
        self.filhos=list(filhos)

    def cumprimentar(self):
        return  f'Olá meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def metodo_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()

        return f'{cumprimentar_da_classe}. Aperto de mão'
class Mutante(Pessoa):
    #def cumprimentar(self):
        #return 'Olhada com o olho que tudo vê'
    olhos = 3


if __name__ == '__main__':
    bernardo = Mutante(nome='Bernardo')
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
    deividi.olhos=1
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
    print(bernardo.olhos)
    print(bernardo.cumprimentar())
    print(deividi.cumprimentar())

