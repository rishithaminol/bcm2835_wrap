CC = gcc

default: libbcm2835.a

libbcm2835.a: bcm2835.o pwm.o
	ar rcs $@ $^

bcm2835.o: bcm2835.c bcm2835.h
	$(CC) -c $<

pwm.o: pwm.c pwm.h
	$(CC) -c $<

clean:
	rm *.o *.a
