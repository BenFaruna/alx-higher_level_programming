#!/usr/bin/python3
"""list db entry for a specific state"""
import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:-1])
    cur = conn.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
