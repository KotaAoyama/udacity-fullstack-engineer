#!/usr/bin/env python3
import psycopg2
DBNAME = "news"


def logOne():
    '''This function shows the most popular three articles of all time.'''
    try:
        db = psycopg2.connect(dbname=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
    else:
        c = db.cursor()
        c.execute('''
            select articles.title, count(log.path)
            from log
            join articles on log.path = '/article/' || articles.slug
            group by articles.title
            order by count(log.path) desc
            limit 3;
        ''')
        print("1. What are the most popular three articles of all time?")
        rows = c.fetchall()
        for row in rows:
            print(row[0]+" --- "+str(row[1])+" views")
        db.close()


def logTwo():
    '''This function shows the most popular arthors of all time.'''
    try:
        db = psycopg2.connect(dbname=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
    else:
        c = db.cursor()
        c.execute('''
            select authors.name, count(authors.name)
            from log
            join articles on log.path = '/article/' || articles.slug
            join authors on articles.author = authors.id
            group by authors.name
            order by count(authors.name) desc
        ''')
        print("2. Who are the most popular article authors of all time?")
        rows = c.fetchall()
        for row in rows:
            print(row[0] + " --- " + str(row[1]) + " views")
        db.close()


def logThree():
    '''This function shows the day
    on which more than 1% of requests lead to errors.'''
    try:
        db = psycopg2.connect(dbname=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
    else:
        c = db.cursor()
        c.execute('''
            select error_log.date, cast(error_count as float)/all_count*100
            from error_log, all_log
            where error_log.date = all_log.date
            and cast(error_count as float) / all_count >= 0.01;
        ''')
        print("3. On which days did more than 1% of requests lead to errors?")
        rows = c.fetchall()
        for row in rows:
            print(str(row[0]) + " --- " +
                  str(round(row[1], 1)) + "% errors")
        db.close()


if __name__ == '__main__':
    logOne()
    logTwo()
    logThree()
