"""
    d) Implementar uma rotina que receba um grafo DIRECIONADO qualquer e: 
        a. [ ] [X] Represente o mesmo através da matriz de adjacência E Lista de adjacência
        b. [ ] Informe se o grafo é uma arvore, se for, informe o tipo
        c. [X] Informe o grau de cada vértice
        d. [X] Informe o grau o grafo
        e. [X] Informe se o grafo é completo
        f. [X] Informe se o grafo possui laços
        g. [X] Informe se é um grafo simples
        h. [ ] Imprima a matriz/lista de adjacência

"""


class Graph:

    def __init__(self, graph: dict[str, str]):
        # Representações
        self.graph: dict[str, str] = graph       # graph é equivalente a lista de adjacência.
        self.adjacency_matrix: list[int] = None

        # Atributos adicionais
        self.vertices_qtt: int = len(self.graph.keys()) # Quantidade de vértices
        self.edges_qtt: int    = self.count_edges()     # Quantidade de arestas

        # Atributos de verificações
        # 1º verifica se tem loop e aresta paralela
        self.has_loop: bool     = self.verify_loop()
        self.has_parallel: bool = self.verify_parallel()
       
        # Se has_loop ou has_parallel forem verdadeiros, o grafo não é simples/completo.
        self.its_simple: bool   = self.verify_simplicity()
        self.its_complete: bool = self.verify_completeness()
        self.its_tree: bool     = True  # Considera que é uma até não ser.
        
        # Contagem dos graus de entrada e saída de cada vértice.
        self.vertices_out_degree: list[int] = self.count_vertices_out_degree()
        self.vertices_in_degree: list[int]  = self.count_vertices_in_degree()

        self.graph_out_degree: int = self.count_graph_out_degree()
        self.graph_in_degree: int  = self.count_graph_in_degree()
        
        print(f'{self.graph_in_degree} | {self.graph_out_degree}')

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
        for i, vertice in enumerate(self.graph.keys()):
           print(f"{vertice} -> {self.vertices_out_degree[i]}\n{vertice} <- {self.vertices_in_degree[i]}\n") 

    def count_vertices_in_degree(self) -> list[int]:
        """
        Count the in degree of all vertices present in the graph.

        return:
            A list of ints.
        """
        degree_list: list[int] = []
        
        for vertice in self.graph.keys():
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
        
        for vertice in self.graph.keys():
            degree_list.append(len(self.graph[vertice]))

        return degree_list
                

    def print_adjancency_list(self) -> None:
        """
        Print the adjancency list of the graph in the format:
        {vertice1}: {v1}, {v2}, {v3}, ...
        {vertice2}: {v1}, {v2}, {v3}, ...
        """
        for vertice in self.graph.keys():
            print(f"{vertice}: ", end="")
            for i, adj_vertice in enumerate(self.graph[vertice]):
                if i == (len(self.graph[vertice]) - 1):
                    print(adj_vertice)
                else:
                    print(f"{adj_vertice}, ", end="")
         
    def verify_completeness(self) -> bool:
        """
        Verify if the graph is complete or not.
        A complete graph is a graph where all the vertices are connect with the others.

        Returns:
            True if is complete and False if is not.
        """
        if self.its_simple:
            if self.edges_qtt == (self.vertices_qtt * (self.vertices_qtt - 1)):
                return True
        return False

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
        for vertice in self.graph.keys():
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

if __name__ == '__main__':
    # Representação de um grafo:
    # {'Vértice': ['array de vértices conectados']}
    # Caso o vértice não possua conexões, fica:
    # {'Vértice': []}
    graph = Graph({'A': ['B', 'C'], 
                   'B': [],
                   'C': ['B'],
                   'D': ['B', 'B', 'D']})
    

