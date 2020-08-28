the program was developed in python language in a virtual environment.

It requires to operate :
	
	pyhton, pip and mysql

In ressources folder create a YAML file named connection.yaml and insert inside :

host: 'localhost'
user: 'root'
password: 'Your Password here'

replace (Your Password here) with your mysql password 

Then at the root of the project, in a terminal launch the program with :

	pip install -r requirements.txt

and run with

	python main.py

Using :

-------------------------------------------------------------------------------------------------------------------
Que souhaitez vous faire ?
-------------------------------------------------------------------------------------------------------------------

1 - Remplacer un aliment
2 - Retrouver mes aliments substitués
3 - Réinstaller la base de donnée
4 - Quitter le programe

