import sys

from modules.__io import display, get_instruction_type
from modules.__matrices import product, det

def help():
    operations = {
        'DETERMINANT (syntax)': 'det(a0,0 a0,1 ... a0,M, ... aN,0 aN,1 ... aN,M):\n [ ai,j \u03B5 \u2102 \u2200 i,j \u03B5 \u2115]',
        'PRODUCT (syntax)': 'a0 a1 ... aN x b0 b1 ... bN:\n [ ai, bj \u03B5 \u2102 \u2200 i,j \u03B5 [0,N]]',
        'NUMBERS (format)': '(-)(number)(-/+)(number)j (i.e 1+j, 2, -2-j, -2, -2.20, 2.2)',
        'SYNTAX': '1. Seperate columns by spaces. \n2. Seperate rows by columns \n3. Seperate values by operators. \n'
    }
    
    print('\n')
    
    for key, value in operations.items():
        print('{} -------------- \n{}\n'.format(key, value))


def calculate(instr, type):
    try:
    
        if type == 'det':
            return det(instr)

        if type == 'prod':
            return product(instr)

    except Exception as e:

        print(e)

def app():
    if '-help' in sys.argv:
        help()
    else:
        instr = input()
        instr_type = get_instruction_type(instr)
        answer = calculate(instr, instr_type)
        display(answer)

if __name__ == '__main__':
    app()
