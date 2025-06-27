#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name)

    # Création du curseur
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération des résultats et affichage
    for row in cursor.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
