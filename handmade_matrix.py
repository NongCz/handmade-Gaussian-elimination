import random

def generate_linear_system(n, min_val=-10, max_val=10):
 
    A = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    
    x = [i+1 for i in range(n)]
    
    b = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    
    return A, b, x


n = 3  
A, b, x_true = generate_linear_system(n)

print("Matrix A:")
for row in A:
    print(row)
print("\nRight-hand side b:", b)
print("\nKnown solution x:", x_true)
