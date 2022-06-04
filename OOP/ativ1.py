class Livro():
    def __init__(self, titulo, pag, cap, preco):
        self.titulo = titulo
        self.pag = pag
        self.cap = cap
        self.preco = preco


    def cadastro():
        print()

    
    def alterarPreco():
        print()



class LivroImpresso(Livro):
    def __init__(self, titulo, pag, cap, preco, peso, dimensao, tipoCapa):
        super().__init__(titulo, pag, cap, preco)
        self.peso = peso
        self.dimensao = dimensao
        self.tipoCapa = tipoCapa 
    

    def comprar():
        print()



class LivroDigital(Livro):
    def __init__(self, titulo, pag, cap, preco, tamanhoArq,formato):
        super().__init__(titulo, pag, cap, preco)
        self.tamanhoArq = tamanhoArq
        self.formato = formato


    def baixar(self):
        print(f"Baixando o livro {self.titulo}.")
        
        
livro1 = LivroDigital("O susto", "234", "20", "120", "280", "pdf")

print(livro1.baixar())
  