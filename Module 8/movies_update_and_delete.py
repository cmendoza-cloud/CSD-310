import mysql.connector

def connect_to_database():
    """Connects to the MySQL movies database."""
    return mysql.connector.connect(
        host="127.0.0.1",
        user="movie_user",
        password="popcorn",
        database="movies"
    )
def show_films(cursor, title):
    """Displays films with specified columns and a title."""
    query = """
        SELECT 
            film_name AS Name, 
            genre_name AS Genre, 
            studio_name AS Studio, 
            film_director AS Director
        FROM 
            film
        INNER JOIN 
            genre ON film.genre_id = genre.genre_id
        INNER JOIN 
            studio ON film.studio_id = studio.studio_id;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"\n{title}")
    print("-" * 50)
    for row in results:
        print(f"Name: {row[0]}, Genre: {row[1]}, Studio: {row[2]}, Director: {row[3]}")

