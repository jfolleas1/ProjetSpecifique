/*************************************************************************
                           Commande  -  description
                             -------------------
    début                : 22/01/2016
    copyright            : (C) 2016 par lhammel
*************************************************************************/

//---------- Réalisation de la classe <Commande> (fichier Commande.cpp) --

//---------------------------------------------------------------- INCLUDE

//-------------------------------------------------------- Include système
using namespace std;
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

//------------------------------------------------------ Include personnel
#include "Commande.h"
#include "Modele.h"
#include "Point.h"
//------------------------------------------------------------- Constantes

//vector <Commande> Commande::histoCommandes;
//Modele Commande::modele;
//---------------------------------------------------- Variables de classe

//----------------------------------------------------------- Types privés
Modele Commande::modele;

//----------------------------------------------------------------- PUBLIC
//-------------------------------------------------------- Fonctions amies

//----------------------------------------------------- Méthodes publiques
// type Commande::Méthode ( liste de paramètres )
// Algorithme :
//
//{
//} //----- Fin de Méthode
string Commande::getNomCommande()
{
	return nomCommande;
}


//------------------------------------------------- Surcharge d'opérateurs
/*
Commande & Commande::operator = ( const Commande & uneCommande )
// Algorithme :
//
{
} //----- Fin de operator =
*/

//-------------------------------------------- Constructeurs - destructeur
Commande::Commande ( const Commande & uneCommande )
// Algorithme :
//
{
#ifdef MAP
    cout << "Appel au constructeur de copie de <Commande>" << endl;
#endif
    nomCommande = uneCommande.nomCommande;
    arguments = uneCommande.arguments;
   
} //----- Fin de Commande (constructeur de copie)


Commande::Commande (string args)
// Algorithme :
//
{
#ifdef MAP
    cout << "Appel au constructeur de <Commande>" << endl;
#endif

    vector <string> v = separerNomCommande(args);

    nomCommande = v.at(0);
	arguments = v.at(1);

	executerCommande();

	if ((nomCommande == "S" || nomCommande == "PC" || nomCommande == "R" 
		|| nomCommande == "OR" || nomCommande == "OI" || nomCommande == "LOAD" 
		|| nomCommande == "MOVE" || nomCommande == "DELETE") 
		&& !erreur)
	{
		modele.insertCommandeUndoable(this);
	}


} //----- Fin de Commande

Commande::Commande (string args, bool silence)
// Algorithme :
//
{
#ifdef MAP
    cout << "Appel au constructeur de <Commande>" << endl;
#endif

    vector <string> v = separerNomCommande(args);

    nomCommande = v.at(0);
	arguments = v.at(1);

	executerCommande();


} //----- Fin de Commande

Commande::~Commande ( )
// Algorithme :
//
{
#ifdef MAP
    cout << "Appel au destructeur de <Commande>" << endl;
#endif
} //----- Fin de ~Commande


//------------------------------------------------------------------ PRIVE

//----------------------------------------------------- Méthodes protégées

//------------------------------------------------------- Méthodes privées

