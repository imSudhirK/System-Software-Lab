all:  main
.PHONY: skiprebuild
skiprebuild:
	touch -m main.o depend.o depend.h;
.PHONY: skiprebuildh
skiprebuildh:
	touch -r main.o depend.h;
main: main.o depend.o
	g++ main.o depend.o -o main
main.o: main.cpp depend.h
	g++ -c main.cpp
depend.o:depend.cpp depend.h
	g++ -c depend.cpp
.PHONY: clean
clean:
	rm *.o
