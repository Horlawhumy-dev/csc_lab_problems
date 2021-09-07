# print("Python program that calculates the multiplication of matrices matrices")
 # First Matrix
def first_matrix():
    row_1 = int(input("Enter the number of rows for first matrix: "))
    column_1 = int(input("Enter the number of columns in first matrix: "))
    row = []
    col = []
    while row_1 > 0:
        for i in range(column_1):
            entry = float(input(f"Enter the element at index {i} of the matrix: "))
            col.append(entry)
        row.append(col)
        col = []
        row_1 -= 1
    return row

# # Second Matrix
def second_matrix():
    row_2 = int(input("Enter the number of rows for second matrix: "))
    column_2 = int(input("Enter the number of columns second matrix: "))
    row = []
    col = []
    while row_2 > 0:
        for i in range(column_2):
            entry = float(input(f"Enter the element at index {i} of the matrix: "))
            col.append(entry)
        row.append(col)
        col = []
        row_2 -= 1
    return row

first = first_matrix()
print("<------------------------------------------------------->")
second = second_matrix()

def matrix_multiplication():
    result = [[0 for x in range(len(second) + 1)] for y in range(len(first))]
    # iterate through rows of first
    for i in range(len(first)):
       # iterate through columns of second
       for j in range(len(second[i])):
           # iterate through rows of second
           for k in range(len(second)):
               result[i][j] += first[i][k] * second[k][j]
    return  result

answer = matrix_multiplication()
print(answer)


# res = [[0 for x in range(10)] for y in range(10)]

# res = [
# #     [0, 0, 0],
# #     [0, 0,0],
# #     [0, 0, 0]
# # ]
# #
# # # explicit for loops
# # for i in range(len(matrix1)):
# #     for j in range(len(matrix2[0])):
# #         for k in range(len(matrix2)):
# #             # resulted matrix
# #             res[i][j] += matrix1[i][k] * matrix2[k][j]
# #
# # print(res)