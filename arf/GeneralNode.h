/*************************************************************************
                           GeneralNode  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//--------------- Class interface <Node> (file GeneralNode.h) -----------
#if ! defined ( GENERALNODE_H )
#define GENERALNODE_H

//--------------------------------------------------- Interfaces utilisées
#include <vector>
#include <string>
#include <iostream>

//------------------------------------------------------------- Constantes 

//------------------------------------------------------------------ Types 

class GeneralNode
{
    protected:
    	GeneralNode* father;


    public:
	GeneralNode* getFather();
    	virtual void printData()=0;
    	virtual ~GeneralNode()=0;
    	virtual bool GetValue();
    	virtual void SetValue();
    	virtual void changeChildValue(GeneralNode* const & ,const bool &);
   	    virtual void ChangeLeafValue(const int & place , const bool & value);
    	virtual void Split(const int leafSplited, const int leafTrue);
	   virtual bool SonIsLeaf(int place); 
};


#endif 
