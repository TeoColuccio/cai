# Il programma genera 10 moltiplicazioni tra numeri casuali
# compresi tra 0 e 10. Lo studente dovra' rispondere ed il programma 
# calcolera' le risposte esatte, se queste sono inferiori al 75%, il
# programma consiglia allo studente di ripetere.

from cai import *

conta = 0
esatte = 0
opzione = 0
livello = 0

# Scelta opzioni
while opzione != 1 and opzione != 2 and opzione != 3 and opzione != 4 and opzione != 5:
    opzione = input('Scegli un opzione: 1(solo addizioni), 2(solo sottrazioni), 3(solo moltiplicazioni), 4(solo divisioni), 5(tutte le operazioni): ')
# Scelta livello
while livello != 1 and livello != 2 and livello != 3:
    livello = input('Scegli un livello: 1(operazioni a 1 cifra),  2(operazioni a 2 cifre), 3(operazioni a 3 cifre): ')
# Livello 1
if livello == 1:
    while conta < 10:
        a = cai_extract()
        b = cai_extract()
        cai_play(a, b, esatte)
        conta += 1
# Livello 2
elif livello == 2:
    while conta < 10:
        a = cai_extract_livello_2()
        b = cai_extract_livello_2()
        cai_play(a, b, esatte)
        conta += 1
# Livello 3
elif livello == 3:
    while conta < 10:
        a = cai_extract_livello_3()
        b = cai_extract_livello_3()
        cai_play(a, b, esatte)
        conta += 1
# Resoconto
if esatte < 7:
    print 'Please ask your instructor for extra help!'
else: 
    print 'Very good'
