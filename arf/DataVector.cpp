/*************************************************************************
                           DataVector.cpp  -  description
                             -------------------
    date                 : 21/01/2016
    copyright            : (C) 2016 par jacques folleas
    e-mail               : jacques.folleas@insa-lyon.fr
*************************************************************************/

//-------Realisation of the class <DataVector> (file DataVector.cpp)------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- system includes
using namespace std;
#include <iostream>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <set>
#include <time.h>   


//----------------------------------------------------- personnal includes
#include "DataVector.h"

//------------------------------------------------------------- Constantes
const char SEPARATOR = ',';
//---------------------------------------------------- Variables de classe

//---------------------------------------------------------- private Types 


//----------------------------------------------------------------- PUBLIC

//-------------------------------------------------------- Publis methodes



void DataVector::printDataVector()
{
	cout.precision(15);
	cout<<"numberOfElement :"<<numberOfElement<<endl;
	cout<<"dim :"<<dim<<endl;
	cout<<"domain :"<<domain<<endl;
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it)
		{
			 for (std::vector<int>::iterator itv = it->begin() ; itv != it->end(); ++itv)
			{
				cout<<*itv<<"\t";
			}
			cout<<endl;
		}
	cout<<"SET : \n\r";
 for (std::set< vector<int> >::iterator it = this->Data.begin() ; it != this->Data.end(); ++it)
		{
			 for (std::vector<int>::const_iterator itv = it->begin() ; itv != it->end(); ++itv)
			{
				cout<<*itv<<"\t";
			}
			cout<<endl;
		}

}


void DataVector::checkToSet()
{
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it)
		{
			if(this->Data.find(*it)==this->Data.end())
				cout<<"PB one data is missing to the set"<<endl;
		}
}

//Discretie and put all data in the set
void DataVector::toSet()
{
	vector<int> myDiscretisedVector;
	int myDiscretisedValue;
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it)
		{	
			myDiscretisedVector.clear();
			for (std::vector< int >::iterator itk = (*it).begin() ; itk != (*it).end(); ++itk)
			{//we find the middle of the range which contain our value and push the left and right neighbor middle 
				myDiscretisedValue=(((*itk)-1)/(minRangeSize))*(minRangeSize);
				myDiscretisedValue+=(minRangeSize/2)+1;
				myDiscretisedVector.push_back(myDiscretisedValue);
			}
			this->Data.insert(myDiscretisedVector);
		}
}


DataVector::DataVector(const DataVector & copied)
{
	numberOfElement = copied.numberOfElement;
	dim =  copied.dim;
	domain = copied.domain;
	realElements =  copied.realElements;
	minRangeSize = copied.minRangeSize;
}

DataVector DataVector::makeSimilar(const int & similarity, int number)
{
	if (number==0 || ( number > (this->realElements.end()-this->realElements.begin())) )
	{ number = this->realElements.end()-this->realElements.begin();}


	DataVector similar;
	similar.dim=this->dim;
	similar.domain=this->domain;
	similar.minRangeSize=this->minRangeSize;
	similar.numberOfElement=number;
	vector<int> myvector;
	int myint;
	 for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.begin() + number ; ++it)
		{
			myvector.erase(myvector.begin(),myvector.end());
			 for (std::vector<int>::iterator itv = it->begin() ; itv != it->end(); ++itv)
			{	//for all vector and all dimention we add to the value a random valu in the range [-similarity ; similarity]
				myint = -1;
				while(myint<1 || myint > domain )
				myint = (*itv)+((((double)rand()/RAND_MAX)-0.5)*2*similarity);
				myvector.push_back (myint);
			}
			similar.realElements.push_back (myvector);
		}
	return similar;
}


