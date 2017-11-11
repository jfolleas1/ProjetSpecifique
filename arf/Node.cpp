/*************************************************************************
                           Node  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//------------------ class <Node> (file Node.cpp) -----------------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <math.h>

//------------------------------------------------------ Include personnel
#include "Node.h"
//#include "Util.hpp"
//------------------------------------------------------------- Constantes
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int BIT_SIZE_OF_CHAR =8;
//---------------------------------------------------- Class variables
int Node::dim = 1;
int Node::minRangeSize = 1;
int Node::deep = 0;
//----------------------------------------------------------------- PRIVATE

	bool Node::LeafGotSameValue()
	{
		for(vector<GeneralNode*>::iterator it = childNodes.begin(); it != childNodes.end(); it++)
		{ 
		if((Leaf*)(*it)->GetValue() != (Leaf*)(*childNodes.begin())->GetValue())
			return false;		
		}
		return true;
	}

	bool Node::OnlyGotLeafChild()
	{
		for(vector<char>::iterator it = childsAreLeaf.begin(); it != childsAreLeaf.end(); it++)
		{ 
		if((*it) != (char)MIN( ((int)pow(2,pow(2,dim))-1), 255 ) )
			return false;		
		}
		return true;
	}

	void Node::SetDim(int myDim)
	{
		dim=myDim;
	}

	void Node::SetMinRangeSize(int myMinRangeSize)
	{
		minRangeSize=myMinRangeSize;
	}

	//When a node necome a leaf
Leaf* Node::ChangeChild(GeneralNode* const & childPointer, const bool & value)
	{
		int place = 0;
		for (std::vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
			if( (*it) == childPointer )
			{
				
				
				place=it-childNodes.begin();
				childNodes[place]=new Leaf(this,value);
				childsAreLeaf[(place/BIT_SIZE_OF_CHAR)] |= ((int)pow(2,(place%BIT_SIZE_OF_CHAR)));
				
			}
		}
	return (Leaf*)childNodes[place];	
	}

	void Node::ChangeLeafValue(const int & place , const bool & value)
	{
		childNodes[place]->ChangeLeafValue(place,value);
	}

	//When a leaf become node
	void Node::Split( const int LeafSplited)
	{
		

		
		delete childNodes[LeafSplited];

		childNodes[LeafSplited]=new Node(this);



				
		
		childsAreLeaf[(LeafSplited/BIT_SIZE_OF_CHAR)] &= (255-((int)pow(2,(LeafSplited%BIT_SIZE_OF_CHAR))));
				

	}

	bool Node::SonIsLeaf(int place)
	{
		int res = childsAreLeaf[(place/BIT_SIZE_OF_CHAR)] & ((int)pow(2,(place%BIT_SIZE_OF_CHAR)));
		if (res != 0)
		{	return true;
		}
		else
		{	return false;
		}
	
	}

//----------------------------------------------------------------- PUBLIC

//----------------------------------------------------- Méthodes publiques

	GeneralNode* Node::getChildNodes(int place)
	{
		return this->childNodes[place];
	}


	void Node::printData()
	{
		deep++;
		cout<<"Node"<<" DT=";
		for (vector<char>::iterator it = --childsAreLeaf.end() ; it != --childsAreLeaf.begin(); it--)
		{	for(int i =7; i>=0;i--)
			cout<<((((int)(*it))&((int)pow(2,i)))/pow(2,i));
		}
		cout<<"\r\n";
		for (vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
			for(int i =0 ; i <deep ; i++)
			cout<<"\t";
			(*it)->printData();
		}
		deep--;
	}

	Node::Node ( const Node & myNode)
	{
		
		for (std::vector<GeneralNode *>::const_iterator it = myNode.childNodes.begin() ; it != myNode.childNodes.end(); ++it)
		{
			childNodes.push_back(*it);
		}
		for (std::vector<char>::const_iterator it = myNode.childsAreLeaf.begin() ; it != myNode.childsAreLeaf.end(); ++it)
		{
			childsAreLeaf.push_back(*it);
		}
		father=myNode.father;
	}

	

    Node::Node()
	{
		for (vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
			childNodes.push_back(NULL);
		}
		childsAreLeaf.push_back(0);
		father=NULL;
	}


    Node::Node ( GeneralNode* const & theFather)
	{
		father=theFather;
		for (int i = 0; i <  pow(2,dim);i++ )
		{
			Leaf * ptLeaf=new Leaf(this,false);
			childNodes.push_back(ptLeaf);
		}
		if(dim<3)
		{	char a = pow(2,pow(2,dim))-1;
			childsAreLeaf.push_back(a);
		}
		else 
		{
			for(int i = 0 ; i< pow(2,dim)/BIT_SIZE_OF_CHAR ; i++)
			{
				char a = 0;
				a |= 255;
				childsAreLeaf.push_back(a);
			}
		}
	}

Leaf* Node::Merge()
{
	bool leafValue=false;
	int myInt=0;
	
	for (std::vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
			myInt=it-childNodes.begin();
			if( (childsAreLeaf[(myInt/BIT_SIZE_OF_CHAR)] & (int)pow(2,(myInt%BIT_SIZE_OF_CHAR))) !=0)
			{
				
				leafValue|=(*it)->GetValue();
			} 
		}
	Node * father = (Node*)(this->getFather());
	Leaf* myLeaf = ((Node*)(father))->ChangeChild(this, leafValue);	
	return myLeaf ;

}

	
//Si on crée le noeud en dessous c'est sensé n'être que des feuille 


    // Mode d'emploi :
    //
    // Contrat :
    //

    Node::~Node ( )
	{
		for (std::vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
		
			delete (*it);
		}
	}    
// Mode d'emploi :
    // Détruit le noeud et tous les fils 
    // Contrat :
    //


bool Node::GotUsefulLeafs(const int & min)
{
	int numberOfUsefulLeaf=0;
	for (std::vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
		
			if((((Leaf*)(*it))->used)==true)
			numberOfUsefulLeaf++;
		}
	if(numberOfUsefulLeaf > min)
	{
		for (std::vector<GeneralNode *>::iterator it = childNodes.begin() ; it != childNodes.end(); ++it)
		{
			(((Leaf*)(*it))->used)=false;
		}
		return true;
	}
	else 
	{
		return false;
	}



}



