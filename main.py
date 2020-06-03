
import sys
import re
from matrices import read_matrix, determinant
from vectors import read_vector, dot_product

def help():
    operations = {
        'determinant': 'det(a0,0 a0,1 ... a0,M, ... aN,0 aN,1 ... aN,M\n [ ai,j \u03B5 \u211D \u2200 i,j \u03B5 \u2115]',
        'dot product': 'a0 a1 ... aN x b0 b1 ... bN\n [ ai, bj \u03B5 \u211D \u2200 i,j \u03B5 \u2115]'
    }
    
    print('\n')
    
    for key, value in operations.items():
        print('{}: {}\n'.format(key, value))

def get_instruction_type(instr: str):
    try:
        operations = {
            'det': r'^det\([0-9. ,]*\) *$',
            'dprod': r'^[0-9 .]*x[0-9 .]*$'
        }

        for key, regex in operations.items():

            try:
                if re.match(regex, instr).end() == len(instr):
                    return key
            except:
                pass
        
        raise Exception()
    
    except:
        print('Invalid instruction format.')

def calculate(instr, type):
    try:
    
        if type == 'det':
            matrix = read_matrix(instr[ 4 : -1 ])
            return determinant(matrix)
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    
    for x in sys.argv:
        if x == '-help':
            help()
            sys.exit()
    
    else:

        instr = input()

        instr_type = get_instruction_type(instr)

        result = calculate(instr, instr_type)

        print(result)
