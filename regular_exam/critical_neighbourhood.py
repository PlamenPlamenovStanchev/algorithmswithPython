import heapq


def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return path, cost
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in seen:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path))
    return None, None


def main():
    r = int(input())
    graph = {}
    for _ in range(r):
        city1, city2, distance = input().split(' - ')
        distance = int(distance)
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = distance
        graph[city2][city1] = distance

    closed_roads = input().split(',')
    for road in closed_roads:
        city1, city2 = road.split('-')
        if city1 in graph and city2 in graph[city1]:
            del graph[city1][city2]
        if city2 in graph and city1 in graph[city2]:
            del graph[city2][city1]

    start_city = input()
    end_city = input()

    path, cost = dijkstra(graph, start_city, end_city)

    if path:
        print(' - '.join(path))
        print(cost)
    else:
        print("No path found")


if __name__ == "__main__":
    main()

