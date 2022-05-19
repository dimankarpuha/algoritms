# 1. На улице встретились N друзей. Каждый пожал руку всем остальным
# друзьям (по одному разу). Сколько рукопожатий было?
def dfs(graph):
    is_visited = [None] * len(graph)  #список посещенных
    path = []  #список для пути
    count_edge = []
    def _dfs(current):
        is_visited[current] = True   #в список посещенных добавляем текущую вершину
        path.append(current)   # в список путь добавляем текущую вершину
        for vertex in graph[current]:   #проходим по списку вершин инцедентных данной вершине
            if not is_visited[vertex]:
                _dfs(vertex)
            count_edge.append(1) # считаем рукопожатия, в конце делим на два т.к. граф не направленный
    _dfs(0)
    return path, len(count_edge) // 2


def make_graph(N):
    graph = []
    for row in range(N):
        graph.append([num for num in range(N) if num != row])
    return graph

N = 10

graph = make_graph(N)
print(graph)
print('Друзей:', dfs(graph)[0])
print('Рукопожатий:', dfs(graph)[1])
