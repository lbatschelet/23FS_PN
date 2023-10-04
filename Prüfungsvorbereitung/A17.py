"""
# (a)
def lowercase_and_c_to_k(input_string):
    mod_string = input_string.replace("c", "k")
    mod_string = mod_string.lower()
    return mod_string

# (b)
def dataContains(search_string):
    with open("data.txt", "r") as file:
        for line in file:
            if search_string in line:
                return True
    return False

print(dataContains("Frog"))
"""
# (c)
def max_matrix(matrix):
    max = matrix[0][0] #festsetzten des ersten Wertes
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max:
                max = matrix[i][j]
    return max

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(max_matrix(matrix))