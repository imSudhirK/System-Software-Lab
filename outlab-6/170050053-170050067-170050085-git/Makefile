all:  main clean
main: main.o sorting.o
	g++ main.o sorting.o -o main
main.o: main.cpp sorting.h
	g++ -c main.cpp
sorting.o:sorting.cpp sorting.h
	g++ -c sorting.cpp
clean:
	rm *.o
