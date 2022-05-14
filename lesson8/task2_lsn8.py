# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
g = [
    [0, 1, 3, 5, 0],
    [1, 0, 0, 0, 4],
    [3, 0, 0, 0, 3],
    [5, 0, 0, 0, 2],
    [0, 4, 3, 2, 0]
]

def deikstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length  # добавляем список парентс
    min_cost = 0
    cost[start] = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start   # если изменяем вершину то пишем ей родителя

        min_cost = float('inf')

        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, parent

def find_path(g, parents, start):
    path = [[] for _ in g]
    def _find_path(i, current):
        if parents[current] != -1:
            path[i].append(parents[current])   # пишем вершину в путь если она не равна -1
        if parents[current] != start and parents[current] != -1:   # если это не старт то рекурсивно вызываем
            _find_path(i, parents[current])

    for i in range(len(parents)):   #  просто по очереди закидываем вершины до которых хоти добраться
        path[i].append(i)
        _find_path(i, i)

    return path

start = 3
cost, parents = deikstra(g, start)

print('Стоимость до вершины', cost)
print(parents)
print('Путь от каждой вершины до старта', find_path(g, parents, start))
