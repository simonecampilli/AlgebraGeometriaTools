# Ricontrolliamo il calcolo del determinante di A utilizzando Sympy per evitare errori manuali
import sympy as sp
# Definiamo le variabili
x, y, z, k = sp.symbols('x y z k')

# Matrice dei coefficienti
A = sp.Matrix([
    [3,2,2],
    [0,1,k],
    [k,1,0],

])

# Calcoliamo il determinante di A
det_A = A.det()
det_A.simplify()
print(det_A)
print(det_A.simplify())