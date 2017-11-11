/*************************************************************************
                           Commande  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par lhammel
*************************************************************************/

//---------- Interface de la classe <Commande> (fichier Commande.h) ------
#if ! defined ( COMMANDE_H )
#define COMMANDE_H

//--------------------------------------------------- Interfaces utilisées
#include <vector>
#include <string>
using namespace std;

#include "Modele.h"
//------------------------------------------------------------- Constantes 

//------------------------------------------------------------------ Types 
class Modele;
//------------------------------------------------------------------------ 
// Rôle de la classe <Commande>
//
// La classe Commande permet d'executer une commande appelée et de vérifier
//que les arguments sont bien rentrés.
//------------------------------------------------------------------------ 

class Commande
{
//----------------------------------------------------------------- PUBLIC

public:
//----------------------------------------------------- Méthodes publiques
    // type Méthode ( liste de paramètres );
    // Mode d'emploi :
    //
    // Contrat :
    //
    string getNomCommande();

//------------------------------------------------- Surcharge d'opérateurs
    //Commande & operator = ( const Commande & unCommande );
    // Mode d'emploi :
    //
    // Contrat :
    //


//-------------------------------------------- Constructeurs - destructeur
    Commande ( const Commande & uneCommande );
    // Mode d'emploi (constructeur de copie) :
    //
    // Contrat :
    //

    Commande (string args);
    // Mode d'emploi :
    //
    // Contrat :
    //

    Commande (string args, bool silence);
    // Mode d'emploi :
    //
    // Contrat :
    //

    virtual ~Commande ( );
    // Mode d'emploi :
    //
    // Contrat :
    //

//------------------------------------------------------------------ PRIVE 

protected:
//----------------------------------------------------- Méthodes protégées

private:
//------------------------------------------------------- Méthodes privées
    void executerCommande();
    // Mode d'emploi :
    //
    // Contrat :
    //

    vector<int> decouperArgsInt(const string ligne, char delim);
    // Mode d'emploi :
    //
    // Contrat :
    //

    vector<int> &decouperArgsInt(const string &s, char delim, vector<int> &elems);
    // Mode d'emploi :
    //
    // Contrat :
    //

    vector<string> decouperArgsString(const string ligne, char delim);
    // Mode d'emploi :
    //
    // Contrat :
    //

    vector<string> &decouperArgsString(const string &s, char delim, vector<string> &elems);
    // Mode d'emploi :
    //
    // Contrat :
    //

    void ecrireSauvegarde(string nomFichier);

    vector<string> separerNomCommande(string aArgs);



protected:
//----------------------------------------------------- Attributs protégés

    string nomCommande = ""; //Le nom principal de notre commande
    string arguments = "";   //Les arguments suivant le nom de la commande
    string message = "";     //Le commentaire à afficher après le resultat de la commande
    bool erreur = false;     //Permet de savoir si une erreur est survenue a l'appel de la commande


private:
//------------------------------------------------------- Attributs privés
static Modele modele;
//---------------------------------------------------------- Classes amies

//-------------------------------------------------------- Classes privées

//----------------------------------------------------------- Types privés

};

//----------------------------------------- Types dépendants de <Commande>

#endif // COMMANDE_H
