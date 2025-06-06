
from purealgebra import gaussian_elimination

def test_gaussian_elimination():
    A = [[2,1], [5,7]]
    b = [11,13]
    sol = gaussian_elimination(A,b)
    assert round(sol[0],2) == 7.111111111111111 - 6.333333333333333
