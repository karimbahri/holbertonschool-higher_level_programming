#!/usr/bin/python3
"""
print states from database
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dataBase = MySQLdb.connect(host="localhost", user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states\
                    ORDERED BY id ASC")

    rows = cursor.fetchall()

    for elemeny in rows:
        print(element)

    cursor.close()
    database.close()
