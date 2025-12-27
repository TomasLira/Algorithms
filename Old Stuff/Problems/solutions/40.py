from collections import deque
def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0
    time_rotten = -1

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))  
            elif grid[i][j] == 1:
                fresh_oranges += 1  

    if fresh_oranges == 0:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2 
                    fresh_oranges -= 1  
                    queue.append((nx, ny)) 
        time_rotten += 1
    return -1 if fresh_oranges > 0 else time_rotten
