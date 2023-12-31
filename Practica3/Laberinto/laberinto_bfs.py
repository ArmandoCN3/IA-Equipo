from collections import deque
import time

def solve_maze(maze, start, end):
    queue = deque([(start, [start])])
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return True, path

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    queue.append(((nx, ny), path + [(nx, ny)]))
                    if maze[nx][ny] != 'E':
                        maze[nx][ny] = '2'

    return False, []

if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end
    
    maze = [ #maze con solución 20x50
    # 0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['S', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0'],
    ['1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
    ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1', '0', '0', '1'],
    ['1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1'],
    ['1', '0', '0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '0'],
    ['1', '1', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1'],
    ['1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '1', '1', '0', '1', '1', '0', '1', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '0', '1'],
    ['0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'E', '1']
    ]
    start = (1, 0)
    end = (20, 48)
    
    time_start = time.time()
    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")
    time_end = time.time()
    print(f"\nTiempo de ejecución: {time_end-time_start} ")
