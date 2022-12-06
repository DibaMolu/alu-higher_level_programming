#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
        from sys import argv
            import MySQLdb
                db = MySQLdb.connect(user=argv[1],
                                                 passwd=argv[2],
                                                                          db=argv[3])
                    cr = db.cursor()
                        cr.execute("SELECT * from states\
                                                WHERE name LIKE 'N%'\
                                                                ORDER BY states.id")
                            states = cr.fetchall()
                                for state in states:
                                            if state[1][0] == 'N':
                                                            print(state)
                                                                cr.close()
                                                                    db.close()
