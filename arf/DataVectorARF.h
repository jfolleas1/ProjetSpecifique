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

#include "ARF.h"

//------------------------------------------------------------- Constantes

//------------------------------------------------------------------ Types

//////////////////////////////////////////////////////////////////  PUBLIC
//------------------------------------------------------  public fonctions


class DataVector
{
private:
	
	int numberOfElement;
	int dim;
	int minRangeSize;
	std::vector< std::vector<int> >realElements;

	int domain;
public:

	DataVector();/// work
	DataVector(int dim, int numberOfElement, int domainPower ,int myMinRangeSize=1);/// work


	void printDataVector(ARF & myARF);/// work
	void toSet(ARF & myARF);/// work
	void checkToSet(ARF & myARF);/// work
	DataVector makeSimilar(const int & similarity, int number =0);/// work
	DataVector(const DataVector & copied);///
	DataVector makeDifferent(const int & similarity, int number =0);/// work
	void AddKey(ARF & myARF); /// work
	void checkPresence(ARF & myARF, bool different); //
	
	void Discretise(ARF & myARF , std::vector<int> Key, std::vector< std::vector<int> > & VectKeys, std::vector<bool> & vectorIsPresent ,int numberOfElementsOnEachSide=1);
	void InsertPotentialVectorWV(ARF & myARF,const std::vector< std::vector<int> > & discretisedVector, std::vector<int> & vectorToPush , std::vector< std::vector<int> > & VectKeys  , std::vector<bool> & vectorIsPresent);
	
	void checkPresenceAround(ARF & myARF, bool different);
	~DataVector();///
/*
	void save(const std::string & filename);
	void load(const std::string & filename);
*/


		

// Mode d'emploi :
//
// Contrat :
//
};
#endif // DATAVECTOR_H

