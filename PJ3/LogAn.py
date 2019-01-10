#!/usr/bin/env python
import psycopg2
import time


# con=psycopg2.connect (database="news")

try:
    # connecting the data base using postgresql
    con = psycopg2.connect(database="newsdb")
    print("Heepe Connected..!")
    curr = con.cursor()
except Exception as ex:
    print("Ooh error :(", ex)


def articles_view():
    curr.execute("select title,views from articles_view limit 3;")
    art = curr.fetchall()
    print("The most popular three articles::")
    for a_v in art:
        print a_v[0], "--", a_v[1]


def authors_view():
    curr.execute("select name,total from authors_view limit 3;")
    art = curr.fetchall()
    print("The most popular article authors::")
    for a_v in art:
        print a_v[0], "--", a_v[1]


def log_view():
    curr.execute("select * from log_view where percentage_errors > 1 ;")
    find = curr.fetchall()
    print("On which day did more than 1%  of errors found::")
    for i in find:
        print i[0], "--", '%0.1f%%' % (i[1])

articles_view()
authors_view()
log_view()
curr.close()
con.close()
