#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    fir_row = []

    for i in matrix:
        sec_row = []

        for x in i:
            sec_row.append(x ** 2)

        fir_row.append(sec_row)

    return fir_row
