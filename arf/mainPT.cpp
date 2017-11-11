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

6 number of trainning querys
*/

int main (int argc, char* argv[])
{
	/*cout<<"begin \r\n";
	//Get parameters
	int domainPow = atoi(argv[1]);
	int minRangeSize = atoi(argv[2]);
	int dim = atoi(argv[3]);
	
	int numberOfKey = atoi(argv[4]);
	int filterSize = atoi(argv[5]);
	
	int numberOfTrainingQuery =  atoi(argv[6]);

	 cout<<"Creation of the database \r\n";
	DataVector myDataBase(dim, numberOfKey , domainPow, minRangeSize);
	myDataBase.toSet();

	 cout<<"Creation of the ARF \r\n";
	ARF myARF(dim,minRangeSize, domainPow, filterSize);

	cout<<"making of the perfect tree \r\n";
	myDataBase.AddKey(myARF);

	cout<<"reducing the size of the ARF to the target size"<<endl;
	myARF.erase();

	cout<<"Training"<<endl; 
		
	DataVector myTrainingQuery=myDataBase.makeDifferent(minRangeSize,numberOfTrainingQuery);
	cout<<"toset"<<endl;
	myTrainingQuery.toSet();
	cout<<"will check"<<endl;
	myTrainingQuery.checkPresenceAround(myARF, true);

	myARF.resetStatistics();

	//End of the training;

	//show results

	DataVector myQuery1=myDataBase.makeDifferent(minRangeSize,1000);
	cout<<"toset"<<endl;
	myQuery1.toSet();
	cout<<"will check"<<endl;
	myQuery1.checkPresenceAround(myARF, true);

	cout<<"Results 1 : \r\n";
	myARF.DispStatistics();
	myARF.resetStatistics();
	
	int truc =0;
	DataVector myQuery2=myDataBase.makeSimilar(truc,1000);
	myQuery2.toSet();
	myDataBase.checkPresenceAround(myARF, false);

	cout<<"Results 2 : \r\n";
	myARF.DispStatistics();
	myARF.resetStatistics();

	DataVector myQuery3=myDataBase.makeDifferent(minRangeSize,1000);
	myQuery3.toSet();
	myQuery3.checkPresenceAround(myARF, true);

	cout<<"Results 3 : \r\n";
	myARF.DispStatistics();
	myARF.resetStatistics();

	cout<<"Tree Size : "<<myARF.Size()<<endl;*/
	


	ARF myARF(2,3,4,40);
	DataVector myDV(2, 2 , 4, 3);
	vector<bool> vectorIsPresent;
	for(int i =0; i < 9 ; i++)
	{ vectorIsPresent.push_back(false);}

		
	myDV.toSet();
	myDV.printDataVector();
	myDV.AddKey(myARF);
	myARF.printARF();
	myARF.erase();
	myARF.printARF();
	int a, b;
	cin>>a>>b;
	int myints[2];
	myints[0]=a;
	myints[1]=b;
	vector<int> K1(myints, myints+2);
	
	vector< vector<int> > VectKeys; 
	myARF.DiscretiseWV(K1,VectKeys,1);
	for(vector< vector<int> >::iterator it = VectKeys.begin(); it != VectKeys.end(); it++)
	{
		for(int i =0; i < 2 ; i++)
		cout<<(*it)[i]<<"\t";
		cout<<endl;
	}
	myARF.CheckAroundKey(&myDV,VectKeys,vectorIsPresent,true);
	myARF.printARF();
	
	/*ARF myARF(2,3, 3);
  std::cout << "\n =============================== \n\r";

	int myints[] = {3,2};
	std::vector<int> K1(myints, myints+2);
	std::vector< std::vector<int> > VectKeys;
	/*int myints2[] = {8,8};
	std::vector<int> K2(myints2, myints2+2);
	myARF.AddKey(K1);
	myARF.printARF();
	if (myARF.CheckKey(K2, true))
	cout<<"OK \r\n";*/
	/*myARF.DiscretiseWV(K1, VectKeys);
	for (std::vector< vector< int > >::iterator it = VectKeys.begin() ; it != VectKeys.end(); ++it)
		{
			for (std::vector< int >::iterator itv = (*it).begin() ; itv != (*it).end(); ++itv)
			cout<<(*itv)<<" ";
			cout<<endl;
		}*/
	/*myARF.printARF();
	int targetSize=25;	
	//myARF.erase(targetSize);
  std::cout << "\n =============================== \n\r";
	int myints[] = {1,1};
	std::vector<int> K1(myints, myints+2);
	myARF.AddKey(K1);
	myints[0] = 2;
	std::vector<int> K2(myints, myints+2);
	myARF.CheckKey(K2, true);
	myints[1]= 2;
	std::vector<int> K3(myints, myints+2);
	myARF.CheckKey(K3, true);
	myints[0] = 1;
	std::vector<int> K4(myints, myints+2);
	myARF.CheckKey(K4, true);
std::cout << "\n =============================== \n\r";
	myARF.printARF();
	cout<<"erase"<<endl;
	myARF.erase(targetSize);
	cout<<"fin\r\n";
	myARF.printARF();	
	//Ici pb
	//myARF.printARF();
	/*myARF.printARF();
	cout<<myARF.Size()<<endl;
	cout<<"==============================="<<endl;
	DataVector myDV(3,3,3);
	myDV.printDataVector();
	cout<<"==============================="<<endl;
	myDV.AddKey(myARF);
	myARF.printARF();
	cout<<myARF.Size()<<endl;
	/*myDV.checkPresence(myARF,false);
	myARF.DispStatistics();
	myARF.resetStatistics();
	cout<<"==============================="<<endl;
	myARF.DispStatistics();
	//myARF.printARF();
	cout<<"==============================="<<endl;
	DataVector myOtherDV = myDV.makeDifferent(1, 1000);
	cout<<"coucocu \r\n";
	myOtherDV.checkPresence(myARF,true);
	myARF.DispStatistics();*/
//	myOtherDV.printDataVector();
/*	Node myNode(NULL);
//	GeneralNode* pt = & myNode;
//	if(instanceof<Node>(pt))
	myNode.printData();
	cout<<"check  value \r\n";
	myNode.ChangeLeafValue(2,true);
	cout<<"ok \r\n";	
	myNode.Split(4,5);
	myNode.printData();



*/
/*	int myints[] = {10,9,4,4,4,7,4,8};
	std::vector<int> K1(myints, myints+2);
	std::vector<int> M(myints+2,myints+4);
	std::vector<int> K2(myints+4,myints+6);
	std::vector<int> K3(myints+6,myints+8);

	ARF myARF(2,5, 3);

	myARF.printARF();
	cout<<"==============================="<<endl;
	
	//cout<<myARF. navigate(myARF.root,M,8,K)<<endl;
	myARF.AddKey(K1);
//	myARF.AddKey(K1);
//	myARF.AddKey(K1);
	myARF.printARF();
	cout<<"==============================="<<endl;
	//myARF.root->Split(2,2);
	//myARF.root->Split(0,0);
	//printf("%x \r\n", &a );
	//myARF.printARF();
	/*int size = 128;
	cout<<"==============================="<<endl;
	*/
	//int size = 8;	
	//Leaf* P= myARF.navigate((Node*)(myARF.root), M,size, K);
	/*Node* Old = (Node*)(((Node*)(myARF.root))->getChildNodes(0));
	cout<<"O"<<Old<<endl;
	//Leaf* R = (Leaf*)(Old->getChildNodes(0));
*/	//cout<<"P"<<P<<endl;
/*	cout<<"Root"<<myARF.root<<endl;
	*/

	//cout<<(8&(255-((int)pow(2,9%8))))<<endl;
return 0;
}
