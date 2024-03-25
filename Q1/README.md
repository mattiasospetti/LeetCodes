Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

**EX1**

| 0 | 0 | 0 | \
| 0 | 1 | 0 | \
| 0 | 0 | 0 | 

**Input**: mat=[[0,0,0],[0,1,0],[0,0,0]]

**Output**: mat=[[0,0,0],[0,1,0],[0,0,0]]

**EX2**

| 0 | 0 | 0 | \
| 0 | 1 | 0 | \
| 1 | 1 | 1 | 

**Input**: mat=[[0,0,0],[0,1,0],[1,1,1]]

**Output**: mat=[[0,0,0],[0,1,0],[1,2,1]]

N.B: this time I won't care about constraints, as I assume inputs will respect them.

This is what you'll see as a "starting point":
```
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
```

[Difficulty: Medium]
