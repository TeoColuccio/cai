from random import *

def myrandom_init():
    seed()

def myrandom_beetween(min, max):
    return randint(min, max)

if __name__ =='__main__':
    print myrandom_beetween(1, 10)
