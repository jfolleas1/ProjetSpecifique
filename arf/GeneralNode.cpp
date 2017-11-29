/*************************************************************************
                           GeneralNode  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//------------------ class <GeneralNode> (file GeneralNode.cpp) -----------------

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>
#include <vector>

//------------------------------------------------------ Include personnel
#include "GeneralNode.h"

 GeneralNode::~GeneralNode()
{}


GeneralNode* GeneralNode::getFather()
{return this->father;}

bool GeneralNode::SonIsLeaf(int place)
{return false;}

bool GeneralNode::GetValue()
{return true;}

void GeneralNode::Split(const int leafSplited, const int leafTrue)
{}

void GeneralNode::SetValue()
{}

void GeneralNode::ChangeLeafValue(const int & place , const bool & value)
{}

void GeneralNode::changeChildValue(GeneralNode* const & ,const bool &)
{}
