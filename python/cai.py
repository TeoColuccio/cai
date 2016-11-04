from random import *

def cai_extract(level):
    return randrange(0, 10**level)

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

def cai_play(opzione, a, b, esatte):
    if opzione == 1:
        ris = a + b
        
        print 'Quanto fa la seguente addizione: ', a, '+', b
        risposta = input()
    
    elif opzione == 2: 
        ris = a - b
        
        print 'Quanto fa la seguente sottrazione: ', a, '-', b
        risposta = input()
    
    elif opzione == 3:
        ris = a * b
        
        print 'Quanto fa la seguente moltiplicazione: ', a, '*', b
        risposta = input()
    
    elif opzione == 4:
        ris = a / b

        print 'Quanto fa la seguente addizione: ', a, '/', b
        risposta = input()
    
   #elif opzione == 5: 
    #   rand = randrange(0, 6)

    if risposta != ris:
        print cai_false()
    else:
        print cai_true()
        esatte += 1
        
    return esatte

if __name__ == '__main__':
    print cai_true()
