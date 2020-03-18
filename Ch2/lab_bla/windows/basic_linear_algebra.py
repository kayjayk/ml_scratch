def vector_size_check(*vector_variables):
    return len(set([len(vector) for vector in vector_variables])) == 1


def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(t) for t in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return [-sum(t) + t[0]*2 for t in zip(*vector_variables)]



def scalar_vector_product(alpha, vector_variable):
    return [alpha * t for t in vector_variable]


def matrix_size_check(*matrix_variables):
    return all((vector_size_check(*matrix_variables),
                all([vector_size_check(t) for t in zip(*matrix_variables)])))


def is_matrix_equal(*matrix_variables):
    return all([all([len(set(t))==1 for t in zip(*vectors)]) for vectors in zip(*matrix_variables)])


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(t) for t in zip(*vectors)] for vectors in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[t[0]*2 -sum(t) for t in zip(*vectors)] for vectors in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [list(vector) for vector in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha * t for t in vector] for vector in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len([t for t in zip(*matrix_a)]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a*b for a,b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
