#!/usr/bin/python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='tevatrondb' user='postgres' host='localhost' password='postgres'")
except:
    print ("I am unable to connect to the database")

print ("Connection Sucessful")
