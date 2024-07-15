from sympy import Matrix, zeros

# Definiamo i vettori generatori di U e W
v1 = Matrix([1, 0, 1, 1])
v2 = Matrix([2, 1, 2, 3])

v3 = Matrix([0, 2, 1, 2])
w1 = Matrix([1, -2, 0, -1])
w2 = Matrix([0, 1, 0, 0])

from sympy import Matrix, symbols, Eq, solve, linsolve

# Definiamo i simboli per i coefficienti
a, b, c, d, e = symbols('a b c d e')

# Definiamo i vettori generatori di U e W


# Espressione per la combinazione lineare di U e W
expr = a * v1 + b * v2 + c * v3 - d * w1 - e * w2

# Configuriamo il sistema di equazioni omogenee
equations = [Eq(x, 0) for x in expr]

# Risolviamo il sistema
solution = linsolve(equations, a, b, c, d, e)

# Stampiamo la soluzione
solution

print(solution)