void Commande::executerCommande()
// Algorithme :
//
{

	if (nomCommande == "S")	
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un nom puis les coordonnées de 2 points";
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);


			if (vecteurNomArgs.at(1).length() < 1)
			{
				erreur = true;
				message = "Veuillez entrer un nom puis les coordonnées de 2 points";
			}
			else
			{
				
				vector<int> argsVector = decouperArgsInt(vecteurNomArgs.at(1), ' ');

				//Verifie qu'une figure porte deja ce nom
				if (modele.nomDispo(vecteurNomArgs.at(0)))
				{
					//Regarde si on a un bon nombre d'arguments
					if (argsVector.size() != 4)
					{
						erreur = true;
						message = "Veuillez entrer un nom puis les coordonnées de 2 points";
					}
					else
					{
					
						//Changer le vecteur de int en vecteur de point
						vector<Point> Vpoints;
						for(unsigned int u=0 ; u<argsVector.size(); u+=2)
						{	
							Point pt(argsVector[u],argsVector[u+1]);
							Vpoints.insert(Vpoints.end(),pt);
						}
						
						//Appel du constructeur de Segment
						modele.insertion(vecteurNomArgs.at(0), nomCommande, Vpoints);
						message = "Segment " + vecteurNomArgs.at(0) + " créé";
					
					}
				}
				else
				{
					erreur = true;
					message = "Nom déjà utilisé";
				}
			}
		}
	}

	else if (nomCommande == "R")	
	{

		if (arguments.length() < 1)
		{
			erreur = true;
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			//Verifie qu'une figure porte deja ce nom
			if (modele.nomDispo(vecteurNomArgs.at(0)))
			{
				if (vecteurNomArgs.at(1).length() < 1)
				{
					erreur = true;
				}
				else
				{
					vector<int> argsVector = decouperArgsInt(vecteurNomArgs.at(1), ' ');
					
					//Regarde si on a un bon nombre d'arguments
					if (argsVector.size() != 4)
					{
						erreur = true;
					}
					else
					{
						//Vérifie que les point peuvent former un rectangle
						if((argsVector.at(0) <= argsVector.at(2)) && (argsVector.at(1) >= argsVector.at(3)))
						{	
							//Changer le vecteur de int en vecteur de point
							vector<Point> Vpoints;
							for(unsigned int u=0 ; u<argsVector.size(); u+=2)
							{	
								Point pt(argsVector[u],argsVector[u+1]);
								Vpoints.insert(Vpoints.end(),pt);
							}
							
							//Appel du constructeur de Rectangle
							modele.insertion(vecteurNomArgs.at(0), nomCommande, Vpoints);
							message = "Rectangle " + vecteurNomArgs.at(0) + " créé";
						}
						else
						{
							erreur = true;
						}
					}
				}
			}
			else
			{
				erreur = true;
			}
		}

		if (erreur)
		{
			message = "Veuillez entrer un nom non utilisé puis les coordonnées de 2 points";
		}
	}

	else if (nomCommande == "PC")	
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un nom puis les coordonnées d'une suite de points";
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			//Verifie qu'une figure porte deja ce nom
			if (modele.nomDispo(vecteurNomArgs.at(0)))
			{
				if (vecteurNomArgs.at(1).length() < 1)
				{
					erreur = true;
					message = "Veuillez entrer un nom puis les coordonnées d'une suite de points";
				}
				else
				{
					vector<int> argsVector = decouperArgsInt(vecteurNomArgs.at(1), ' ');

					if(argsVector.size()%2 != 0)
					{
						erreur = true;
						message = "Veuillez entrer un nom puis les coordonnées d'une suite de points";
					}
					else
					{					
						//Changer le vecteur de int en vecteur de points
						vector<Point> Vpoints;
						for(unsigned int u=0 ; u<argsVector.size(); u+=2)
						{	
							Point pt(argsVector.at(u),argsVector.at(u+1));
							Vpoints.insert(Vpoints.end(),pt);
						}

						//On vérifie que le polygone est bien convexe
						PolygoneConvexe pc (vecteurNomArgs.at(0), Vpoints);
						if(pc.estConvexe(Vpoints))
						{
							//Appel du constructeur de PolygoneConvexe
							modele.insertion(vecteurNomArgs.at(0), nomCommande, Vpoints);
							message = "Polygone Convexe " + vecteurNomArgs.at(0) + " créé" ;
						}
						else
						{
							erreur = true;
							message = "Polygone non convexe";
						}
						
					}
				}
			}
			else
			{
				erreur = true;
				message = "Nom déjà utilisé";
			}
		}

	}

	else if (nomCommande == "OR")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un nom puis plusieurs noms de figures";
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			//Verifie si une figure porte deja ce nom ou pas
			if (modele.nomDispo(vecteurNomArgs.at(0)))
			{
				if (vecteurNomArgs.at(1).length() < 1)
				{
					erreur = true;
					message = "Veuillez entrer au moins deux noms de figures";
				}
				
				else
				{
					vector<string> argsVector = decouperArgsString(vecteurNomArgs.at(1), ' ');

					//Vérifier d'abord que toutes les figures existent
					bool nomsExistent = true;
					for(unsigned int i = 0; i < argsVector.size(); i++)
					{
						if (modele.nomDispo(argsVector.at(i)))
						{
							nomsExistent = false;
							break;
						}
					}

					if(!nomsExistent)
					{
						erreur = true;
						message = "Une des figures n'existe pas";					}
					else
					{
						message = "Opération de réunion";
						modele.insertion(vecteurNomArgs.at(0), nomCommande, argsVector);
					}
					
				}
			}
			else
			{
				erreur = true;
				message = "Nom de figure déjà existant";
			}
		}
	}

	else if (nomCommande == "OI")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			//Verifie qu'une figure porte deja ce nom
			if (modele.nomDispo(vecteurNomArgs.at(0)))
			{
				if (vecteurNomArgs.at(1).length() < 1)
				{
					erreur = true;
				}
				
				else
				{
					vector<string> argsVector = decouperArgsString(vecteurNomArgs.at(1), ' ');

					//Vérifier d'abord que toutes les figures existent
					bool nomsExistent = true;
					for(unsigned int i = 0; i < argsVector.size(); i++)
					{
						if (modele.nomDispo(argsVector.at(i)))
						{
							nomsExistent = false;
							break;
						}
					}

					if(!nomsExistent)
					{
						erreur = true;
					}
					else
					{
						message = "Opération de réunion";
						modele.insertion(vecteurNomArgs.at(0), nomCommande, argsVector);
					}
					
				}
			}
			else
			{
				erreur = true;
			}
		}
		if (erreur)
		{
			message = "Veuillez entrer au moins deux noms de figures existantes";
		}
	}

	else if (nomCommande == "HIT")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un nom de figure puis les coordonnées d'un point";
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			if (vecteurNomArgs.at(1).length() < 1)
			{
				message = "Veuillez entrer un nom de figure et les coordonnées d'un point";
				erreur = true;
			}
			else if (modele.nomDispo(vecteurNomArgs.at(0)))
			{
				message = "Figure inconnue";
				erreur = true;
			}
			else
			{
				vector<int> argsVector = decouperArgsInt(vecteurNomArgs.at(1), ' ');


				bool compris = false;
				Point pt (argsVector.at(0), argsVector.at(1));
				compris = modele.contient(vecteurNomArgs.at(0), pt);

				if (compris)
				{
					cout << "YES" << endl;
					message = "Le point est compris dans la figure " + vecteurNomArgs.at(0);
				}
				else 
				{
					cout << "NO" << endl;
					message = "Le point n'est pas compris dans la figure " + vecteurNomArgs.at(0);
				}
			}
		}

	}

	else if (nomCommande == "DELETE")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez rentrer au moins un nom de figure à supprimer";
		}
		else
		{
			vector<string> argsVector = decouperArgsString(arguments, ' ');
			if(arguments.length() < 1)
			{
				erreur = true;
			}
			else
			{
				//Vérifier d'abord que toutes les figures existent
				bool nomsExistent = true;
				for(unsigned int i = 0; i < argsVector.size(); i++)
				{
					if (modele.nomDispo(argsVector.at(i)))
					{
						nomsExistent = false;
						break;
					}
				}

				//Suppression des figures si toutes les figurent existent
				if (nomsExistent)
				{
					for (unsigned int i = 0; i < argsVector.size(); i++)
					{
						modele.suppretion(argsVector.at(i));
					}
					message = "Figure(s) supprimée(s)" ;
				}
				else
				{
					message = "Au moins une figure est inexistante";
					erreur = true;
				}
				
			}
		}

		if (erreur)
		{
			message = "Veuillez entrer les noms des figures à supprimer";
		}
	}

	else if (nomCommande == "MOVE")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
		}
		else
		{
			vector<string> vecteurNomArgs = separerNomCommande(arguments);

			if (vecteurNomArgs.at(1).length() < 1)
			{
				erreur = true;
			}
			else
			{				
				vector<int> argsVector = decouperArgsInt(vecteurNomArgs.at(1), ' ');

				if(argsVector.size() != 2)
				{
					erreur = true;
				}
				else
				{
					if (modele.nomDispo(vecteurNomArgs.at(0)))
					{
						message = "Figure inconnue";
						erreur = true;
					}
					else
					{
						//Appel de la méthode de deplacement de la figure
						Point pt (argsVector.at(0), argsVector.at(1));
						modele.deplacer(vecteurNomArgs.at(0), pt);
						message = "La figure " + vecteurNomArgs.at(0) + " a été déplacée" ;
					}
				}
			}
		}

		if (erreur)
		{
			message = "Veuillez entrer un nom de figure puis les coordonnées d'un seul point";
		}
	}

	else if (nomCommande == "LIST")
	{
		//Lister toutes les figures grace au vecteur compris dans Modele
		modele.afficher();
		message = "Fin des figures";
	}

	else if (nomCommande == "LOAD")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un argument avec votre commande";
		}
		else
		{
			string nom = "";
			nom = arguments.substr(arguments.find(" ")+1);
			nom = nom.substr(0, nom.find(" "));

			//Verification de l'extention du fichier
			size_t pos = nom.find(".");
			string exten = "";
			
			if (pos != string::npos)
			{
				exten = nom.substr(pos);
			}

			//On regarde si le nom de fichier finit bien par .txt
			if(exten == ".txt")
			{
				//Chargement du fichier "nom"
				modele.Load(nom);
				message = "Nouveau modèle chargé";
			}
			else
			{
				erreur = true;
				message = "Nom de fichier invalide (doit finir en .txt)";
			}

		}
	}

	else if (nomCommande == "SAVE")
	{
		if (arguments.length() < 1)
		{
			erreur = true;
			message = "Veuillez entrer un argument avec votre commande";
		}
		else
		{
			string nom = "";
			nom = arguments.substr(arguments.find(" ")+1);
			nom = nom.substr(0, nom.find(" "));

			//Verification de l'extention du fichier
			size_t pos = nom.find(".");
			string exten = "";
			
			if (pos != string::npos)
			{
				exten = nom.substr(pos);
			}

			//On regarde si le nom de fichier finit bien par .txt
			if(exten == ".txt")
			{
				//Sauvegarde du modèle courant
				modele.Save(nom);
				message = "Le modèle courant a été sauvegardé";
			}
			else
			{
				erreur = true;
				message = "Nom de fichier invalide (doit finir en .txt)";
			}
		}
	}

	else if (nomCommande == "CLEAR")
	{
		modele.Clear();
		message = "Le modèle courant a été effacé";
	}

	else if (nomCommande == "UNDO")
	{
		
		message = "La dernière action a été annulée";
	}

	else if (nomCommande == "REDO")
	{
		message = "La dernière annulation a été annulée";
	}

	
	else if (nomCommande == "EXIT")
	{
		message = "Fermeture de l'application...";
	}

	else
	{
		erreur = true;
		message = "Commande non valide.";
	}


	if(erreur)
	{
		cout << "ERR" << endl;
	}
	else if (nomCommande == "EXIT" || nomCommande == "HIT" || nomCommande == "LIST")
	{
		//Ne rien afficher ici
	}
	else
	{
		cout << "OK" << endl;
	}

	cout << "#" << message << endl;
	erreur = false;

}  //----- Fin de executerCommande



