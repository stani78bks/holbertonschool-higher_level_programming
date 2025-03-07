#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Vérification de la validité des arguments
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)
    
    try:
        # Connexion à la base de données
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        
        with db.cursor() as cur:
            # Exécution de la requête
            cur.execute("SELECT * FROM states ORDER BY id")
            
            # Récupération des résultats et affichage
            rows = cur.fetchall()
            for row in rows:
                print(row)
    
    except MySQLdb.MySQLError as e:
        print(f"Error: {e}")
    finally:
        # Fermeture de la connexion à la base de données
        if db:
            db.close()
