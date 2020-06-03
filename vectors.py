def read_vector():
    try:

        print('\nEnter in Format:\na0 a1 ... aN')

        vector = [ float(an) for an in input().split(' ') ]

        return vector 
  
    except Exception as e:
        raise e


def dot_product(v1, v2):
    try:
        if len(v1) != len(v2):
            raise Exception("Vectors must be same length.")

        return [ v1[i] * v2[i] for i in range(len(v1)) ]
    
    except Exception as e:
        print(e)