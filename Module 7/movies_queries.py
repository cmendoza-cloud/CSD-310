# movies_queries.py

import mysql.connector

def connect_to_database():
    """Connect to the MySQL movies database."""
    return mysql.connector.connect(
        host="127.0.0.1",        
        user="movies_user",     
        password="popcorn", 
        database="movies"      
    )

def run_queries():
    """Run the specified queries and display their results."""
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Query 1: Select all fields for the studio table
        print("Query 1: All fields from the 'studio' table:")
        cursor.execute("SELECT * FROM studio;")
        for row in cursor.fetchall():
            print(row)
        print("\n")

        # Query 2: Select all fields for the genre table
        print("Query 2: All fields from the 'genre' table:")
        cursor.execute("SELECT * FROM genre;")
        for row in cursor.fetchall():
            print(row)
        print("\n")

        # Query 3: Movies with a runtime less than two hours
        print("Query 3: Movies with a runtime less than two hours:")
        cursor.execute("SELECT movie_name FROM movies WHERE runtime < 120;")
        for row in cursor.fetchall():
            print(row[0])  # Display only the movie name
        print("\n")

        # Query 4: Film names and directors grouped by director
        print("Query 4: Film names and directors grouped by director:")
        cursor.execute("""
            SELECT director_name, GROUP_CONCAT(movie_name SEPARATOR ', ') AS movies
            FROM movies
            GROUP BY director_name;
        """)
        for row in cursor.fetchall():
            print(f"Director: {row[0]}, Movies: {row[1]}")
        print("\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean up
        cursor.close()
        connection.close()

if __name__ == "__main__":
    run_queries()
