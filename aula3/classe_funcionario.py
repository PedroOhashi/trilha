class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        print(f"Salario base é {self.salario_base}")

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus_fixo):

        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        resultado = self.salario_base + self.bonus_fixo
        print(f"O salario do gerente é: {resultado}")

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, quantidade_vendas, preco_por_venda):

        super().__init__(nome, salario_base)
        self.quantidade_vendas = quantidade_vendas
        self.preco_por_venda = preco_por_venda

    def calcular_salario(self):
        resultado = self.salario_base + (self.quantidade_vendas * self.preco_por_venda)    
        print(f"O salario do Vendedor é: {resultado}")

funcionario1 = Funcionario("Gerente", 1200)
funcionario1.calcular_salario()

gerente1 = Gerente("pedro", 1200, 40)
gerente1.calcular_salario()

vendedor1 = Vendedor("Otavio", 1200, 40, 100)
vendedor1.calcular_salario()