#!/usr/bin/python3
"""
module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
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
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))

    # fetch all the rows
    rows = cursor.fetchall()

    # printing the result
    for row in rows:
        print(row)

    # database connection closing
    cursor.close()
    db_server.close()
