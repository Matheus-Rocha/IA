import random


pop_tamanho = input(print("Digite o tamanho da população:  \n"))
matriz_cromossomo = input(print("Digite numero de cromossomos:  \n"))
tipo_de_população = input(print("Digite população:  \n"))
limite_cromossomos = input(print("Digite limite de cromossomos:  \n"))
tamanho_cromossomo = input(print("Digite nCrom:  \n"))

items = []
population = []
model_population = []

def item(min, max):
    for i in range(tamanho_cromossomo):
        items.append(random.randint(min, max))


def create_population():
    for i in range(len(items)):
        population.append(item(0,9))


def funcao_fitness(items):
    fitness = 0
    for i in range(len(items)):
        if (items[i] == model_population[i]):
            fitness += 1
    return fitness


#Algoritmo do pdf da aula:
def newpop(nInd, nCrom):
    for i in range(1, nInd):
        for j in range(1, nCrom):
            inf = [j][1]
            sup = [j][2]
            newpop[i, j] = random.randint(1, 1000)*(sup - inf) + inf


def cod(nInd, nCrom, CromLim, lbits, pop):
    for i in range(1, nInd):
        for j in range(1, nCrom):
            inf = CromLim[j][1]
        sup = CromLim[j][2]
        aux = ((pop[i][j] - inf) / (sup - inf)) * (2^lbits[j] - 1)
        # passar aux para binario
