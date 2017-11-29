/*************************************************************************
                           Leaf  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//--------------- Class interface <Leaf> (file Leaf.h) -----------
#if ! defined ( LEAF_H )
#define LEAF_H

//--------------------------------------------------- Interfaces utilisées
#include <vector>
#include <string>
#include <iostream>

#include "GeneralNode.h"

//------------------------------------------------------------- Constantes 

//------------------------------------------------------------------ Types 




class Leaf : public GeneralNode
{

    private:
    bool value;
    
    
    
    public:
    bool used;
    bool GetValue();
	void ChangeLeafValue(const int & place , const bool & value);
    void SetValue(const bool & myValue );
   

    Leaf( GeneralNode* const & myFather, const bool & myValue);

    Leaf();

    ~Leaf();

    void printData();
    

};

#endif // LEAF_H
