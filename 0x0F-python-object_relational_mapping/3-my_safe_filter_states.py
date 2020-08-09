#!/usr/bin/python3
"""
display states safe from MySQL injections
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    dataBase = MySQLdb.connect(host="localhost",
                               port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])

    cursor = dataBase.cursor()

    argument = argv[4]

    cursor.execute("SELECT * FROM\
                   states WHERE name\
                   LIKE BINARY %s\
                   ORDER BY states.id\
                   ASC", (argument, ))

    rows = cursor.fetchall()

    for element in rows:
        print(element)

    cursor.close()
    dataBase.close()