DataVector DataVector::makeDifferent(const int & similarity, int number)
{

	if (number==0)
	{ number = this->realElements.end()-this->realElements.begin();}

	DataVector different;
	different.dim=this->dim;
	different.domain=this->domain;
	different.minRangeSize=this->minRangeSize;
	bool isdifferent;
	bool islocalydifferent;
	different.numberOfElement=number;
	vector<int> myvector;
	int myint;
	int count;

	//we build a random vector and verify if he is distance enough to all the vector in the data base by checking one by one
    for (int i =0 ; i < number ; i++){
                count=0;
                do{
                    isdifferent=true;
                    myvector.erase(myvector.begin(),myvector.end());
                    for (int u =0; u < different.dim ; u++){
                        myint = -1;
                        while(myint<1 || myint > domain )
                        myint =  rand();
                        myvector.push_back(myint);
                    }

                    for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it){
                        islocalydifferent=false;
                         for (int k =0; k < different.dim ; k++){
                            islocalydifferent|=( ((*it)[k]-myvector[k]>similarity) || ((*it)[k]-myvector[k]<(-1* similarity)) );
                        }

                        isdifferent&=islocalydifferent;
                    }
                    if(count==10000){
                        break;
                        cout<<"PB lors du makeDifferent boucle infini"<<endl;
                    }
                    count++;
                }while(!isdifferent);
        different.realElements.push_back (myvector);
    }
    return different;
}

void DataVector::AddKey(ARF & myARF){
	//set at true the corseponding leaf of the arf to all vector in the data base by calling the arf function
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it){
			myARF.AddKey(*it);
		}
}


void DataVector::checkPresence(ARF & myARF, bool different)
{
	
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it){
		cerr << "BEGIN LOOP" << endl;
		myARF.CheckKey(*it, different);
	}
}


void DataVector::checkPresenceAround(ARF & myARF, bool different, DataVector* DataBase)
{
	vector< vector<int> > vectKeys;
	vector<bool> vectorIsPresent;
//build all the neighbor vector of each key and verify if it is in the data base. After it set vectorIsPresnet and call the arf function 
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it)
	{	
		vectKeys.erase(vectKeys.begin(),vectKeys.end());
		vectorIsPresent.erase(vectorIsPresent.begin(),vectorIsPresent.end());
		this->Discretise( *it, vectKeys, vectorIsPresent);
		myARF.CheckAroundKey(DataBase, vectKeys, vectorIsPresent,different);
		
	}
	cout<<endl;
}


void DataVector::Discretise( std::vector<int> Key, std::vector< std::vector<int> > & VectKeys, vector<bool> & vectorIsPresent ,int numberOfElementsOnEachSide)
{
	vector < vector <int> > discretisedVector;
	vector <int> myDiscretisedElements;
	vector <int> vectorToPush;
	int myDiscretisedValue=0;
	for (std::vector< int >::iterator it = Key.begin() ; it != Key.end(); ++it)
	{
		myDiscretisedValue=(((*it)-1)/(minRangeSize))*(minRangeSize);
		myDiscretisedElements.push_back(myDiscretisedValue);
		myDiscretisedElements[0]+=(minRangeSize/2)+1;
		for(int i=1; i< numberOfElementsOnEachSide+1; i++)
		{
			myDiscretisedElements.push_back(myDiscretisedElements[0]-i*minRangeSize);
			myDiscretisedElements.push_back(myDiscretisedElements[0]+i*minRangeSize);				
		}
		discretisedVector.push_back (myDiscretisedElements);
		myDiscretisedElements.erase(myDiscretisedElements.begin(), myDiscretisedElements.end());
	}
	this->InsertPotentialVectorWV( discretisedVector,vectorToPush, VectKeys , vectorIsPresent);
}


void DataVector::InsertPotentialVectorWV(const vector< vector<int> > & discretisedVector, vector<int> & vectorToPush , std::vector< std::vector<int> > & VectKeys  , vector<bool> & vectorIsPresent)
{
	//make all the posible vector of int with the values placed in parameters 
	if(discretisedVector.size() != vectorToPush.size())
	{
		for (int i = 0 ; i < (int)discretisedVector[0].size(); i++)
			{
		vectorToPush.push_back(discretisedVector[vectorToPush.size()][i]);
		this->InsertPotentialVectorWV(discretisedVector,vectorToPush, VectKeys , vectorIsPresent);
		vectorToPush.pop_back();
		}
	}
	else
	{
		VectKeys.push_back(vectorToPush);
		if(this->Data.find(vectorToPush) == this->Data.end())
		vectorIsPresent.push_back(false);
		else
		vectorIsPresent.push_back(true);
	}
}


