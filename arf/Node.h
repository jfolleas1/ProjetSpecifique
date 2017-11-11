/*************************************************************************
                           Node  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par jfolleas
*************************************************************************/

//--------------- Class interface <Node> (file Node.h) -----------
#if ! defined ( NODE_H )
#define NODE_H

//--------------------------------------------------- Interfaces utilisées
#include <vector>
#include <string>
#include <iostream>


#include "GeneralNode.h"
#include "Leaf.h"
//------------------------------------------------------------- Constantes 

//------------------------------------------------------------------ Types 



class Node : public GeneralNode
{
//----------------------------------------------------------------- PUBLIC

public:
//---------------------------------------------------- Publics methodes
    // type Méthode ( liste de paramètres );
    // Mode d'emploi :
    //
    // Contrat :
    //

//------------------------------------------------- Surcharge d'opérateurs
    //node & operator = ( const node & unnode );
    // Mode d'emploi :
    //
    // Contrat :
    //
	
	static void SetDim(int myDim);
	static void  SetMinRangeSize(int myMinRangeSize);

    void printData();
	void ChangeLeafValue(const int & place , const bool & value);
	bool SonIsLeaf(int place);
	GeneralNode* getChildNodes(int place);
	void Split(const int LeafSplited);
	bool OnlyGotLeafChild();
	bool LeafGotSameValue();
	Leaf* Merge();
	bool GotUsefulLeafs(const int & min);

//-------------------------------------------- Constructeurs - destructeur
    Node( const Node & MyNode );
    // Mode d'emploi (constructeur de copie) :
    //
    // Contrat :
    //

    Node();
    // Mode d'emploi :
    //
    // Contrat :
    //

    Node(GeneralNode* const & theFather);
//Si on crée le noeud en dessous c'est sensé n'être que des feuille 


    // Mode d'emploi :
    //
    // Contrat :
    //

    ~Node( );
    // Mode d'emploi :
    // Détruit le noeud et tous les fils 
    // Contrat :
    //

//------------------------------------------------------------------ PRIVATE 

private:
//------------------------------------------------------- Private methodes
    Leaf* ChangeChild(GeneralNode* const & childPointer, const bool & value);
	


private:
//------------------------------------------------------- Private attributs

std::vector<GeneralNode *> childNodes;
std::vector<char> childsAreLeaf;
static int dim;
static int minRangeSize;
static int deep;


//----------------------------------------------------------- Types privés

};


#endif // NODE_H
