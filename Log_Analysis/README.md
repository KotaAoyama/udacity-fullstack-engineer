# Logs Analysis Project
This project is analysising logs for a fictional news website by using a command line tool.

## Table Contents
Three tables: articles, authors, log

Table "articles"
 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


 Table "authors"
 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


Table "log"
 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)


## Quetions

### 1. What are the most popular three articles of all time?
### 2. Who are the most popular article authors of all time?
### 3. On which days did more than 1% of requests lead to errors?


## Instructions

1. In this project, you use vagrant and virtial box. If you need, install [Vagrant](https://www.vagrantup.com/) and [VirtualBox 5.1.38](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
2. Download the ``https://github.com/KotaAoyama/udacity-fullstack-engineer/tree/master/Log_Analysis/vagrant`` folder.
3. Set up and log in the VM.
4. Move ``/vagrant``.
5. Unzip ``newsdata.zip`` and use ``psql -d news -f newsdata.sql`` command in terminal so that you insert fictional newsdata into postgreSQL.
6. Use ``psql -d news -f create_views.sql`` command so that you prepare log analysis by creating views. 
7. Finally, move ``forum/`` and try the log analysis command line tool by using ``python3 log_analysis.py`` command. 
 
