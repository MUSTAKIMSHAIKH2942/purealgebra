
from purealgebra import transpose, dot_product, matrix_multiply, determinant, inverse_2x2

def test_transpose():
    assert transpose([[1,2],[3,4]]) == [[1,3],[2,4]]

def test_dot_product():
    assert dot_product([1,2,3],[4,5,6]) == 32

def test_matrix_multiply():
    A = [[1,2],[3,4]]
    B = [[2,0],[1,2]]
    assert matrix_multiply(A,B) == [[4,4],[10,8]]

def test_determinant():
    assert determinant([[1,2],[3,4]]) == -2

def test_inverse_2x2():
    inv = inverse_2x2([[4,7],[2,6]])
    assert round(inv[0][0],2) == 0.6
