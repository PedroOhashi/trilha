class Livro:
    def __init__(self, titulo, autor, paginas, paginas_lidas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, quantidade):
        if self.paginas_lidas + quantidade > self.paginas:
            print(f"Quantidade invalida, o livro tem apenas {self.paginas} paginas")
            return
        
        self.paginas_lidas += quantidade
        print(f"Voce ja leu {self.paginas_lidas} paginas")

    def progresso(self):
        porcentagem = (self.paginas_lidas / self.paginas) * 100
        print(f"Voce leu no total {porcentagem}% do livro")


livro1 = Livro("Livro 1", "autor 1", 100, 0)

livro1.ler(2)
livro1.progresso()

livro2 = Livro("Livro 2", "autor 2", 500, 24)

livro2.progresso()