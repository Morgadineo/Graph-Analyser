"""
    d) Implementar uma rotina que receba um grafo DIRECIONADO qualquer e: 
        a. [X] Represente o mesmo através da matriz de adjacência E Lista de adjacência
        b. [ ] Informe se o grafo é uma arvore, se for, informe o tipo
        c. [X] Informe o grau de cada vértice
        d. [X] Informe o grau o grafo
        e. [x] Informe se o grafo é completo
        f. [X] Informe se o grafo possui laços
        g. [x] Informe se é um grafo simples
        h. [X] Imprima a matriz/lista de adjacência
        i. [X] Verificar se o grafo é simétrico, assimétrico / não simétrico

"""

class Graph:

    def __init__(self, graph: dict[str, str]):
        # Representações
        self.graph: dict[str, str] = graph       # graph é equivalente a lista de adjacência.

        # Atributos adicionais
        self.vertices: list[str] = [vertice for vertice in self.graph.keys()] # Lista de vertices
        self.vertices_qtt: int   = len(self.vertices)                         # Quantidade de vértices
        self.edges_qtt: int      = self.count_edges()                         # Quantidade de arestas
        
        # Atributos de verificação
        self.has_loop    : bool = self.verify_loop()
        self.has_parallel: bool = self.verify_parallel()
       
        # Se has_loop ou has_parallel forem verdadeiros, o grafo não é simples/completo.
        self.its_simple   : bool = self.verify_simplicity()
        
        # Contagem dos graus de entrada e saída de cada vértice.
        self.vertices_out_degree: list[int] = self.count_vertices_out_degree()
        self.vertices_in_degree : list[int]  = self.count_vertices_in_degree()
        
        # Contagem de graus de entrada e saída do grafo.
        self.graph_out_degree: int = self.count_graph_out_degree()
        self.graph_in_degree : int  = self.count_graph_in_degree()

        # Matriz de adjacência
        self.adjacency_matrix: list[int] = self.create_adjacency_matrix()
        
        self.print_adjancency_matrix()

        # Caracteristicas do Digrafo
        self.its_simetry           : bool = self.verify_simetry()
        self.its_assimetry         : bool = self.verify_assimetry() 
        self.its_complete          : bool = self.verify_completeness()
        self.its_complete_simetry  : bool = self.its_complete and self.its_simetry
        self.its_complete_assimetry: bool = self.its_complete and self.its_assimetry
        
        self.its_balanced          : bool = self.verify_balancing()
        # self.its_connected         : bool = self.verify_connectivity()
        
    def verify_balancing(self) -> bool:
        """
        Verify if the digraph is balanced.
        A digraph is balanced if every vertice has the same out and in degree.

        return:
            A boolean value. True: if the digraph is balance; False: if is not.
        """
        for i in range(self.vertices_qtt):
            if (self.vertices_in_degree[i] != self.vertices_out_degree[i]):
                return False
            
        return True

    def verify_completeness(self) -> bool:
        """
        Verify if the digraph is complete.
        A complete digraph is a simple digraph where every vertice has at least one edge with all the other.

        return:
            A boolean value. True: If the graph is complete; False: if is not.
        """
        has_edge: bool = False
        if self.its_simple:
            for i in range(self.vertices_qtt):
                has_edge = False
                for j in range(self.vertices_qtt):
                    if i != j:
                        if (self.adjacency_matrix[j][i] or self.adjacency_matrix[i][j]):
                            has_edge = True
            if not has_edge:
                return False
            else:
                return True
        else:
            return False

    def verify_assimetry(self) -> bool:
        """
        Verify if the digraph is assimetry.
        A digraph is a assimetry digraph if have at most one arc direction between two vertices.


        return:
            A boolean value. True: if is assimetry; False: if is not.
        """
        if not (self.its_simetry):
            for i in range(self.vertices_qtt):
                for j in range(self.vertices_qtt):
                    if i != j: # Se não estiver na diagonal principal:
                        if (self.adjacency_matrix[j][i]) and (self.adjacency_matrix[i][j]):
                            return False
            return True
        return False

    def verify_simetry(self) -> bool:
        """
        Verify if the digraph is simetry.
        A digraph is a simetry digraph if for every arc(a, b) exist a arc(b, c).

        return:
            A boolean value. True: the digraph is simetry; False: it is not.
        """
        for i in range(self.vertices_qtt):
            for j in range(self.vertices_qtt):
                if i != j: # Se não estiver na diagonal principal
                    # Se existir uma aresta entre (i, j) e não tiver uma entre (j, i)
                    if (self.adjacency_matrix[i][j]) and (not (self.adjacency_matrix[j][i])):
                        return False # Não é simétrica
        return True # Não tenhuma que liga (i, j) e não liga (j, i) -> é simétrica.

    def verify_is_tree(self) -> bool:
        """
        Identify if the graph is a tree.
        To identify, is verify if the graph is simple, and if is, verify if the
        number of edges are the number of vertices minus one.

        return:
            A boolean value. True: the graph is a tree; False is not.
        """
        if self.its_simple:
            if self.edges_qtt == (self.vertices_qtt) - 1:
                return True
        else:
            return False
