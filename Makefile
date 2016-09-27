CFLAGS=-Wall --ansi

cai: main.o cai.o random.o
				gcc main.o cai.o random.o -o cai

main.c: random.h
cai.c: cai.h random.h
random.c: random.h

clean:
				rm -f *.o
