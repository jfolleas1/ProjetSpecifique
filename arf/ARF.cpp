/*************************************************************************
                          ARF  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//------------------ class <ARF> (file Leaf.cpp) -----------------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <math.h>

//------------------------------------------------------ Include personnel
#include "ARF.h"


//---------------------------------------------------- Class variables
int ARF::minUsefullLeaf = 1;
int nbrOfAddaptationBeforeErase = 0;
Leaf* lastErased=NULL;

void ARF::SetMinUsefullLeaf(int myMinUsefullLeaf)
	{
		minUsefullLeaf=myMinUsefullLeaf;
	}

//the first dimension is the strongest weight bit
int ARF::nextNode(const vector<int> & Key , vector<int> & middle)
{
	int nextNode = 0;
	for(int i = 1; i <= dim ; i++)
	{
		if (Key[i-1]>middle[i-1])
		{
			nextNode|=(int)pow(2,dim-i);
		}
	}
	return nextNode;
}


void ARF::nextMiddleAndRangeSize(const vector<int> & Key , vector<int> & middle, int & rangeSize)
{
	
	for(int i = 0; i < dim ; i++)
	{
		if (Key[i]>middle[i])
		{
			middle[i] += rangeSize/2;
		}
		else
		{
			middle[i] -= rangeSize/2;
		}
	}
    rangeSize/=2;
}


Leaf* ARF::navigate(Node* currentNode, vector<int> & middle, int & rangeSize ,const vector<int> & Key )
{	
	//We look who is the next general node on the pointeur table
	int myNextNode = this->nextNode(Key,middle);
	//If it's a leaf we return his address
	if(currentNode->SonIsLeaf(myNextNode))
	{
		return (Leaf*)currentNode->getChildNodes(myNextNode);
	}
	else
	{
		//else we continue deeper in the tree
		currentNode=(Node*)currentNode->getChildNodes(myNextNode);
		this->nextMiddleAndRangeSize(Key, middle, rangeSize);
	return this->navigate(currentNode,middle,rangeSize,Key);
	}
}

void ARF::AddKey(vector<int> & Key)
{
    int rangeSize = (this->domain)/2;
    int place=-1;
    Node* currentNode = (Node*)this->root;
    Leaf* theDeepestLeaf = NULL;
    vector<int>  middle;
    middle.clear();
    for (int i =0; i<this->dim; i++)
    middle.push_back(domain/2);

//we find the deepest leaf and split it if it corresponding to a too much big range 
    while(rangeSize>minRangeSize)
    {

        theDeepestLeaf=this->navigate(currentNode, middle,rangeSize,Key);//test OK
        currentNode=(Node*)theDeepestLeaf->getFather();
        
        for(int i = 0 ; i<pow(2,this->dim); i++)
        {
            if(currentNode->getChildNodes(i)==(GeneralNode*)theDeepestLeaf)
            {
                place=i;
                break;
            }
        }
        if(rangeSize>minRangeSize)
        { //we update the set of the leafs
	myLeafs.erase((Leaf*)(currentNode->getChildNodes(place)));
        currentNode->Split(place);//
	for(int i =0 ; i < (int)pow(2,dim);i++)	
	myLeafs.insert((Leaf*)(((Node*)(currentNode->getChildNodes(place)))->getChildNodes(i)));
        numberOfNode++;
        numberOfLeaf+=((int)pow(2,dim)-1);        
        }
        
    }
	 
    theDeepestLeaf->SetValue(true);
}


bool ARF::CheckKey(vector<int> & Key, bool different)
{
    int rangeSize = (this->domain)/2;
    Node* currentNode = (Node*)this->root;
    Leaf* theDeepestLeaf = NULL;
    vector<int>  middle;
    for (int i =0; i<this->dim; i++)
    middle.push_back(domain/2); 
       
    theDeepestLeaf=this->navigate(currentNode, middle,rangeSize,Key);
    theDeepestLeaf->used=true;
	if(theDeepestLeaf->GetValue())
	{ 	
		if(different)
		numberOfFalsePositif++;
		else
		numberOfTruePositif++;
	return true;
	}
	else
	{
		numberOfTrueNegatif++;
	return false;
	}

}

void ARF::DiscretiseWV(std::vector<int> Key, std::vector< std::vector<int> > & VectKeys, int numberOfElementsOnEachSide)
{
	vector < vector <int> > discretisedVector;
	vector <int> myDiscretisedElements;
	vector <int> vectorToPush;
	int myDiscretisedValue=0;
	//We find all the value and put it into a vector
	for (std::vector< int >::iterator it = Key.begin() ; it != Key.end(); ++it)
	{
		myDiscretisedValue=(((*it)-1)/(minRangeSize))*(minRangeSize);
		myDiscretisedElements.push_back(myDiscretisedValue);
		myDiscretisedElements[0]+=(minRangeSize/2)+1;
		for(int i=1; i< numberOfElementsOnEachSide+1; i++)
		{
			myDiscretisedElements.push_back(myDiscretisedElements[0]+i*minRangeSize);
			myDiscretisedElements.push_back(myDiscretisedElements[0]-i*minRangeSize);
						
		}
		discretisedVector.push_back (myDiscretisedElements);
		myDiscretisedElements.erase(myDiscretisedElements.begin(), myDiscretisedElements.end());
	}
	//we shuffle all the value to built any possibl vector near enough
	this->InsertPotentialVectorWV(discretisedVector,vectorToPush, VectKeys );
}

void ARF::InsertPotentialVectorWV(const vector< vector<int> > & discretisedVector, vector<int> & vectorToPush , std::vector< std::vector<int> > & VectKeys  )
{
	if(discretisedVector.size() != vectorToPush.size())
	{
		for (int i = 0 ; i < (int)discretisedVector[0].size(); i++)
			{
		vectorToPush.push_back(discretisedVector[vectorToPush.size()][i]);
		this->InsertPotentialVectorWV(discretisedVector,vectorToPush, VectKeys );
		vectorToPush.pop_back();
		}
	}
	else
	{
		VectKeys.push_back(vectorToPush);
	}
}

void ARF::Discretise(std::vector<int> Key, std::vector< std::vector<int> > & VectKeys )
{
	
	vector < pair <int,int> > discretisedVector;
	pair <int,int> mypair;
	vector <int> vectorToPush;
	int myDiscretisedValue=0;
	
			discretisedVector.erase (discretisedVector.begin(),discretisedVector.end());
			for (std::vector< int >::iterator it = Key.begin() ; it != Key.end(); ++it)
			{
				myDiscretisedValue=((*it)/(minRangeSize))*(minRangeSize);
				mypair.first=myDiscretisedValue;
				mypair.first+=(minRangeSize/2)+1;
				if( mypair.first>(*it) )
				{
					if(mypair.first-minRangeSize>0)
					mypair.second=mypair.first-minRangeSize;
					else
					mypair.second=mypair.first;
				}
				else
				{
					if(mypair.first+minRangeSize<=domain)
					mypair.second=mypair.first+minRangeSize;
					else
					mypair.second=mypair.first;
				}
				discretisedVector.push_back (mypair);
				
			}
			vectorToPush.erase (vectorToPush.begin(),vectorToPush.end());
			this->InsertPotentialVector(discretisedVector,vectorToPush, VectKeys );
}




void ARF::InsertPotentialVector(const vector<pair<int,int> > & discretisedVector, vector<int> vectorToPush , std::vector< std::vector<int> > & VectKeys  )
{
	if(discretisedVector.size() != vectorToPush.size())
	{
		vectorToPush.push_back(discretisedVector[vectorToPush.size()].first);
		this->InsertPotentialVector(discretisedVector,vectorToPush, VectKeys );
		vectorToPush.pop_back();
		vectorToPush.push_back(discretisedVector[vectorToPush.size()].second);
		this->InsertPotentialVector(discretisedVector,vectorToPush , VectKeys);
	}
	else
	{
		VectKeys.push_back(vectorToPush);
	}
}

void ARF::CheckAroundKey(DataVector* const & myDV, vector< vector<int> > & vectKeys, vector<bool> vectorIsPresent, bool distantEnough)
{

	int size;
	Node* currentNode;
	Leaf* theDeepestLeaf;
	vector<int>  middle;
	bool answerOfARF=false;

	
//For all the discretised and near vector we find the leaf coresponding 
	for(vector< vector<int> >::iterator it = vectKeys.begin(); it!= vectKeys.end(); it++)
	{
		
		size = (this->domain)/2;
		currentNode = (Node*)this->root;
		theDeepestLeaf = NULL;
	   	middle.clear();
	    	for (int i =0; i<this->dim; i++)
	    	middle.push_back(domain/2); 
	       
	    	theDeepestLeaf=this->navigate(currentNode, middle,size,(*it));
	
	
	    theDeepestLeaf->used=true;

		answerOfARF|=theDeepestLeaf->GetValue();
	//And we update the tree if it is necessary 
		if(!(vectorIsPresent[it-vectKeys.begin()]) && theDeepestLeaf->GetValue() )
		{
			
			this->nextMiddleAndRangeSize((*it),middle,size);
			

			this->DoAddapt(myDV, theDeepestLeaf, middle , size);
		}
	
		
	}
		if(answerOfARF)
		{	
			if(distantEnough)
			numberOfFalsePositif++;
			else
			numberOfTruePositif++;
		}
		else
		{
			numberOfTrueNegatif++;
		}

}


void ARF::DoAddapt(DataVector* const & myDV, Leaf* & theDeepestLeaf , const std::vector<int> & middle ,const int & size)
{


	int place = -1;	

		
	Node* father = (Node*)theDeepestLeaf->getFather();
	for(int i = 0; i< (int)pow(2,dim); i++)
	{	
		if(theDeepestLeaf==(Leaf*)father->getChildNodes(i))
		place = i;
	}
//Wee insert the news leafs in the set and remoove the older
	myLeafs.erase((Leaf*)(father->getChildNodes(place)));
	father->Split(place);
	
	for(int i =0 ; i < (int)pow(2,dim);i++)	
	{
	myLeafs.insert((Leaf*)(((Node*)(father->getChildNodes(place)))->getChildNodes(i)));
	((Leaf*)(((Node*)(father->getChildNodes(place)))->getChildNodes(i)))->used = true;
	}
        numberOfNode++;
        numberOfLeaf+=((int)pow(2,dim)-1);    

//We set at true the leafs which coresponding to present data 
	for(set< vector<int> >::const_iterator itData = myDV->Data.begin();itData != myDV->Data.end(); itData++ )
	{
		 this->QuickAddKey(*itData,(father->getChildNodes(place)));
	}
	nbrOfAddaptationBeforeErase++;
	if((nbrOfAddaptationBeforeErase%5)==0)
	this->erase();
}


void ARF::QuickAddKey(const std::vector<int> & Key, GeneralNode* father)
{
//we verify if for all the data the coresponding leaf is set at true 
	int rangeSize;
	std::vector<int> middle;
	Node* currentNode;
	Leaf* theDeepestLeaf = NULL;
	rangeSize=domain/2;
	middle.clear();
	for(int i = 0 ; i<dim ; i++)
	middle.push_back(domain/2);
	currentNode= (Node*)root ;
	theDeepestLeaf=this->navigate(currentNode, middle,rangeSize,Key);//test OK
	if(!(theDeepestLeaf->GetValue()) && (theDeepestLeaf->getFather()!=father) )//look if the seted leaf at true is normal
	cout<<"PB"<<endl;
    	theDeepestLeaf->SetValue(true);
}

//Constructor
ARF::ARF(const int & myDim, const int & myMinRangeSize,const int & myDomain, const int & myTargetSize)
	{
		targetSize=myTargetSize;
		numberOfFalsePositif=0;
		numberOfTruePositif=0;
		numberOfTrueNegatif=0;
		domain=(int)pow(2,myDomain)*myMinRangeSize;
		dim=myDim;
		Node::SetDim(dim);
		minRangeSize=myMinRangeSize;
		Node::SetMinRangeSize(minRangeSize);
		root = new Node(NULL);
		for(int i =0 ; i < (int)pow(2,dim);i++)
		myLeafs.insert((Leaf*)(((Node*)root)->getChildNodes(i)));

        numberOfNode=1;
        numberOfLeaf=(int)pow(2,dim);
	}

int ARF::Size(){
//we return the number of bit
	return numberOfNode*(int)pow(2,dim)+numberOfLeaf*2;
}

/**
 * Return the number of true positive. 
 * @return [description]
 */
