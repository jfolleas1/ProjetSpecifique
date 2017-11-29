#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Node.h"
#include "GeneralNode.h"
#include "Leaf.h"
#include "ARF.h"
#include "DataVector.h"


using namespace std;


//Here put the args and wath they do
/*
1 puissance de deux du domaine 
2 minimum range size
3 dim
domain = 2^domainPow*minRangeSize
4 nbre of keys in the data base
5 size of the filter (8*nbrekeys) in number of bits
7 nameFile feed
8 nameFile test
*/

int main (int argc, char* argv[]){

	int perfectSize;
	cout<<"begin \r\n";
	//Get parameters
	int domainPow = atoi(argv[1]);
	int minRangeSize = atoi(argv[2]);
	int dim = atoi(argv[3]);
	int numberOfKey = atoi(argv[4]);
	int filterSize = atoi(argv[5]);
	string nameFileFeed =  argv[6];
	string nameFileTest =  argv[7];

	cerr << domainPow << endl;
	cerr << minRangeSize << endl;
	cerr << dim << endl;
	cerr << numberOfKey << endl;
	cerr << filterSize << endl;
	cerr << nameFileFeed << endl;
	cerr << nameFileTest << endl;

    // --------------------------------------------------------------------------------------
    // Build the ARF
	cerr << "load the data from file \r\n";
	DataVector myDataBase(dim, numberOfKey , domainPow, minRangeSize, nameFileFeed);
	myDataBase.toSet();

	cerr<<"Creation of the sdf ARF \r\n";
	ARF myARF(dim, minRangeSize, domainPow, filterSize);

	cerr<<"making of the perfect tree" << endl;
	myDataBase.AddKey(myARF);
	cerr<<"reducing the size of the ARF to the target size"<<endl;
	perfectSize = myARF.Size();
	cerr<<"Tree Size : "<<myARF.Size()<<endl;
	myARF.erase();
	cerr<<"Tree Size after: "<<myARF.Size()<<endl;
	myDataBase.checkPresenceAround(myARF, false, &myDataBase);
	myARF.DispStatistics();
	cerr<<"SIZE: "<< myARF.Size() << "False positive" << myARF.getNumberOfFalsePositif() << endl;
	// We reset the stats
	myARF.resetStatistics();

	cerr<<" WO Training"<<endl;
	myARF.resetStatistics();

    // --------------------------------------------------------------------------------------
    // Begin Test
	DataVector myQuery1 (dim, numberOfKey , domainPow, minRangeSize, nameFileTest);
	myQuery1.toSet();
	cerr<<"checking"<< endl;
	myQuery1.checkPresenceAround(myARF, true, &myDataBase);

	// display result.
	myARF.DispStatistics();
	cout<<"SIZE:*"<< myARF.Size() << "*False positive:*" << myARF.getNumberOfFalsePositif() << '*'<< endl;

	return 0;
	
}
