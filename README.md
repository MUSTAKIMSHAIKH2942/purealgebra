
# purealgebra

[![CI](https://github.com/yourusername/purealgebra/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/purealgebra/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/purealgebra.svg)](https://badge.fury.io/py/purealgebra)

A minimal pure Python algebra library (no dependencies).

## Installation

```bash
pip install purealgebra
```

## Development install

```bash
git clone https://github.com/yourusername/purealgebra.git
cd purealgebra
pip install .
```

## Usage

```python
from purealgebra import add, matrix_multiply, poly_eval

print(add(2, 3))  # 5

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(matrix_multiply(A, B))

poly = [1, 0, 3]  # 1 + 0*x + 3*x^2
print(poly_eval(poly, 2))  # 13
```

## Modules

- Basic: add, subtract, multiply, divide
- Linear Algebra: transpose, dot_product, matrix_multiply, determinant, inverse_2x2
- Polynomial: poly_add, poly_eval, poly_derivative
- Solver: gaussian_elimination

## Run Tests

```bash
pip install pytest
pytest tests
```

## License

MIT License.
