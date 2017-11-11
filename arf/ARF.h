/*************************************************************************
                           ARF  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//--------------- Class interface <ARF> (file ARF.h) -----------
#if ! defined ( ARF_H )
#define ARF_H

//--------------------------------------------------- Interfaces utilisées
#include <vector>
#include <set>
#include <string>
#include <iostream>

#include "GeneralNode.h"
#include "Node.h"
#include "Leaf.h"
#include "DataVector.h"

//------------------------------------------------------------- Constantes 

//------------------------------------------------------------------ Types 


class DataVector;

class ARF 
{

    private:
	
	int dim;
	int domain;
	int minRangeSize;
	int numberOfNode;
	int numberOfLeaf;
	int numberOfFalsePositif;
	int numberOfTruePositif;
	int numberOfTrueNegatif;
	std::set<Leaf*> myLeafs;
	int targetSize;

	static int minUsefullLeaf;

	//return the place of the adress of the next node on the next general node table 
	/*
		parameters:
		Key : the key that we want to place in the ARF
		middle : the middle of the vectorial range
		represanted by the current node
	*/
   	int nextNode(const std::vector<int> & Key , std::vector<int> & middle);

	// determine the middle and the range size of the next node by compering the key and the middle placed in parameters
	/*
		parameters:
		Key : the key that we want to place in the ARF
		middle : the middle of the vectorial range
		represanted by the current node
		size : the size of the vectorial range on one 
		dimession
	*/
    void nextMiddleAndRangeSize(const std::vector<int> & Key , std::vector<int> & middle, int & size);

    public:

	//function to do a discretasation with pair discretasation
	/*
		parameters:
		Key : the vector that we want to discretise 
		VectKeys : the vector that will containe the
		different key which are the discretisation the the Key
	*/
	void Discretise(std::vector<int> Key, std::vector< std::vector<int> > & VectKeys);

	//used by the previous function to built the coresponding number of vector with the values discretised	
	void InsertPotentialVector(const std::vector<std::pair<int,int> > & discretisedVector, std::vector<int> vectorToPush , std::vector< std::vector<int> > & VectKeys);

	// return the number of false positive.
	int getNumberOfTruePositif();

	// return the number of false positive.
	int getNumberOfFalsePositif();

	// Function to do a discretisation with un unpair number of value discretised
	void DiscretiseWV(std::vector<int> Key, std::vector< std::vector<int> > & VectKeys, int numberOfElementsOnEachSide=1);
	//used by the previous function to built the coresponding number of vector with the values discretised	
	void InsertPotentialVectorWV(const std::vector< std::vector<int> > & discretisedVector, std::vector<int> & vectorToPush , std::vector< std::vector<int> > & VectKeys  );
	
	// Do the split necessary to raise the performaance of the ARF after a false positive answer;
//(Mettre les bit used des leaf cree a true pour le erase qui va suivre)	
	void DoAddapt(DataVector* const & myDV, Leaf* & theDeepestLeaf, const std::vector<int> & middle ,const int & size);
	
	//function to insert data into the ARF without doing any split
	void QuickAddKey(const std::vector<int> & Key, GeneralNode* father);	
	
    public:
	//Allow to determine the minimum number of used bit to do an merge during anthe erase function
	static void SetMinUsefullLeaf(int myMinUsefullLeaf);
	

	GeneralNode* root;
	//reduce the size of the tree to the target size placed in parameter
	void erase();
	//Set all the statistics values to zero 	
	void resetStatistics();
	//Disp the statistic values
	void DispStatistics();
	//return the size in theoric bit of the tree
	int Size();
	//Set the coresponding leaf at true for the key placed in parameter. It make some split if it is necessary to got a leaf range size equal to the min range size.
	void AddKey(std::vector<int> & Key );
	//Verify if a key is exactly in the database
	bool CheckKey(std::vector<int> & Key, bool different);
	//Verify if the database containe a key near enough to the key placed in parameter

	//verify if the data base containe a key which in the neighbor of the query key 
	/*
		parameters:

		myDV: the data of refernece that is used in case of adaptation
		vectKeys : all the discret keys in the neighbor of the query key
		vectorIsPresent : vector of boolean that is set at true if an elements of vectKeys is present in the database
		distantEnough: is set at true if we expecte a false answer
	*/
	void CheckAroundKey( DataVector* const & myDV , std::vector< std::vector<int> > & vectKeys, std::vector<bool> vectorIsPresent, bool distantEnough);

	//return the adress of the leaf which coresponding to the ey placed in parameter 
	/*
		parameter:

		currentNode: the in which we are 
		middle : the middle coresponding to the curent muéti dimentionnal range reprensented by the current node
		size : the size of the range represented by the sons of the current node 
		Key : the key that we want to find the coresponding leaf

	*/
    Leaf* navigate(Node* currentNode, std::vector<int> & middle, int & size,const  std::vector<int> & Key );
	
	//constructor
/*
                parameter:

                dim: the dimenssion of the data in the data base
                minRangeSize : the minimum size of a range which can be represented by a leaf
                domainPower : the power of two that will be multiplied by minRangeSize that will make the size of the entier domaine
		myTargetSize : the size that we expect for the filter

        */
    ARF(const int & dim, const int & minRangeSize, const int &  domainPower, const int & myTargetSize);
	//destructor 
    ~ARF();

	//print the ARF tree 
    void printARF();
    

};

#endif // ARF_H
