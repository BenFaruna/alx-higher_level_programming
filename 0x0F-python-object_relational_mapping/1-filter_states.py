#!/usr/bin/env python3
"""List data with a pattern"""

import sys
import MySQLdb as mysql_

if __name__ == "__main__":
    conn = mysql_.connect("localhost", *sys.argv[1:])

    conn.query(
            "SELECT * FROM states WHERE name LIKE 'N_%' ORDER BY states.id;"
    )
    result = conn.store_result()
    states = result.fetch_row(maxrows=0)

    for state in states:
        print(state)
