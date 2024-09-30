# Projeto ACO (Colônia de Formigas)

Este projeto implementa o **algoritmo de Colônia de Formigas** (Ant Colony Optimization - ACO) para otimização de rotas entre cidades, resolvendo o **Problema do Caixeiro Viajante (TSP - Travelling Salesman Problem)**. O ACO é aplicado em dois cenários: `Oliver30.py` com 30 cidades e `Rykel48.py` com 48 cidades, com o objetivo de encontrar a rota mais curta que passa por todas as cidades e retorna à cidade de origem.

## Funcionamento do Algoritmo

O **algoritmo de Colônia de Formigas (ACO)** é inspirado no comportamento das formigas reais na natureza. Formigas artificiais são usadas para explorar diferentes rotas entre cidades, e essas rotas são otimizadas com o tempo através de uma técnica de atualização de feromônios. O objetivo principal do ACO é encontrar o **ótimo global**, que é a solução mais eficiente possível para o problema em questão.

### Ótimo Global

O **ótimo global** refere-se à solução ideal em um espaço de busca, que minimiza (ou maximiza) uma função de custo, como a distância total no problema do Caixeiro Viajante. O ACO tenta equilibrar a **exploração** (tentar novas rotas) e a **exploração** (refinar as rotas promissoras) para se aproximar dessa solução ideal.

### O Problema do Caixeiro Viajante (TSP)

O TSP é um problema clássico de otimização em que um vendedor deve visitar todas as cidades de uma lista exatamente uma vez e, em seguida, retornar à cidade de origem, minimizando a distância total percorrida. No ACO, as formigas constroem rotas entre as cidades e, ao retornar à cidade de origem, o feromônio é atualizado para guiar a busca por melhores soluções.

### Componentes Principais do ACO

1. **Formigas**: As formigas artificiais constroem soluções viáveis para o TSP, visitando todas as cidades e retornando ao ponto de partida.
   
2. **Feromônio**: Após completar uma rota, as formigas depositam feromônio nos caminhos que percorreram. Rotas mais curtas acumulam mais feromônio, o que aumenta a probabilidade de serem seguidas por outras formigas.

3. **Evaporação do Feromônio**: O feromônio evapora com o tempo para evitar que o algoritmo fique preso em soluções subótimas, permitindo a exploração de novas rotas.

4. **Rotas**: As formigas constroem rotas probabilisticamente, favorecendo caminhos com mais feromônio e menores distâncias. O processo é repetido até que o algoritmo encontre uma solução otimizada.

### Processo Geral:
- **Inicialização**: Um número de formigas é distribuído entre as cidades.
- **Construção da Solução**: Cada formiga constrói uma rota completa, escolhendo o próximo destino com base nas trilhas de feromônio e nas distâncias entre as cidades.
- **Atualização do Feromônio**: As trilhas de feromônio são atualizadas ao final de cada iteração, com as melhores rotas recebendo mais feromônio.
- **Repetição**: O processo é repetido até que uma solução aceitável seja encontrada ou o número máximo de iterações seja atingido.

## Estrutura do Código

### 1. Leitor de Arquivos `.txt` para Matrizes de Distâncias

O projeto implementa um **leitor de arquivos `.txt`** que carrega a matriz de distâncias entre cidades para ser utilizada no algoritmo de Colônia de Formigas. A matriz de distâncias, representada como valores separados por vírgulas, é lida de um arquivo e convertida em um array NumPy para facilitar o processamento.


1. ### **Carregamento da Matriz**:
   O arquivo `.txt` contendo a matriz de distâncias é lido linha por linha. Cada linha representa as distâncias de uma cidade para as outras, e essas distâncias são armazenadas em uma matriz bidimensional.

   ```python
   def carregar_matriz(self, arquivo):
       """Carrega a matriz de distâncias do arquivo."""
       with open(arquivo, 'r') as f:
           linhas = f.readlines()
           distancias = []
           for linha in linhas:
               distancias_linha = [float(x) for x in linha.split(',')]
               distancias.append(distancias_linha)
       return np.array(distancias)


2. ### Matrizes de Distâncias
As **matrizes de distâncias** representam o custo (ou a distância) entre cada par de cidades, servindo como base para a construção das rotas pelas formigas.

#### Exemplo de Matriz de Distâncias para Oliver30:
``` [0, 10, 15, 20, ..., 35] [10, 0, 25, 30, ..., 40] [15, 25, 0, 35, ..., 45] [20, 30, 35, 0, ..., 50] ```

Cada valor representa a distância entre duas cidades, que é utilizada para calcular a eficiência das rotas.

3. ### `Oliver30.py`
Este arquivo implementa o ACO para um cenário com **30 cidades**. A matriz de distâncias é específica para estas cidades, e o objetivo é encontrar a rota mais curta que conecta todas elas e retorna à cidade de origem.

#### Funções Principais:
- `iniciar_formigas()`: Inicializa as formigas, colocando-as em cidades aleatórias.
- `movimentar_formigas()`: As formigas seguem as trilhas de feromônio e as distâncias para construir suas rotas.
- `atualizar_feromonio()`: Atualiza as trilhas de feromônio com base nas rotas encontradas.
- `melhorar_solucao()`: Avalia as soluções encontradas e otimiza as rotas.

4. ### `Rykel48.py`
Este arquivo aplica o ACO em um cenário com **48 cidades**, uma versão mais complexa do problema com uma matriz de distâncias maior. O objetivo também é encontrar a rota mais curta entre todas as cidades e retornar à cidade de origem.

#### Funções Principais:
- `calcular_resultados()`: Processa os dados obtidos pela simulação e retorna métricas de desempenho.
- `gerar_grafo()`: Cria o grafo de 48 cidades baseado na matriz de distâncias.
- `exibir_grafo()`: Exibe o grafo, mostrando visualmente as trilhas de feromônio e as conexões entre as cidades.
- `salvar_resultados()`: Salva os resultados da simulação em formato CSV ou gráfico.


## Tecnologias e Bibliotecas Utilizadas

- **Python**: Linguagem de programação principal usada no projeto.
- **NumPy**: Utilizada para operações matemáticas e manipulação de arrays, facilitando o cálculo de distâncias e a gestão de matrizes.
- **Matplotlib**: Usada para a visualização dos resultados, como a exibição dos grafos e as rotas geradas pelo algoritmo.
- **CSV**: Usado para salvar os resultados das simulações, permitindo uma análise posterior dos dados.


## Resultados Esperados

Após rodar as simulações, você verá as soluções otimizadas para as rotas das 30 cidades e 48 cidades, junto com métricas como tempo de execução e eficiência das rotas.



## Referências Bibliográficas

Dorigo, M., & Gambardella, L. M. (1997). Ant Colony System: A Cooperative Learning Approach to the Traveling Salesman Problem. *IEEE Transactions on Evolutionary Computation*, 1(1), 53-66.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/ACO_Project.git