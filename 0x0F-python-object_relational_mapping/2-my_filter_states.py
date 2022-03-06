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
    cursor.execute("SELECT * FROM states WHERE(name='{}' AND id < 3) \
                   ORDER BY id".format(searched))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_conn.close()
