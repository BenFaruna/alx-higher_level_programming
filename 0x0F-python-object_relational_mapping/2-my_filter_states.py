#!/usr/bin/env python3
"""list db entry for a specific state"""
import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:-1])
    query = """SELECT * FROM states
        WHERE states.name = '{}'
        ORDER BY states.id;
    """.format(sys.argv[-1])

    conn.query(query)
    result = conn.store_result()
    states = result.fetch_row(maxrows=0)

    for state in states:
        print(state)

    conn.close()
