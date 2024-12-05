# def s1(grid):
#     rows, cols = len(grid), len(grid[0])
#     word = "XMAS"
#     count = 0
#     dirs = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]

#     def check(x, y, dx, dy):
#         for k in range(len(word)):
#             nx, ny = x + k * dx, y + k * dy
#             if not (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == word[k]):
#                 return False
#         return True

#     for r in range(rows):
#         for c in range(cols):
#             for dx, dy in dirs:
#                 if check(r, c, dx, dy):
#                     count += 1

#     return count

# def s2(grid):
#     rows, cols = len(grid), len(grid[0])
#     count = 0
#     pat = [["M", "A", "S"], ["S", "A", "M"]]

#     def check(x, y):
#         p1 = [grid[x][y], grid[x+1][y+1], grid[x+2][y+2]]
#         p2 = [grid[x][y+2], grid[x+1][y+1], grid[x+2][y]]
#         return p1 in pat and p2 in pat

#     for i in range(rows - 2):
#         for j in range(cols - 2):
#             if check(i, j):
#                 count += 1

#     return count

# with open('input.txt', 'r') as f:
#     grid = [list(l.strip()) for l in f.readlines()]
#     print(s1(grid))
#     print(s2(grid))

s=open("input.txt").read()
q=lambda j:f(j)+f(-j)
n=m=0
for i in range(len(s)):f=lambda j:s[i::j][:4]=="XMAS";n+=q(1)+q(w:=s.find("\n"))+q(w+1)+q(w+2);f=lambda j:s[i-j::j][:3]=="MAS";m+=q(w)*q(w+2)
print(n,m)
