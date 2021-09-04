import random


class Sala():
    def __init__(self, sala_largura, sala_comprimento, porta, tablado):
        self.sala_largura = sala_largura
        self.sala_comprimento = sala_comprimento
        self.porta = porta
        self.tablado = tablado
        self.sala_modelo_matriz = []
        self.sala_random_matriz = []

    def cria_sala(self):
        for i in range(sala_comprimento):
            self.sala_modelo_matriz += [[0]*sala_largura]

    def aloca_tablado(self):
        if self.tablado == 1:
            for item in range(sala_largura):
                self.sala_modelo_matriz[0][item] = 9

        elif self.tablado == 2:
            for item in range(sala_largura):
                self.sala_modelo_matriz[sala_comprimento-1][item] = 9

        elif self.tablado == 3:
            for item in range(sala_comprimento):
                self.sala_modelo_matriz[item][0] = 9

        elif self.tablado == 4:
            for item in range(sala_comprimento):
                self.sala_modelo_matriz[item][sala_largura-1] = 9

    def aloca_porta(self):
        if self.porta == 1:
            self.sala_modelo_matriz[0][0] = 9

        elif self.porta == 2:
            self.sala_modelo_matriz[0][sala_largura-1] = 9

        elif self.porta == 3:
            self.sala_modelo_matriz[sala_comprimento-1][0] = 9

        elif self.porta == 4:
            self.sala_modelo_matriz[sala_comprimento-1][sala_largura-1] = 9
    
    def aloca_alunos(self):
        for linha in range(0, sala_comprimento, 2):
            for coluna in range(0, sala_largura, 2):
                if self.sala_modelo_matriz[linha][coluna] != 9:
                    self.sala_modelo_matriz[linha][coluna] = 1

    def cria_sala_aleatoria(self, min, max):
        for i in range(sala_comprimento):
            self.sala_random_matriz += [[0]*sala_largura]

        for linha in range(sala_comprimento):
            for coluna in range(sala_largura):
                    self.sala_random_matriz[linha][coluna] = random.randint(min, max)

    def mostra_matriz(self):
        print("Mostrando sala modelo...\n")
        for i in range(sala_comprimento):
            print(self.sala_modelo_matriz[i])

        print("\nMostrando população criada...\n")
        for j in range(sala_comprimento):
            print(self.sala_random_matriz[j])


class AlgoritmoGenetico():
    def __init__(self, sala_comprimento, sala_largura, sala_modelo_matriz, sala_random_matriz):
        self.sala_comprimento = sala_comprimento
        self.sala_largura = sala_largura
        self.fitness = 0
        self.populacao = sala_random_matriz
        self.população_modelo = sala_modelo_matriz

    def fitness_func(self):
        for l in range(self.sala_comprimento-1):
            for c in range(self.sala_largura-1):
                if (self.população[l][c] == self.população_modelo[l][c]):
                    self.fitness += 1
            return self.fitness

    def crossover(self):
        pass

    def mutacao(self):
        pass
    

print("\n\n------------- Startando Algoritmo Genético... -------------\n\n")

print("------------- Coletando dados sobre a população... -------------")

print("\nDigite a largura da sala em metros:")
sala_largura = int(input())

print("Digite o comprimento da sala em metros:")
sala_comprimento = int(input())

print("1 - Porta no local superior esquerdo:\n2 - Porta no local superior direito:\n"
        + "3 - Porta no local inferior esquerdo:\n4 - Porta no local inferior direito:\n")
porta = int(input())

print("1 - tablado na extremidade superior:\n2 - tablado na extremidade inferior\n"
        + "3 - tablado na extremidade esquerda:\n4 - tablado na extremidade direita:\n")
tablado = int(input())


sala = Sala(sala_largura, sala_comprimento, porta, tablado)
sala.cria_sala()
sala.aloca_tablado()
sala.aloca_porta()
sala.aloca_alunos()
print("Digite o valor mínimo para criação da populção:")
min = int(input())
print("Digite o valor máximo para criação da populção:")
max = int(input())

print("Criando população...\n")
sala.cria_sala_aleatoria(min, max)

sala.mostra_matriz()




