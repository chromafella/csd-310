import mysql.connector
from mysql.connector import errorcode


def show_films(cursor, title):
    # Modified query to match expected output exactly
    cursor.execute("""
        SELECT 
            film_name, 
            film_director, 
            genre_name, 
            studio_name
        FROM 
            film 
            INNER JOIN genre ON film.genre_id = genre.genre_id 
            INNER JOIN studio ON film.studio_id = studio.studio_id
        ORDER BY film_name
    """)

    films = cursor.fetchall()

    print("\n— {} —".format(title))

    for film in films:
        print("Film Name: {}".format(film[0]))
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))
        print("Studio Name: {}".format(film[3]))
        print()


try:
    config = {
        "user": "movies_user",
        "password": "popcorn",
        "host": "127.0.0.1",
        "database": "movies",
        "raise_on_warnings": True
    }

    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Display initial films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert Star Wars (as shown in expected output)
    cursor.execute("""
        INSERT INTO film 
        (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
        VALUES 
        ('Star Wars', 'George Lucas', 
        (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'), 
        (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),
        '1977', 121)
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to Horror
    cursor.execute("""
        UPDATE film 
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') 
        WHERE film_name = 'Alien'
    """)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")