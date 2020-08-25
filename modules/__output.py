def print_number(num):
    
    if type(num) == complex:
        if num.imag == 0:
            result = clean_float(num.real)
        elif num.real == 0:
            result = '{}j'.format(clean_float(num.imag))
        else:
            result = num

    elif type(num) == float:
        result = clean_float(num)

    print(result, end = ' ')

def clean_float(num):
    
    if num.is_integer():
        return int(num)
    else:
        return num

def display(data):

    print('\n')
    
    if type(data) == list:
        for r in data:
            if type(r) == complex:
                print_number(r)
            else:
                for c in r:    
                    print_number(c)

            print('\n')

    elif type(data) == complex:
        print_number(data)