import os

import yaml

FILE_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    with open(os.path.join(FILE_PATH, "dev_connection.yaml")):
        CONNECTION_FILE = os.path.join(FILE_PATH, "dev_connection.yaml")
except IOError:
    try:
        with open(os.path.join(FILE_PATH, "user_connection.yaml")):
            CONNECTION_FILE = os.path.join(FILE_PATH, "user_connection.yaml")
    except IOError:
        print('Erreur! Fichier de connection introuvable')
        quit()

with open(CONNECTION_FILE) as file:
    CONNECTION_DATA = yaml.load(file, Loader=yaml.FullLoader)
