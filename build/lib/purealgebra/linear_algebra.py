
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return sum(a * b for a, b in zip(v1, v2))

def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(s)
        result.append(row)
    return result

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif len(matrix) == 3:
        a,b,c = matrix[0]
        d,e,f = matrix[1]
        g,h,i = matrix[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    else:
        raise NotImplementedError("Only 2x2 or 3x3 determinant implemented")

def inverse_2x2(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular")
    return [[matrix[1][1]/det, -matrix[0][1]/det],
            [-matrix[1][0]/det, matrix[0][0]/det]]