>>>>>>> 610f642 (Mega update)

    def print_adjancency_matrix(self) -> None:

        for vertice in range(self.vertices_qtt):
            print(f"  {self.vertices[vertice]}", end="")

        print("\n")

        for vertice in range(self.vertices_qtt):
            print(f"{self.vertices[vertice]}", end="")

            for edge in range(self.vertices_qtt):
                print(f" {self.adjacency_matrix[vertice][edge]} ", end="")
            print("\n")

    def create_adjacency_matrix(self) -> list[list[int]]:
        """
        Create the adjancency matrix of the graph.

        returns:
            The adjancency matrix of the graph. 
        """
        adjancency_matrix = self.__initialize_adjancy_matrix__() # Inicializa a matriz com 0s

        for i, vertice in enumerate(self.vertices):
            for edge in self.graph[vertice]:
                adjancency_matrix[i][self.vertices.index(edge)] += 1

        return adjancency_matrix

    def __initialize_adjancy_matrix__(self):
        """
        Create and return a adjacency matrix [vertices][vertices]

        return:
            The matrix full with 0 with [vertices][vertices] with only 0.
        """
        # Esta "list comprehension" inicializa uma matrix de 0s.
        # Pode-se escrever utilizando estruturas de repetição também.
        adjacency_matrix: list[list[int]] = [[0 for i in range(self.vertices_qtt)] 
                                              for j in range(self.vertices_qtt)]
        
        return adjacency_matrix



    def count_graph_in_degree(self) -> int:
        """
        Count the total graph in degree.

        return:
            The graph in degree.
        """
        total = 0
        for i in range(self.vertices_qtt):
            total += self.vertices_in_degree[i]

        return total

    def count_graph_out_degree(self) -> int:
        """
        Count the total graph out degree.

        return:
            The graph out degree.
        """
        total = 0
        for i in range(self.vertices_qtt):
            total += self.vertices_out_degree[i]

        return total

    def print_vertices_degrees(self) -> None:
        """
        Print the vertices in and out degree.
        """
        for i, vertice in enumerate(self.vertices):
           print(f"{vertice} -> {self.vertices_out_degree[i]}\n{vertice} <- {self.vertices_in_degree[i]}\n") 

    

    def count_vertices_in_degree(self) -> list[int]:
        """
        Count the in degree of all vertices present in the graph.

        return:
            A list of ints.
        """
        degree_list: list[int] = []
        
        for vertice in self.vertices:
            ocurrency = 0
            for adjancency in self.graph.values():
                ocurrency += adjancency.count(vertice)
            
            degree_list.append(ocurrency)

        return degree_list

    def count_vertices_out_degree(self) -> list[int]:
        """
        Count the out degree of all vertices present in the graph.

        return:
            A list of ints. Degree[0] is referent to graph.keys()[0].
        """
        degree_list: list[int] = []
        
        for vertice in self.vertices:
            degree_list.append(len(self.graph[vertice]))

        return degree_list
                

    def print_adjancency_list(self) -> None:
        """
        Print the adjancency list of the graph in the format:
        {vertice1}: {v1}, {v2}, {v3}, ...
        {vertice2}: {v1}, {v2}, {v3}, ...
        """
        for vertice in self.vertices:
            print(f"{vertice}: ", end="")
            for i, adj_vertice in enumerate(self.graph[vertice]):
                if i == (len(self.graph[vertice]) - 1):
                    print(adj_vertice)
                else:
                    print(f"{adj_vertice}, ", end="")

    def verify_simplicity(self) -> bool:
        """
        Verify if the graph is simple.
        A simples graph is a graph that doesnt have laces or parallel edges.

        Returns:
            True if is simple and False if complex
        """

        if self.has_loop or self.has_parallel:
            return False
        else:
            return True

    def verify_parallel(self) -> bool:
        """
        Verify if the graph has paralell edges.
        
        Returns:
            True if have a parallel edge and False if not.
        """
        values = self.graph.values()
        for adjacent in values:
            if len(set(adjacent)) != len(adjacent):
                return True
        return False

    def verify_loop(self) -> bool:
        """
        Verify if the graph has a loop/lace edge.

        Returns:
            True if have a loop edge and False if not.
        """
        for vertice in self.vertices:
            if vertice in self.graph[vertice]:
                return True
        return False

    def count_edges(self) -> int:
        """
        Count the numbers of edges present in the graph using the adjacency list.

        return:
            int number of edges.
        """
        edges_qtt = 0

        for adjacency in self.graph.values():
            edges_qtt += len(adjacency)

        return edges_qtt

def create_graph() -> dict[str: list[str]]:
    """
    Function to create a adjancency list of a graph.
        1º Input the number of vertices.
        2º Input the vertice name. Example: A
        3º Input the vertices to create a edge with. Example: A B C
    
    return:
        A dict {vertice: [v1, v2, v3]} with the vertice as key and a list of edges as value. 
    """
    number_vertices: int = int(input("Quantos vértices terá? "))
    adjacency_list = {} 
    for vertice in range(number_vertices):
        vertice = input("Vertice: ")
        edges   = input("Arestas: ")
         
        edges = edges.split(' ')
        print('\n')

        adjacency_list.update({vertice: edges})
    return adjacency_list

if __name__ == '__main__':
    # Representação de um grafo:
    # {'Vértice': ['array de vértices conectados']}
    # Caso o vértice não possua conexões, fica:
    # {'Vértice': []}
    graph = Graph(create_graph())

