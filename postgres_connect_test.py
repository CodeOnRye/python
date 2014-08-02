#!/usr/bin/python
#
# Small script to show PostgreSQL and Pyscopg together
#
import psycopg2

dbname = "tevatrondb"
user = "postgres"
host = "localhost"
password = "postgres"

try:
    conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (dbname, user, host, password))
except:
    print ("I am unable to connect to the database")

print ("Connection Sucessful")
