#!/usr/bin/python3

"""
script that lists all states with a given name
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3])
    searched = argv[4]
    cursor = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_conn.close()
