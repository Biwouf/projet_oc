#Fichier qui permet de gérer les opérations en base de données.

import sqlite3

class DatabaseHandler():
    """
    Objet pour gérer les opérations en base de données
    """
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.cur = self.db.cursor()
        self.cur.execute('pragma foreign_keys="1"')
    
    def __del__(self):
        self.cur.close()
        self.db.close()

    
