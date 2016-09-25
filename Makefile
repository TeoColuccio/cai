CFLAGS=-Wall --ansi

cai: main.o cai.o random.o
				gcc main.o cai.o random.o -o cai

main.o: main.c
cai.o: cai.c
random.o: random.c

clean:
				rm -f *.o
