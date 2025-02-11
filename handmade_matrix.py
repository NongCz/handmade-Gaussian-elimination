import random

def generate_linear_system(n, min_val=-10, max_val=10):
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    x = [i+1 for i in range(n)]
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return A, b, x

def generate_hilbert_system(n):
    A = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
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

def backward_substitution(A, b):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

def compute_residual(A, x, b):
    n = len(A)
    residual = [sum(A[i][j] * x[j] for j in range(n)) - b[i] for i in range(n)]
    return residual

def test_solution(n, use_hilbert=False):
    if use_hilbert:
        A, b, x_true = generate_hilbert_system(n)
        print(f"\nTesting Hilbert system of size {n}:")
    else:
        A, b, x_true = generate_linear_system(n)
        print(f"\nTesting random system of size {n}:")
    
    forward_elimination(A, b)
    x_solution = backward_substitution(A, b)
    residual = compute_residual(A, x_solution, b)
    
    print("\nComputed solution x:", x_solution)
    print("Expected solution x:", x_true)
    print("Residual error Ax - b:", residual)
    
    is_correct = all(abs(res) < 1e-6 for res in residual)
    print("Test passed!" if is_correct else "Test failed!")

test_sizes = [5, 10, 20]
for size in test_sizes:
    test_solution(size, use_hilbert=False)
    test_solution(size, use_hilbert=True)