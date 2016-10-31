CFLAGS=-Wall --ansi

cai: main.o cai.o random.o
				gcc main.o cai.o random.o -o cai

main.o: main.c cai.h
cai.o: cai.c cai.h random.h
random.o: random.h

clean:
				rm -f *.o
