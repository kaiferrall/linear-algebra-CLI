def read_matrix(data):
    try:
        rows = data.split(',')
        matrix = []

        for r in rows:
            cols = r.split(' ')
            col = []

            for c in cols:
                try:
                    n = float(c)
                    col.append(n)
                except:
                    pass

            matrix.append(col)

        return matrix    

    except Exception as e:
        raise e

def determinant(matrix):
    try:
        
        det = 0
        
        r = len(matrix)
        c = len(matrix[0])

        for j in range(0, r):
            if (len(matrix[j]) != r):
                raise Exception('Not square.')

        if (r == 2 and c == 2):
            return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])

        else:
            for a in range(0, r):
                
                sub_matrix = [ matrix[j][:a] + matrix[j][a+1:] for j in range(1, r)]

                if a % 2 == 0:
                    det = det + (matrix[0][a] * determinant(sub_matrix))
                else:
                    det = det - (matrix[0][a] *determinant(sub_matrix))
      
        return det
    
    except Exception as e:
        print(e)

'''
a = determinant([[1, 2], [1, 2]])
print(a)


a = "1 2,1 2 3 4 5    "
m = read_matrix(a)
print(m)
'''