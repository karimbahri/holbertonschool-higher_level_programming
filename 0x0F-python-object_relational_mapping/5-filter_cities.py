#!/usr/bin/python3
"""
lists all citie of that state
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

    argument = argv[4]

    cursor.execute("SELECT cities.name\
                    FROM cities JOIN\
                    states\
                    ON cities.state_id = states.id\
                    WHERE states.name = %s", (argument, ))

    rows = cursor.fetchall()

    i = 0
    length = len(rows)
    for element in rows:
        if i:
            print(", ", end="")
        i += 1
        print(element[0], end="")
    print("")
    cursor.close()
    dataBase.close()
