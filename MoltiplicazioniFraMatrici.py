def multiply_matrices(matrix1, matrix2):
    # Verifica se le matrici sono compatibili per la moltiplicazione
    if len(matrix1[0]) != len(matrix2):
        print("Impossibile moltiplicare le matrici. Il numero di colonne della prima matrice non corrisponde al numero di righe della seconda.")
        return None

    # Inizializza una nuova matrice risultante con dimensioni corrette
    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Effettua la moltiplicazione delle matrici
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix

# Esempio di utilizzo
matrix1 = [[2, 1 ,3 , -1],
           [0, 0, -5, 2]]

matrix2 = [[1, -1, 3, 0]]


result = multiply_matrices(matrix1, matrix2)
if result:
    print("Risultato della moltiplicazione:")
    for row in result:
        print(row)
