#!/usr/bin/env python3
"""List data with a pattern"""

import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    conn.close()
