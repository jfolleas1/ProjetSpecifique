/*************************************************************************
                           DataVector.h -  description
                             -------------------
    date                 : 16/06/2016
    copyright            : (C) 2016 par jacques folleas
    e-mail               : jacques.folleas@insa-lyon.fr
*************************************************************************/

//------- Interface of the class <DataVector> (file DataVector.h) --------
#if ! defined ( DATAVECTOR_H )
#define DATAVECTOR_H

//------------------------------------------------------------------------
// Rôle de la classe <DataVector>
//
//
//------------------------------------------------------------------------

/////////////////////////////////////////////////////////////////  INCLUDE
//-------------------------------------------------------- Interfaces used

#include <iostream>
#include <vector>
#include <stdlib.h>
#include <sstream>
#include <set>
#include <fstream>

#include "ARF.h"

//------------------------------------------------------------- Constantes

//------------------------------------------------------------------ Types

//////////////////////////////////////////////////////////////////  PUBLIC
//------------------------------------------------------  public fonctions


class ARF;

class DataVector
{
private:
	int numberOfElement;
	int dim;
	int minRangeSize;
	std::vector< std::vector<int> >realElements;
	int domain;

	std::vector<std::string> split(std::string value, char delimiter);

public:
	//containe the discretised value that will use the ARF for the adaptation
	std::multiset< std::vector<int> >Data;

	DataVector();/// work
	DataVector(int dim, int numberOfElement, int domainPower ,int myMinRangeSize=1);/// work
	DataVector(int dim, int numberOfElement, int domainPower ,int myMinRangeSize,
					std::string nameFile);/// work

	//print all the data with real value and discretised values
	void printDataVector();/// work
	
	//discretise all the real value and put all the vector in the multiset
	void toSet();/// work

	//unused
	void checkToSet();/// work
	

	//Creat an objet data vector with near vector compar to the similarity placed in parameter and with the number of vector indicate in the parametrs
	/*
		parameters :

		similarity : the maximum distant between the created vector and the reference vector on each dimension
		number : the number of vector that will be creat
	*/
	DataVector makeSimilar(const int & similarity, int number =0);/// work
	
	//copy constructor 
	DataVector(const DataVector & copied);///
	


	 //Creat an objet data vector with the good number of distant enough vector compar to the similarity placed in parameters
        /*
                parameters :

                similarity : the minimum distant between the created vector and all the vector in the DataVector object that call the fonction
                number : the number of vector that will be creat
        */
	DataVector makeDifferent(const int & similarity, int number =0);/// work
	
	//Turn at true the leafs coresponding to all the data in the DataVector caller in the ARF placed in parameters
	/*
		parameters : 
		
		myARF : the ARF that will be modified
	*/
	void AddKey(ARF & myARF); /// work

	//unused
	void checkPresence(ARF & myARF, bool different); //
	
//should be private 
	void Discretise(std::vector<int> Key, std::vector< std::vector<int> > & VectKeys, std::vector<bool> & vectorIsPresent ,int numberOfElementsOnEachSide=1);
	void InsertPotentialVectorWV(const std::vector< std::vector<int> > & discretisedVector, std::vector<int> & vectorToPush , std::vector< std::vector<int> > & VectKeys  , std::vector<bool> & vectorIsPresent);
	

	//Creat the neighbor vector and the boolean vector that answer if a vector is prensent in the data base and ask to the ARF 
	/*
		parameters :
		myARF : the filter that will answer to the querys
		different : set at true if the query keys are distant enough to the vectors in the database
		DataBase : pointeur to the data base used for the addaptation
	*/	
void checkPresenceAround(ARF & myARF, bool different, DataVector* DataBase);
	~DataVector();///

	void save(const std::string & filename);
	void load(const std::string & filename);


		

// Mode d'emploi :
//
// Contrat :
//
};
#endif // DATAVECTOR_H

