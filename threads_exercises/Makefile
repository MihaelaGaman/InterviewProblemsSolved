#sthread: sthread.o
#	gcc -pthread sthread.o
#
#threadHello: threadHello.o sthread.o
#	gcc -pthread sthread.o threadHello.o -o hello
#
#sthread.o: sthread.c sthread.h
#	gcc -c sthread.c
#
#threadHello.o: threadHello.c sthread.h
#	gcc -c threadHello.c
#
HEADERS = sthread.h

default: threadHello

threadHello.o: threadHello.c $(HEADERS)
	gcc -c threadHello.c -o threadHello.o 

threadHello: threadHello.o sthread.o
	gcc sthread.o threadHello.o -o threadHello -lpthread

sthread.o: sthread.c sthread.h
	gcc -c sthread.c 

clean:
	-rm -f *.o
	-rm -f sthread threadHello