/*
void DataVector::save(const string & myfilename)
{
	
	const char * filename = myfilename.c_str();
	FILE* myFile = NULL;


    myFile = fopen(filename, "w+");


    if (myFile != NULL)

    {
	
	fprintf(myFile, "%d %d ",this->numberOfElement,this->dim);
	for (std::vector< vector<int> >::iterator it = this->realElements.begin() ; it != this->realElements.end(); ++it)
		{
			 for (vector<int>::iterator itv = it->begin() ; itv != it->end(); ++itv)
			{
				 fprintf(myFile, "%.15lf ",(*itv));
				
			}
			
		}

        
	   fclose(myFile);
    }

    else

    {
        printf("problem with the saving file");
    }



}

*/
void DataVector::load (const string & myfilename){
	ifstream file ( myfilename.c_str(), std::ifstream::in);
	string str;
	vector< std::vector<int> > element;
	int line = 0;
	while ( file.good()){
		 getline ( file, str, '\n' ); // read a string until next comma: http://www.cplusplus.com/reference/string/getline/
	     // we remove the colums.
		 if (line != 0 and str.length() > 0 ){
			 vector<std::string> values =  split(str, SEPARATOR);
			 // insert values in vector.
			 vector<int> vectorValue;
		     for(int i = 1; i < values.size() ; i ++){
		    	 vectorValue.push_back(atoi(values[i].c_str()));
		     }
		     this->realElements.push_back(vectorValue);
	     }

	     line ++;
	}
}


/*

void DataVector::checkPresence(BloomFilter & bloomFilter)
{
	int jump = pow(2,dim);
	int nbMaybe = 0;
	for (std::vector< string >::iterator it = this->stringElements.begin() ; it != this->stringElements.end(); it+=jump)
		{
				for (std::vector< string >::iterator it2 = it ; it2 != it+jump ; ++it2)
			{
				if(bloomFilter.readKey((*it2)))
				{
					nbMaybe++;
					break;
				}
			}
		}
}

*/


DataVector::DataVector()
{
	srand (time(NULL));
	numberOfElement = 0;
	dim = 0;
	domain = 1;
	minRangeSize=1;
	
}



DataVector::DataVector(int myDim, int myNumberOfElement , int domainPower, int myMinRangeSize)
{
	//creat uniforme random vetor with the dimension and in the domain indicate in the parameter
	srand (time(NULL));	
	numberOfElement = myNumberOfElement;
	dim = myDim;
	minRangeSize=myMinRangeSize;
	domain = (int)pow(2,domainPower)*myMinRangeSize;
	vector<int> myvector;
	int myint;
	for(int i = 0 ; i<numberOfElement ; i++)
	{
		myvector.erase (myvector.begin(),myvector.end());
		for(int d = 0 ; d<dim ; d++)
		{
			myint =  rand()%domain;
			myvector.push_back (myint);
		}
		realElements.push_back (myvector);
	}
}

DataVector::DataVector(int myDim, int myNumberOfElement , int domainPower, int myMinRangeSize, string nameFile)
{
	//creat uniforme random vetor with the dimension and in the domain indicate in the parameter
	srand (time(NULL));	
	numberOfElement = myNumberOfElement;
	dim = myDim;
	minRangeSize=myMinRangeSize;
	domain = (int) pow(2,domainPower) * myMinRangeSize;
	vector<int> myvector;
	int myint;

	// get the value from an existing file.
	load(nameFile);
}

DataVector::~DataVector()
{}

//------------------------------------------------------------------ PRIVE

//----------------------------------------------------- Méthodes protégées

//------------------------------------------------------- Méthodes privées
vector<string> DataVector::split(string value, char delimiter){
	vector<string> returnValue;
	string temp = "";
	for(int i = 0; i < value.length(); i++){
		if (value[i] == delimiter){
			returnValue.push_back(temp);
			temp = "";
		}else{
			temp += value[i];
		}
	}
	returnValue.push_back(temp);
	return returnValue;
}
