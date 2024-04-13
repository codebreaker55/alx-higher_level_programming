#!/usr/bin/python3
import sys
import MySQLdb
"""module that lists all states from the database hbtn_0e_0_usa"""


def states_list(username, password, database):
    """a function that is used to connect to the MySQL server"""
    db_server = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cursor = db_server.cursor()

    # using execute to fetch all the states
    cursor.execute("SELECT * FROM states ORDER by id ASC")

    # fetch all the rows
    rows = cursor.fetchall()

    # printing the result
    for row in rows:
        print(row)

    # database connection closing
    db_server.close()


# the example ussage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    states_list(username, password, database)
