def is_reflective(matrix):
    for i in range(0, len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def is_transitive(matrix):
    ord1_list = set()
    ord2_list = set()
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            if matrix[x][y] == 1:
                ord1_list.add(y)

        for z in ord1_list:
            for p in range(0, len(matrix)):
                if matrix[z][p] == 1:
                    ord2_list.add(p)
        for k in ord2_list:
            if matrix[x][k] == 0:
                return False
        ord1_list = set()
        ord2_list = set()
    return True
    
def is_symetric(matrix):
    for i in range(0, len(matrix)):
        for k in range(0, len(matrix)):
            if matrix[i][k] != matrix[k][i]:
                return False
    return True

def is_antisymetric(matrix):
    for i in range(0, len(matrix)):
        for k in range(0, len(matrix)):
            if matrix[i][k] == matrix[k][i] and k != i:
                return False
    return True

def transitive_lock(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    ord1_list = set()
    ord2_list = set()
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix)):
            if matrix[x][y] == 1:
                ord1_list.add(y)

        for z in ord1_list:
            for p in range(0, len(matrix)):
                if matrix[z][p] == 1:
                    ord2_list.add(p)

        for k in ord2_list:
            if matrix[x][k] == 0:
                matrix[x][k] = 1
        ord1_list = set()
        ord2_list = set()
    return matrix

def reflective_lock(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    for i in range(0, len(matrix)):
        matrix[i][i] = 1
    return matrix

def symetric_lock(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    for i in range(0, len(matrix)):
        for k in range(0, len(matrix)):
            if matrix[i][k] == 1:
                matrix[k][i] = 1
    return matrix

def make_antisymetric(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    if is_antisymetric(matrix) == True:
        return matrix
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix)):
            if matrix[row][col] == matrix[col][row] == 1 and row != col:
                matrix[row][col] = 0
    return matrix

def relation_power(mat, n=2):
    if n == 1:
        return mat
    def mat_mult(mat, mat1):
        new_mat = []
        for row in range(0,len(mat)):
            new_mat.append([])
            for col in range(0, len(mat)):
                el = 0
                for i in range(0, len(mat)):
                    el += mat[row][i]*mat1[i][col]
                    if el == 1:
                        break
                new_mat[row].append(el)
        return new_mat
    res_mat = []
    for i in range(0,len(mat)):
        res_mat.append([])
        for j in range(0,len(mat)):
            res_mat[i].append(mat[i][j])
    for j in range(0, n-1):
        res_mat = mat_mult(res_mat, mat)
    return res_mat

def equiv_lock(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    while is_equiv(matrix) == False:
        matrix = reflective_lock(matrix)
        matrix = transitive_lock(matrix)
        matrix = symetric_lock(matrix)
    return matrix

def is_equiv(matrix):
    if is_symetric(matrix) == True and is_reflective(matrix) == True and is_transitive(matrix) == True:
        return True
    else:
        return False

def is_part_order(matrix):
    if (is_reflective(matrix) == True) and (is_transitive(matrix) == True) and (is_antisymetric(matrix) == True):
        return True
    else:
        return False

def make_trans_and_antisym(mat):
    def custom_transitive_lock(matrix):
        ord1_list = set()
        ord2_list = set()
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix)):
                if matrix[x][y] == 1:
                    ord1_list.add(y)

            for z in ord1_list:
                for p in range(0, len(matrix)):
                    if matrix[z][p] == 1:
                        ord2_list.add(p)

            for k in ord2_list:
                if matrix[x][k] == 0 and matrix[k][x] == 1:
                    matrix[k][x] = 0
                    matrix[x][k] = 1
            ord1_list = set()
            ord2_list = set()
        return matrix
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    matrix = make_antisymetric(matrix)
    matrix = custom_transitive_lock(matrix)

    return matrix

def printed(matrix):
    string = ""
    ln = len(matrix[0])
    string += (ln + (ln-1)*6 + 6) * "-" + "\n"
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if col == 0:
                string += f"|  {matrix[row][col]}   "
            elif col == len(matrix[0]) - 1:
                string += f"   {matrix[row][col]}  |"
            else:
                string += f"   {matrix[row][col]}   "
        string += "\n"
    string += (ln + (ln-1)*6 + 6) * "-"
    return string

def part_order_lock(mat):
    matrix = []
    for i in range(0, len(mat)):
        matrix.append([])
        for k in range(0, len(mat[0])):
            matrix[i].append(mat[i][k])
    matrix = reflective_lock(matrix)
    matrix = transitive_lock(matrix)
    if is_part_order(matrix) == True:
        return matrix
    else:
        print("It is impossible to close this matrix by partial order relation. Symmetric elements must be removed")
        matrix = make_antisymetric(matrix)
        matrix = transitive_lock(matrix)
        if is_part_order(matrix) == True:
            return matrix
        else:
            matrix = make_trans_and_antisym(matrix)
            if is_part_order(matrix) == True:
                return matrix

matrix = [ [1,1,1,0,0], [0,0,1,1,1], [1,0,0,1,1], [1,1,1,1,0], [1,0,0,0,1] ]
print("Input matrix: \n", printed(matrix))
print("Symmetric? \n", is_symetric(matrix), "\n\nReflective?\n", is_reflective(matrix), "\n\nTransitive?\n", is_transitive(matrix))
print("\nIs equivalence relation?\n", is_equiv(matrix), "\n\nIs partial order?\n", is_part_order(matrix))
print("\nReflective clouser: \n", printed(reflective_lock(matrix)), "\n\nTransitive closure:\n ", printed(transitive_lock(matrix)), "\n\nSymmetric closure: \n", printed(symetric_lock(matrix)))
print("\nEquivalence closure: \n", printed(equiv_lock(matrix)))
print()
print("\nPartial order closure: \n", printed(part_order_lock(matrix)))
print("\nRelation to the 2nd power: \n", printed(relation_power(matrix)), "\n\nRelation to the 3d power: \n", printed(relation_power(matrix, 3)))