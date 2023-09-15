##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/14/2023                   #
# Filename: 1.10.py                          #
# License: Apache 2.0                        #
#                                            #
##############################################

def read_matrix(matrix_name):
    print(f"Enter {matrix_name}:")
    matrix = []
    data = [float(el) for el in input().split()]
    matrix.append(data[:3])
    matrix.append(data[3:6])
    matrix.append(data[6:])
    return matrix

def add_matrices(a, b):
    result_matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(a[i][j] + b[i][j])
        result_matrix.append(row)
    return result_matrix

a = read_matrix("matrix1")
b = read_matrix("matrix2")

res = add_matrices(a, b)

print(f"{a[0][0]} {a[0][1]} {a[0][2]}\t \t{b[0][0]} {b[0][0]} {b[0][2]}\t \t{res[0][0]} {res[0][0]} {res[0][0]}")
print(f"{a[1][1]} {a[1][1]} {a[1][2]}\t+\t{b[1][0]} {b[1][1]} {b[0][2]}\t=\t{res[1][1]} {res[1][1]} {res[1][1]}")
print(f"{a[2][2]} {a[2][1]} {a[2][2]}\t \t{b[2][0]} {b[2][2]} {b[0][2]}\t \t{res[2][2]} {res[2][2]} {res[2][2]}")