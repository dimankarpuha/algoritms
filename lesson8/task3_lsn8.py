# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

graph = [
    [1, 2],
    [0, 4],
    [0, 3, 5],
    [2, 4],
    [1, 3],
    [2]
]

def dfs(graph, start, finish):
    is_visited = [None] * len(graph)  #список посещенных
    path = []  #список для пути

    def _dfs(current):
        is_visited[current] = True   #в список посещенных добавляем текущую вершину
        path.append(current)   # в список путь добавляем текущую вершину
        for vertex in graph[current]:   #проходим по списку вершин инцедентных данной вершине
            if not is_visited[vertex] and not is_visited[finish]:   #если вершина не посещенная и не финишн то
                _dfs(vertex)                                        #рекурсивно вызываем функцию
        if not is_visited[finish]:   # после того как обошли все вершины инцендентых текущей вершине и при этом
                                     # мы не дошли до финиша, значит это тупиковая вершина и ее удаляем из пути
            path.remove(current)

    _dfs(start)

    return path

start = 1
finish = 4
print(f'Graph: {graph}')
print(f'Start: {start}, finish {finish}')
print('Path from start to finish:',dfs(graph, start, finish))
