from collections import deque

dirs = [(0,1),(1,1),(1,0),(1,-1),(-1,0),(-1,-1),(-1,0),(-1,1)]
def get_clear_neighbors(i, j, n, grid):
  neighbors = []
  for row, col in dirs:
    ii, jj = i+row, j+col
    if ii >=0 and jj >= 0 and ii < n and jj < n:
      if grid[ii][jj] == 0:
        neighbors.append((ii, jj))
  return neighbors

def shortestPathBinaryMatrix(grid):
  visited = set()
  n = len(grid)
  q = deque([(0, 0, 0)]) 
  minPathLen = float('inf')
  while q:
    row, col, level = q.popleft()
    visited.add((row, col))
    for ii, jj in get_clear_neighbors(row, col, n, grid):
      if (ii, jj) not in visited:
        q.append((ii, jj, level+1))

      if ii==n-1 and jj==n-1:
        if minPathLen > level+1:
          minPathLen = level+1

  return minPathLen

grid = [[0,1],[1,0]]
print(shortestPathBinaryMatrix(grid))
