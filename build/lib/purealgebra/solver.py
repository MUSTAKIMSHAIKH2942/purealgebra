
def gaussian_elimination(A, b):
    n = len(A)
    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        for j in range(i + 1, n):
            ratio = A[j][i] / A[i][i]
            A[j] = [a - ratio * ai for a, ai in zip(A[j], A[i])]
            b[j] -= ratio * b[i]
    
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x
