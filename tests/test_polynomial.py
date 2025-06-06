
from purealgebra import poly_add, poly_eval, poly_derivative

def test_poly_add():
    assert poly_add([1,2],[3,4,5]) == [4,6,5]

def test_poly_eval():
    assert poly_eval([1,0,3],2) == 13

def test_poly_derivative():
    assert poly_derivative([1,2,3]) == [2,6]
