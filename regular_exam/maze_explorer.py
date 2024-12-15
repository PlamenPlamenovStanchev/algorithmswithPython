from collections import deque


def find_shortest_path(maze):
    n = len(maze)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    start = None
    end = None

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    queue.append((start, 0))
    visited = set([start])

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < n and
                maze[nx][ny] != '#' and (nx, ny) not in visited):
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

    return -1


n = int(input())
maze = [input().strip() for _ in range(n)]
print(find_shortest_path(maze))
