import random

def generate_linear_system(n, min_val=-10, max_val=10):
    
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    
    x = [i+1 for i in range(n)]
    
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    
    return A, b, x

def forward_elimination(A, b):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
        
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
        
        print(f"\nStep {i+1}:")
        for row in A:
            print(row)
        print("b:", b)

def backward_substitution(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

n = 3 
A, b, x_true = generate_linear_system(n)

print("Matrix A:")
for row in A:
    print(row)
print("\nRight-hand side b:", b)

forward_elimination(A, b)

x_solution = backward_substitution(A, b)
print("\nComputed solution x:", x_solution)