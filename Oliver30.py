import numpy as np
import random

class Cidades:
    def __init__(self, arquivo):
        """Inicializa a classe Cidades carregando a matriz de distâncias do arquivo."""
        self.matriz_distancias = self.carregar_matriz(arquivo)
        self.num_cidades = len(self.matriz_distancias)

    def carregar_matriz(self, arquivo):
        """Carrega a matriz de distâncias do arquivo."""
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            distancias = []
            for linha in linhas:
                distancias_linha = [float(x) for x in linha.split(',')]
                distancias.append(distancias_linha)
        return np.array(distancias)

class AntColonySystem:
    def __init__(self, cidades, num_ants, num_iterations, alpha=1.0, beta=2.0, rho=0.1, Q=100.0, q0=0.9):
        self.cidades = cidades
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha  # Peso do feromônio
        self.beta = beta    # Peso da heurística
        self.rho = rho      # Taxa de evaporação
        self.Q = Q          # Constante para atualização global do feromônio
        self.q0 = q0        # Probabilidade de escolha da regra de transição
        self.num_cities = cidades.num_cidades
        self.distances = cidades.matriz_distancias
        self.pheromones = np.ones((self.num_cities, self.num_cities))
        self.best_tour = None
        self.best_tour_length = float('inf')

    def initialize_pheromones(self):
        self.pheromones = np.ones((self.num_cities, self.num_cities))
    
    def choose_next_city(self, current_city, unvisited_cities):
        q = random.random()
        if q <= self.q0:
            # Escolha a cidade com o maior valor de τ_ij * η_ij
            max_product = -1
            next_city = -1
            for city in unvisited_cities:
                pheromone = self.pheromones[current_city][city]
                heuristic = 1 / self.distances[current_city][city]
                product = pheromone ** self.alpha * heuristic ** self.beta
                if product > max_product:
                    max_product = product
                    next_city = city
            return next_city
        else:
            # Escolha a próxima cidade com base na distribuição de probabilidade
            probabilities = []
            pheromone_values = self.pheromones[current_city, unvisited_cities]
            heuristic_values = 1 / self.distances[current_city, unvisited_cities]
            total_sum = np.sum(pheromone_values ** self.alpha * heuristic_values ** self.beta)

            for city in unvisited_cities:
                pheromone = self.pheromones[current_city][city]
                heuristic = 1 / self.distances[current_city][city]
                probabilities.append((pheromone ** self.alpha) * (heuristic ** self.beta) / total_sum)

            return random.choices(unvisited_cities, weights=probabilities, k=1)[0]

    def local_pheromone_update(self, city_i, city_j):
        self.pheromones[city_i][city_j] = (1 - self.rho) * self.pheromones[city_i][city_j] + self.rho * (1 / self.distances[city_i][city_j])

    def global_pheromone_update(self, tours):
        # Evaporação global do feromônio
        self.pheromones *= (1 - self.rho)
        
        # Reforço do melhor tour encontrado nesta iteração
        for tour in tours:
            tour_length = self.calculate_tour_length(tour)
            for i in range(len(tour) - 1):
                city_i = tour[i]
                city_j = tour[i + 1]
                self.pheromones[city_i][city_j] += self.Q / tour_length

    def calculate_tour_length(self, tour):
        return sum(self.distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    def run(self):
        self.initialize_pheromones()

        for iteration in range(self.num_iterations):
            tours = []
            for ant in range(self.num_ants):
                unvisited_cities = list(range(self.num_cities))
                current_city = random.choice(unvisited_cities)
                tour = [current_city]
                unvisited_cities.remove(current_city)

                while unvisited_cities:
                    next_city = self.choose_next_city(current_city, unvisited_cities)
                    tour.append(next_city)
                    unvisited_cities.remove(next_city)
                    self.local_pheromone_update(current_city, next_city)
                    current_city = next_city

                tour.append(tour[0])  # Retorna à cidade inicial
                
                # Aplicar uma heurística de otimização local como 2-opt aqui
                tour = self.two_opt(tour)
                
                tour_length = self.calculate_tour_length(tour)
                tours.append(tour)

                # Exibir geração, formiga, caminho e comprimento do tour para a formiga atual
                caminho = " -> ".join(map(str, tour))
                print(f"Geração {iteration + 1}: Formiga {ant + 1}: Caminho = [{caminho}], Comprimento = {tour_length:.2f}")

            # Atualizar feromônios globalmente
            self.global_pheromone_update(tours)

            # Verificar se encontramos uma melhor solução
            for tour in tours:
                tour_length = self.calculate_tour_length(tour)
                if tour_length < self.best_tour_length:
                    self.best_tour_length = tour_length
                    self.best_tour = tour

            print(f"Melhor comprimento do tour após a Geração {iteration + 1}: {self.best_tour_length:.2f}")

        return self.best_tour, self.best_tour_length

    def two_opt(self, tour):
        """Aprimoramento local usando o algoritmo 2-opt."""
        best = tour
        improved = True
        while improved:
            improved = False
            for i in range(1, len(tour) - 2):
                for j in range(i + 1, len(tour)):
                    if j - i == 1: continue
                    new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                    if self.calculate_tour_length(new_tour) < self.calculate_tour_length(best):
                        best = new_tour
                        improved = True
            tour = best
        return best

# Exemplo de uso
arquivo_matriz = 'Matrizes/Oliver30.DAT'
cidades = Cidades(arquivo_matriz)

acs = AntColonySystem(cidades, num_ants=30, num_iterations=100)
best_tour, best_tour_length = acs.run()
print("\nMelhor caminho encontrado:", "[" + " - ".join(map(str, best_tour)) + "]")
print("Comprimento do melhor caminho: {:.2f}".format(best_tour_length))