
def poly_add(p1, p2):
    length = max(len(p1), len(p2))
    p1 = p1 + [0]*(length - len(p1))
    p2 = p2 + [0]*(length - len(p2))
    return [a + b for a, b in zip(p1, p2)]

def poly_eval(poly, x):
    return sum(coef * (x ** i) for i, coef in enumerate(poly))

def poly_derivative(poly):
    return [i * coef for i, coef in enumerate(poly)][1:]
