
def display(data):
    
    print('\n')
    
    if type(data) == list:

        for r in data:
            for c in r:    
                print(c, end=' ')
            
            print('\n')

    elif type(data) == float:

        print(data)