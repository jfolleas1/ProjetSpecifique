/*************************************************************************
                          Leaf  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//------------------ class <Leaf> (file Leaf.cpp) -----------------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <math.h>

//------------------------------------------------------ Include personnel
#include "Leaf.h"

bool Leaf::GetValue()
{
return value;
}

void Leaf::ChangeLeafValue(const int & place , const bool & value)
{
	this->SetValue(value);
}

void Leaf::SetValue(const bool & myValue )
{
	value=myValue;
}
   

Leaf::Leaf( GeneralNode* const & myFather, const bool & myValue)
{
	used=false;
    father=myFather;
    value=myValue;
}


Leaf::Leaf()
{
	used=false;
    father=NULL;
    value=0;
}

Leaf::~Leaf()
{}//bloc vide


void Leaf::printData()
{
        cout<<"Leaf: v="<<value<<"\tpt ="<<this<<endl;
}
    
