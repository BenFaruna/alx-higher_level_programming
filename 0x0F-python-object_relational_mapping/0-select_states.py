#!/usr/bin/env python3
"""show all data in the database"""
import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:])

    conn.query("SELECT * FROM states ORDER BY states.id;")
    result = conn.store_result()
    states = result.fetch_row(maxrows=0)

    for state in states:
        print(state)
