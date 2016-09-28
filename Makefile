CFLAGS=-Wall --ansi

cai: main.o cai.o random.o
				gcc main.o cai.o random.o -o cai

main.o: random.h
cai.o: cai.h random.h
random.o: random.h

clean:
				rm -f *.o
