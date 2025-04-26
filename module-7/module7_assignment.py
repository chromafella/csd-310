# Module 7.2 Assignment
# By Brennan Cheatwood
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

# using our .env file
secrets = dotenv_values(".env")

"""Database config object"""
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)  # connect to movies db

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    """ Query 1: Select all fields from studio """
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()

    """ Query 2: Select all fields from genre """
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()

    """ Query 3: Select movie names with run time less than 2 hours """
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
        print()

    """ Query 4: List film names and directors grouped by director """
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("SELECT film_director, film_name FROM film ORDER BY film_director")
    directors = cursor.fetchall()
    for director in directors:
        print(f"Film Name: {director[1]}")
        print(f"Director: {director[0]}")
        print()

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" Database does not exist")
    else:
        print(err)

finally:
    db.close()
