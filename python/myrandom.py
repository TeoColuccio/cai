import random

def myrandom_init():
    random.seed()

def myrandom_beetween(min, max):
    return random.randint(min, max)

if __name__ =='__main__':
    print myrandom_beetween(1, 10)
