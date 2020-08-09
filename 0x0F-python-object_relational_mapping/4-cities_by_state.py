#!/usr/bin/python3
"""
list all cities
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dataBase = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    cursor = dataBase.cursor()

    cursor.execute("SELECT cities.id,\
                    cities.name,\
                    states.name FROM\
                    cities LEFT JOIN\
                    states ON states.id = cities.state_id\
                    ORDER\
                    BY cities.id")

    rows = cursor.fetchall()

    for element in rows:
        print(rows)

    cursor.close()
    dataBase.close()
