""" import statements """
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

# using our.env file
secrets = dotenv_values(".env")

"""Database config object"""
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True  # not in .env file

}

try:
    db = mysql.connector.connect(**config) # connect to movies db

    print("\n Database user {} Connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

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