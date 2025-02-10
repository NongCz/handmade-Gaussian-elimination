A = [
    [1, 1, 1, 6],    
    [3, 2, 1, 10],   
    [2, -1, 4, 12]   
]

factor = A[1][0] / A[0][0]
for j in range(4):
    A[1][j] -= factor * A[0][j]

factor = A[2][0] / A[0][0]
for j in range(4):
    A[2][j] -= factor * A[0][j]

factor = A[2][1] / A[1][1]
for j in range(4):
    A[2][j] -= factor * A[1][j]

x3 = A[2][3] / A[2][2]
x2 = (A[1][3] - A[1][2] * x3) / A[1][1]
x1 = (A[0][3] - A[0][1] * x2 - A[0][2] * x3) / A[0][0]

print(f"Solution: x1 = {x1}, x2 = {x2}, x3 = {x3}")
