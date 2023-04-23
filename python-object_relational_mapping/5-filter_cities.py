#!/usr/bin/python3
"""
A script that takes in names of state as argument and lists
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    lst = []
    for r in lst:
        if r[4] == check[0]:
            cities.append(r[2])
        print(','.join(cities))
        cur.close()
        db.close()