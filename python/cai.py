from myrandom import *

def cai_init():
    myrandom_init()

def cai_extract():
    return myrandom_beetween(0, 10)

def cai_true():
    rand = myrandom_beetween(1, 5)

    if rand == 1:
        return 'Very good!'
    elif rand == 2:
        return 'Excellent'
    elif rand == 3: 
        return 'Nice work!'
    elif rand == 4:
        return 'Keep up the good work!'

def cai_false():
    rand = myrandom_beetween(1, 5)
 
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