vector<int> &Commande::decouperArgsInt(const string &s, char delim, vector<int> &elems) 
{
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) 
    {
        elems.push_back(stoi(item));
    }
    return elems;
} //----- Fin de &decouperArgsInt

vector<int> Commande::decouperArgsInt(const string ligne, char delim)
{
	vector<int> elems;
    decouperArgsInt(ligne, delim, elems);
    return elems;
} //----- Fin de decouperArgsInt


vector<string> &Commande::decouperArgsString(const string &s, char delim, vector<string> &elems) 
{
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) 
    {
        elems.push_back(item);
    }
    return elems;
} //----- Fin de &decouperArgsString

vector<string> Commande::decouperArgsString(const string ligne, char delim)
{
	vector<string> elems;
    decouperArgsString(ligne, delim, elems);
    return elems;
} //----- Fin de decouperArgsString

/*
void Commande::ecrireSauvegarde(string nomFichier)
{
	ofstream fichier;
	fichier.open (nomFichier);


	for (vector<Commande>::iterator it = histoCommandes.begin() ; it != histoCommandes.end(); ++it)
	{
		fichier << it->nomCommande << it->arguments;
		fichier << endl;
		cout << it->nomCommande << endl;
		cout << it->arguments << endl;
	}
	
	fichier.close();
}
*/

vector<string> Commande::separerNomCommande(string args)
{
	vector<string> v;

	size_t pos = args.find(" ");
	string nom = "";
	string temp = "";

	if (pos != string::npos)
	{
		nom = args.substr(0, pos);
		temp = args.substr(pos);
		temp = temp.substr(temp.find(" ")+1);
	}
	
	else
	{
		nom = args;
		temp = "";
	}

	v.push_back(nom);
	v.push_back(temp);

	return v;
}



