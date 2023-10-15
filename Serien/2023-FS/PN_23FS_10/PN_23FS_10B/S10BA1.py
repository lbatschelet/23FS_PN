# Definition der Matrizen A und B
A = [[11, 2, 3],
     [4, 2, 6],
     [-11, 24, -1]]

B = [[9, 21, 5],
     [1, -3, 3],
     [9, -8, 2]]

# Initialisierung der Ergebnismatrix C mit Nullen
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Addition der Matrizen A und B, Speicherung in Matrix C
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

# Ausgabe der Ergebnismatrix C
print("Die addierte Matrix C ist:")
for row in C:
    print(row)
