# Il programma genera 10 moltiplicazioni tra numeri casuali
# compresi tra 0 e 10. Lo studente dovra' rispondere ed il programma 
# calcolera' le risposte esatte, se queste sono inferiori al 75%, il
# programma consiglia allo studente di ripetere.

from cai import *

esatte = 0
conta = 0

while conta < 10:
    a = cai_extract()
    b = cai_extract()
    prod = a * b
    
    print 'Quanto fa la seguente moltiplicazione: ', a, '*', b
    risposta = raw_input()
    if risposta!='':
        risposta = int(risposta)
    print "risposta ", risposta

    if risposta != prod:
        print cai_false()
    else:
        print cai_true()
        esatte += 1 
    conta += 1

if esatte < 7:
    print 'Please ask your instructor for extra help!'
else: 
    print 'Very good'
