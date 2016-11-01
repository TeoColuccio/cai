from random import *

def cai_extract():
    return randrange(0, 10)
def cai_extract_livello_2():
    return randrange(0, 100)
def cai_extract_livello_3():
    return randrange(0, 1000)
def cai_true():
    rand = randrange(1, 5)

    if rand == 1:
        return 'Very good!'
    elif rand == 2:
        return 'Excellent'
    elif rand == 3: 
        return 'Nice work!'
    elif rand == 4:
        return 'Keep up the good work!'

def cai_false():
    rand = randrange(1, 5)
 
    if rand == 1:
        return 'No. Please try again.'
    elif rand == 2:
        return 'Wrong. Try once more.'
    elif rand == 3: 
        return 'Don\'t give up!'
    elif rand == 4:
        return 'No. Keep trying.'

if __name__ == '__main__':
    print cai_true()
