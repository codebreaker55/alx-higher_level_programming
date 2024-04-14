#!/usr/bin/python3
"""module that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    db_server = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cursor = db_server.cursor()

    # using execute to fetch all the states
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    INNER JOIN states ON states.id=cities.state_id""")

    # fetch all the rows
    rows = cursor.fetchall()

    # printing the result
    for row in rows:
        print(row)

    # database connection closing
    cursor.close()
    db_server.close()
