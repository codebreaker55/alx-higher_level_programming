#!/usr/bin/python3
"""module listing all states starting with N from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    db_server = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cursor = db_server.cursor()

    # using execute to fetch all the states
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")

    # fetch all the rows
    rows = cursor.fetchall()

    # printing the result
    for row in rows:
        print(row)

    # database connection closing
    cursor.close()
    db_server.close()
