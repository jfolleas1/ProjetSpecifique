FLG= -std=c++11

Node: Node.o main.o GeneralNode.o Leaf.o ARF.o DataVector.o
	g++ $(FLG) -o Node Node.o main.o GeneralNode.o Leaf.o ARF.o DataVector.o

Node.o: Node.cpp Node.h Leaf.h GeneralNode.h #Util.hpp
	g++ $(FLG) -o Node.o -c Node.cpp -W -Wall -ansi -pedantic

GeneralNode.o: GeneralNode.cpp GeneralNode.h
	g++ $(FLG) -o GeneralNode.o -c GeneralNode.cpp -W -Wall -ansi -pedantic

Leaf.o: Leaf.cpp Leaf.h GeneralNode.h
	g++ $(FLG) -o Leaf.o -c Leaf.cpp -W -Wall -ansi -pedantic

ARF.o: ARF.cpp ARF.h Node.h Leaf.h GeneralNode.h DataVector.h #Util.hpp
	g++ $(FLG) -o ARF.o -c ARF.cpp -W -Wall -ansi -pedantic

DataVector.o: DataVector.cpp DataVector.h
	g++ $(FLG) -o DataVector.o -c DataVector.cpp -W -Wall -ansi -pedantic

main.o: main.cpp Node.h Leaf.h GeneralNode.h ARF.h #Util.hpp
	g++ $(FLG) -o main.o -c main.cpp -W -Wall -ansi -pedantic


clean: 
	rm *.o Node
