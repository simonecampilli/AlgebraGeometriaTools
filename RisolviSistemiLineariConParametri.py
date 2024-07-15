import sympy as sp
#RISOLVE SOLO IL RANGO AL MOMENTO
# Defining symbolic variable k
k = sp.symbols('k')

# Coefficient matrix A and augmented matrix [A|b]
'''A = sp.Matrix([
    [1, 1, .1, -3],
    [2, 1, -k, 2],
    [3, 2, 1-k**2, k-3]
])'''
A = sp.Matrix([
    [1,2,0,1,0],
    [0,1,2,-2,1],
    [1,2,1,0,0],
    [1,3,2,-1,0]

])

#b = sp.Matrix([k, 3, 2])

# Augmented matrix [A|b]
#A_b = A.row_join(b)
# Compute the Reduced Row Echelon Form (RREF) of A and the pivot columns
rref_A, pivot_columns = A.rref()

# Calculate the rank of A
rank_A = A.rank()

# Output the results
print("Reduced Row Echelon Form (RREF) of A:")
sp.pprint(rref_A, use_unicode=True)
print("\nPivot columns:", pivot_columns)
print("\nRank of matrix A:", rank_A)

