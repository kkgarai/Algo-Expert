"""
Number of Islands


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:
    @staticmethod
    def numIslands(self, grid: List[List[str]]) -> int:
        def sinkIsland(grid, r, c):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]):
                return
            if grid[r][c] == "1":
                grid[r][c] = "0"
            else:
                return
            sinkIsland(grid, r + 1, c)
            sinkIsland(grid, r, c + 1)
            sinkIsland(grid, r - 1, c)
            sinkIsland(grid, r, c - 1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    sinkIsland(grid, i, j)
        return counter
