
def display(data):
    
    print('\n')
    
    if type(data) == list:

        for r in data:
            for c in r:    
                if c.imag == 0:
                    print(c.real, end=' ')
                elif c.real == 0:
                    print(c.imag, end=' ')
                else:
                    print(c, end=' ')

            print('\n')

    elif type(data) == float:

        print(data)