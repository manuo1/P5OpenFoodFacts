import os
import yaml

# create the path to the game's main directory for user's operating system
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
# sets files paths
CONNECTION_FILE = os.path.join(FILE_PATH, "connection.yaml")

with open(CONNECTION_FILE) as file:
    CONNECTION_DATA = yaml.load(file, Loader=yaml.FullLoader)
