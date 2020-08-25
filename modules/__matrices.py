'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def read_vector(vs):

    try:

        v = vs.split(' ')
        res = []

        for n in v:
            try:
                res.append(complex(n))
            except Exception as e:
                pass

        return res

    except Exception as e:

        raise Exception('Invalid vector string.')

'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def dot(v1, v2):

    if len(v1) == 1:
        return [ v1[0] * nv2 for nv2 in v2 ]
    
    elif len(v2) == 1:
        return [ v2[0] * nv1 for nv1 in v1 ]
        
    elif len(v1) != len(v2):
        raise Exception('Vectors must have same length.')
    
    return sum([v1[i] * v2[i] for i in range(len(v1))])


'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def matrix_multiplication(m1, m2):
    
    r1, c1 = len(m1), len(m1[0])
    r2, c2 = len(m2), len(m2[0])


    if r1 == 1:
        result = [0] * r2
        for j in range(r2):
            result[j] = dot(m2[j][:], m1[0])                
        return result 

    elif r2 == 1:
        result = [0] * r1
        for j in range(r1):
            result[j] = dot(m1[j][:], m2[0])                
        return result

    if c1 != r2:
        raise Exception('Columns and rows must match.')

    result = [ [ 0 for _ in range(c2)] for _ in range(r1) ]

    for i in range(c2):
        for j in range(r1):

            v1, v2 = m1[j][:], [ m2[k][i] for k in range(r2) ]
            result[j][i] = dot(v1, v2)

    return result
    

'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def read_matrix(data):

    rows = data.split(',')
    matrix = []

    for r in rows:
        matrix.append(read_vector(r))

    l = len(matrix[0])
    
    for i in range(1, len(matrix)):
        if len(matrix[i]) != l:
            raise Exception('Inconsistant column size')

    return matrix    


'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def product(instr):

    matrix_strings = instr[:-1].split('x')
    matrices = []
    
    for m in matrix_strings:
        matrices.append(read_matrix(m))
    
    product = matrices.pop(0)

    while matrices:
        product = matrix_multiplication(product, matrices.pop(0))
    
    return product
    
'''
    @ARGS:
    @RETURN:
    @RAISES: 
'''
def det(instr):

    try:

        matrix = read_matrix(instr[ 4 : -2 ])
        det = 0
        
        r = len(matrix)
        c = len(matrix[0])

        for j in range(0, r):
            if (len(matrix[j]) != r):
                raise Exception('Not square.')

        if (r == 2 and c == 2):
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

        else:
            for a in range(0, r):
                
                sub_matrix = [ matrix[j][:a] + matrix[j][a+1:] for j in range(1, r)]

                if a % 2 == 0:
                    det = det + (matrix[0][a] * determinant(sub_matrix))
                else:
                    det = det - (matrix[0][a] * determinant(sub_matrix))
    
        return det
    
    except Exception as e:

        raise Exception('Couldn\'t caclulate determinant')

