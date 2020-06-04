from vectors import Vectors

class Matrices():

    def read_matrix(self, data):
        try:
            rows = data.split(',')
            matrix = []

            for r in rows:
                matrix.append(Vectors().read_vector(r))

            return matrix    

        except Exception as e:
            raise e

    def determinant(self, instr):
        try:

            matrix = self.read_matrix(instr[ 4 : -1 ])
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
