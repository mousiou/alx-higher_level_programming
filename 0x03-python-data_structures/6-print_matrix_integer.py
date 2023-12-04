#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if len(matrix) >= 1:
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=" ")
    print()