int ARF::getNumberOfTruePositif(){
		return numberOfTruePositif;
}

/**
 * Return the number of false positive. 
 * @return [description]
 */
int ARF::getNumberOfFalsePositif(){
		return numberOfFalsePositif;
}

void ARF::resetStatistics(){
		numberOfFalsePositif=0;
		numberOfTruePositif=0;
		numberOfTrueNegatif=0;
}


void ARF::erase(){
	bool reduced = true;
	while(reduced){
		reduced = false;
		//we begin by merging all the leaf which got the same value which containe no added information 
		std::set<Leaf*>::iterator it;
	 	for ( it=myLeafs.find(lastErased) ; it!=myLeafs.end(); ++it){
			if(((Node*)((*it)->getFather()))->OnlyGotLeafChild() && ((Node*)((*it)->getFather()))->LeafGotSameValue()){
				reduced=true;	
				Node* father=(Node*)((*it)->getFather());

				for(int i = 0 ; i < (int)pow(2,dim); i++)
				myLeafs.erase((Leaf*)(father->getChildNodes(i)));
				numberOfLeaf-=pow(2,dim);

				lastErased=father->Merge();
				myLeafs.insert(lastErased);
				delete father;
				numberOfNode--;
				numberOfLeaf++;	
				break;
			}
		}
		if (it == myLeafs.end()){
			lastErased = (*(myLeafs.begin()));
		}
	}

	//If it's not enough we merge the leafs which was not requested recently
	while(this->Size()> targetSize){
		for (std::set<Leaf*>::iterator it=myLeafs.begin(); it!=myLeafs.end(); ++it){
			if(((Node*)((*it)->getFather()))->OnlyGotLeafChild()){
				if( !((Node*)((*it)->getFather()))->GotUsefulLeafs(minUsefullLeaf)){
				Node* father=(Node*)((*it)->getFather());

				for(int i = 0 ; i < (int)pow(2,dim); i++){
					myLeafs.erase((Leaf*)(father->getChildNodes(i)));
				}

				myLeafs.insert(father->Merge());
				delete father;

				numberOfNode--;
        			numberOfLeaf-=((int)pow(2,dim)-1);	

				}

				if(this->Size()< targetSize){
					break;
				}

				for(int i = 0 ; i < 4*(int)pow(2,dim); i++)
				it++;
			}
		}
	}
}


void ARF::DispStatistics()
{
		cout<<"FP : "<<100*numberOfFalsePositif/(0.0+numberOfFalsePositif+numberOfTruePositif+numberOfTrueNegatif)<<endl;
		cout<<"TP : "<<100*numberOfTruePositif/(0.0+numberOfFalsePositif+numberOfTruePositif+numberOfTrueNegatif)<<endl;
		cout<<"TN : "<<100*numberOfTrueNegatif/(0.0+numberOfFalsePositif+numberOfTruePositif+numberOfTrueNegatif)<<endl;
}

ARF::~ARF()
	{
		delete root;
		//all the other node are delete in cascade
	}

void ARF::printARF()
	{
		cout<<"dom="<<domain<<"dim="<<dim<<" R="<<minRangeSize<<endl;
	        root->printData();
	}
