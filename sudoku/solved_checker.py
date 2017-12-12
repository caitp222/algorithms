# def is_solved(st):
#     sorted_arr = ["1","2","3","4","5","6","7","8","9"]
#     matrix_rows = []
#     for i in range(9):
#         row = []
#         for j in range(9):
#             row.append(st[i * 9 + j])
#         matrix_rows.append(row)
#     matrix_columns = []
#     for i in range(9):
#         column = []
#         for j in range(9):
#             column.append(matrix_rows[j][i])
#         matrix_columns.append(column)
#     matrix_boxes = []
#     for h in range(3):
#         for i in range(3):
#             box = []
#             for j in range(3):
#                 for k in range(3):
#                     box.append(matrix_rows[3 * i + j][3 * h + k])
#             matrix_boxes.append(box)
#     for matrix in matrix_columns:
#         if matrix.sort() != sorted_arr:
#             return False
#     for matrix in matrix_rows:
#         if matrix.sort() != sorted_arr:
#             return False
#     for matrix in matrix_boxes:
#         if matrix.sort() != sorted_arr:
#             return False
#     return True

import copy

def is_solved(arr):
    sorted_arr = ["1","2","3","4","5","6","7","8","9"]
    rows = copy.deepcopy(arr)
    columns = []
    for i in range(len(arr)):
        column = []
        for j in range(len(arr[0])):
            column.append(arr[j][i])
        columns.append(column)
    boxes = []
    for h in range(3):
        for i in range(3):
            box = []
            for j in range(3):
                for k in range(3):
                    box.append(arr[3 * i + j][3 * h + k])
            boxes.append(box)
    for column in columns:
        column.sort()
        if column != sorted_arr:
            return False
    for box in boxes:
        box.sort()
        if box != sorted_arr:
            return False
    for row in rows:
        row.sort()
        if row != sorted_arr:
            return False
    return True
