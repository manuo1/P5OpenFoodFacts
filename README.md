DESCRIPTION
============
Ce programme interagit avec la base Open Food Facts pour en récupérer les aliments, les
comparer et proposer à l'utilisateur un substitut plus sain à un aliment qu’il a choisi.

INSTALATION
============
Le programme a été développé en langage python dans un environnement virtuel.

	1 - Il est nécessaire pour le faire fonctionner d’installer
	-------------------------------------------------------------
		1 - Python
		2 - pip
		3 - MySQL

	2 - Vous devez ensuite modifier le fichier :
	--------------------------------------------
	` main\ressources\user_connection.yaml `
	Et remplacer :
	`'votre mot de passe ici'`
	Par votre mot de passe de connexion à MySQL (Les ' ' sont importants)

	3 - Puis dans un terminal placer vous dans le fichier « main » et lancez l’installation avec :
	----------------------------------------------------------------------------------------------
		`pip install -r requirements.txt`

	4 – Enfin lancez le programme avec :
	------------------------------------
		`python main.py`

	5 - *IMPORTANT* :
	-----------------
    	A la première instalation il serra indispensable d'installer la base de données en
    	choisissant le scenario 3 du menu princial

FONCTIONNEMENT
===============
Le menu principal du programme vous propose 4 options :
-------------------------------------------------------
	1 - Remplacer un aliment
	2 - Retrouver mes aliments substitués
	3 - Réinstaller la base de données
	4 - Quitter le programme

Choisissez en saisissant le numéro du scenario voulut puis appuyez sur Entrée pour valider.

Etapes du scénario 1 (Remplacer un aliment)
-------------------------------------------
	1 - Dans quelle catégorie voulez-vous substituer l'aliment ?
		Le programme vous propose 5 catégories d’aliments.
	2 - Quel aliment voulez-vous substituer ?
		Le programme vous propose 20 aliments choisis au hasard dans la catégorie choisie 
		précédemment, vous choisissez en saisissant le numéro de l'aliment voulut puis 
		appuyez sur Entrée pour valider.
	4 - Quel aliment voulez-vous afficher ?
		S’ils existent le programme vous propose un maximum de 3 aliments avec un meilleur 
		Nutri-Score, vous choisissez en saisissant le numéro de l'aliment voulut puis appuyez
		sur Entrée pour valider.
	5 - Voulez-vous sauvegarder ce résultat ? (O/N)
		Pour chaque aliment enregistrer, le programme affiche le nom, le Nutri-Score, une liste des
		magasins ou acheter le aliment et le lien vers la page de l'aliment sur le site 
		d’Open Food Facts, puis il vous propose de sauvegarder un de ces aliment, vous choisissez 
		en saisissant O pour Oui ou N pour Non puis appuyez sur Entrée pour valider, le programme 
		retourne au menu principal.

Etapes du scénario 2 (Retrouver mes aliments substitués)
--------------------------------------------------------
	Le Programme affiche chaque aliment remplacé avec son ou ses aliments de substitution et les 
	détails des aliments de substitution, le programme retourne au menu principal.

Etapes du Scénario 3 (Réinstaller la base de données)
-----------------------------------------------------
	Le programme va récupérer des aliments pour chaque catégorie dans l’API d’Open Food Facts et
	« nettoyer » les résultats récoltés, ensuite il vide la base de données locale en supprimant et
	recréant les tables puis il y insert les nouvelles données récoltées et retourne au menu
	principal.

Etapes du Scénario 4 (Quitter le programme)
-------------------------------------------
	Vous sortez du programme
