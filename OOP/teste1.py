class Aluno():
    def __init__(self, nome, dataNasc, turma):
        self.nome = nome
        self.dataNasc = dataNasc
        self.turma = turma


    def texto(self, prof):
        print(f"Olá professor {prof}.")
        print(f"O aluno {self.nome} nascido em {self.dataNasc} está na turma {self.turma}.")

prof = str(input("Digite seu nome: ".strip().title()))

aluno1 = Aluno("Gabriel", "02/12/2004", "3A")
        
aluno2 = Aluno("Gustavo", "23/01/2002", "5A")
print(aluno2.nome)
print(aluno1.nome)

escolha = str(input("Qual aluno você deseja ver? "))





class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} está comendo")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gato = Gato("Meownt", "Branco")

gato.comer()

