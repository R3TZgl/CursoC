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
    pessoas[f"pessoa{contador}"] = pessoa
    print(f"a pessoa {pessoa.nome} foi cadastrada")
    
            

pessoas = {}
contador = 0


#Início do PetShop
while True:
    contador += 1
    
    #Cadastro
    nome = str(input("Digite seu nome: ").strip().title())
    idade = str(input("Digite sua idade: ").strip().title())
    nome_dog = str(input("Digite o nome do seu cachorro: ").strip().title())
    cor = str(input("Digite a cor do seu cachorro: ").strip().title())

    dog1 = Cachorro(nome_dog, cor)
    pessoa = Pessoa(nome, idade, dog1)

    print(f"\nOlá {pessoa.nome} e {dog1.nome}, sejam bem-vindos ao petshop.")
    print(f"Não se esqueça, o número do seu cadastro é {contador}.")
    print(f"Vamos brincar com o {dog1.nome} então?")
    
    
    #PetShop
    while True:
        resposta = int(input("\nDigite 1 para dar a patinha, 2 para ele latir ou 0 para os dois: "))
        while True:
            if resposta == 0:
                pessoa.treinar()
                break
            elif resposta == 1:
                dog1.daApatinha()
                break
            elif resposta == 2:
                dog1.latir()
                break
            else:
                print("ERRO! Digite um escolha válida!")
            
        while True:
            cont = str(input("\nQuer continuar? ").strip().lower())[0]
            if cont != "n" and cont != "s":
                print("ERRO! Digite um sim ou não.")
            else:
                break
                        
        if cont == "n":
            break
    
    cadastro(pessoa, contador)
       
    while True:
        proximo = str(input("\nQuer cadastrar outra pessoa? ").strip().lower())[0] 
        if proximo != "n" and proximo != "s":
            print("ERRO! Digite um sim ou não.")
        else:
            break
                 
                        
    if proximo == "n":
        break
  
  
      
print("\nCadastros efetuados:")
for c in pessoas:
    print(pessoas[c].nome)
    
    
acesso = int(input("\nDigite o número do seu cadastro para acessar seus dados:"))

print(f'\nNome: {pessoas[f"pessoa{acesso}"].nome}')
print(f'Idade: {pessoas[f"pessoa{acesso}"].idade}')
print(f'Nome do Cachorro: {pessoas[f"pessoa{acesso}"].cao.nome}')
print(f'Cor do Cachorro: {pessoas[f"pessoa{acesso}"].cao.cor}')
        