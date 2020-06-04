class Vectors():

    def read_vector(self, vs):
        try:

            v = vs.split(' ')
            res = []

            for n in v:
                try:
                    res.append(float(n))
                except Exception as e:
                    pass

            return res

        except Exception as e:
            print(e)
            raise Exception('Invalid vector string.')

    def read_dot_product(self, instr):
        try:

            vector_strings = instr.split("x")
            
            vectors = []

            for v in vector_strings:
                vectors.append(self.read_vector(v))
            
            l = len(vectors[0])

            for v in vectors[1:]:
                if len(v) != l:
                    raise Exception('Vectors must be same length')
            
            return vectors

        except Exception as e:
            print(e)
            raise e

    def dot_product(self, instr):
        
        try:

            vectors = self.read_dot_product(instr[ 0 : -1 ])

            r = len(vectors)
            c = len(vectors[0])

            result = [1] * c

            for i in range(r):
                for j in range(c):
                    result[j] *= vectors[i][j]
            
            return result
        
        except Exception as e:
            print(e)