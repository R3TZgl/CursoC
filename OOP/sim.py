class Pessoa():
    def __init__(self, nome, idade, cao):
        self.nome = nome
        self.idade = idade
        self.cao = cao
        
        
    def treinar(self):
        self.cao.daApatinha()
        self.cao.latir()
        
        
class Cachorro():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        
        
    def daApatinha(self):
        print(f"{self.nome} deu a patinha")
        
        
    def latir(self):
        print("AUAUAUAUAUUAUAUUA")
        
        
def cadastro(pessoa, contador):
    pessoas[f"{pessoa}{contador}"] = pessoa
    print(f"a pessoa {pessoa.nome} foi cadastrada")
            

pessoas = {}

dog1 = Cachorro("Thor", "preto")
pessoa1 = Pessoa("Gabriel", "17", dog1)

dog2 = Cachorro("Batavo", "marrom")
pessoa2 = Pessoa("Jaci", "47", dog2)

pessoas["pessoaUm"] = pessoa1
pessoas["pessoaDois"] = pessoa2





print("Pessoas Cadastradas:")
for c in pessoas:
    print(pessoas[c].nome)