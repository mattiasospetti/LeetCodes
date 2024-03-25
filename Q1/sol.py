# The proposed solution uses a BFS (breath-first search: https://en.wikipedia.org/wiki/Breadth-first_search)
# the idea is to start with a distances matrix with all 'inf' values then update with respect to zeros positions

#complexity: O(mxn), m=rows number, n=columns number

from collections import deque

def nearestZeroDistance(mat):
    if not mat:
        return mat
    
    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #steps
    queue = deque()
    
    # Initialization:

    # Distances matrix initialization (you may prefer sys.maxint instead of 'inf')
    distances = [[float('inf') for _ in range(n)] for _ in range(m)]
    
    # first matrix update --> queue first elems (the zeros we'll encounter)
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                queue.append((i, j))
                distances[i][j] = 0
    
    # BFS
    while queue:
        x, y = queue.popleft()
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y #follow directions and create new coordinates (we'll look for adjacent cells)
            if new_x>=0 and new_y>=0 and new_x< m and new_y<n \
            and distances[new_x][new_y]>distances[x][y]+1:  # we are checking if the new coords are compatible with the matrix dims,
                                                            # then we are checking if the current distance value with the adjacent (new_x,new_y)
                                                            # is greater than the expected,
                                                            # if so, we are going to update the distances matrix with the current minimum value,
                                                            # which is the current distance+1 (due to the new step we made) --> seems reasonable, isn't it?
                distances[new_x][new_y] = distances[x][y] + 1
                queue.append((new_x, new_y)) #we will have to check the new node (as BFS algorithm suggests) , so we add the new node to the queue
    
    return distances

# Example usage:
mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]
result = nearestZeroDistance(mat)
print(f'results for {mat}')
for row in result:
    print(row)