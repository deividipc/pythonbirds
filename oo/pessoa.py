class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.idade = idade
        self.nome =nome

    def cumprimentar(self):
        return  f'Olá{id(p)}'
if __name__ == '__main__':
    p = Pessoa('Bernardo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome='Deividi'
    print(p.nome)
    print(p.idade)