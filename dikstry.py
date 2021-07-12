import math


def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

N = len(D)  # число вершин в графе
T = [math.inf] * N  # последняя строка таблицы

v = 0  # стартовая вершина (нумерация с нуля)
S = {v}  # просмотренные вершины
T[v] = 0  # нулевой вес для стартовой вершины
M = [0] * N  # оптимальные связи между вершинами

while v != -1:  # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(D[v]):  # перебираем все связанные вершины с вершиной v
        if j not in S:  # если вершина еще не просмотрена
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                M[j] = v  # связываем вершину j с вершиной v

    v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
    if v >= 0:  # выбрана очередная вершина
        S.add(v)  # добавляем новую вершину в рассмотрение

print(T, M, sep="\n")

# формирование оптимального маршрута:
start = 0
end = 4
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print(P)



# Another realization

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {}
graph["start"] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs['fin'])