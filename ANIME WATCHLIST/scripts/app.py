import mysql.connector

# =========================
# Database Connection
# =========================
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ch@r1z@rd",
    database = "anime_database"
)

cursor = connection.cursor() 

def view_anime():

    cursor.execute("""
    SELECT anime_id,title,episodes
    FROM Anime
    """)

    rows = cursor.fetchall()

    for anime_id,title,episodes in rows:
        print(
            f"ID:{anime_id} | "
            f"Title:{title} | "
            f"Episodes:{episodes}"
        )

# =========================
# Main Program
# =========================

def add_anime():
    #ask user for the anime title u want to add
    title = input("Enter anime title: ")

    #ask fro number of episodes
    #int() converts input from string to integer
    episodes = int(input("Enter the number of episodes: "))

    #ask user for release year
    release_year = int(input("Enter release year: "))

    #ask user for genre id
    #must match an existing genre from the genre table in sql
    genre_id = int(input("Enter genre id: "))
    #sql query to insert a new anime
    #% are placeholders where actual values will be inserted

    query = """
    insert into anime (title,episodes,release_year,genre_id) values
    (%s,%s,%s,%s)"""
    
    #store all values in a tuple 
    #order must match the values placeholders above
    values = (
        title,episodes,release_year,genre_id
    )

    #execute the sql query 
    #replaces % with actual values from the tuple
    cursor.execute(query,values)

    #permanently save changes to database
    #without commit, insetion may be lost
    connection.commit()

    #success message
    print("Anime added successfully")


def view_watchlist():

    query = """
    SELECT
        u.username,
        a.title,
        w.status,
        w.rating
    FROM Watchlist w
    JOIN User u
        ON w.user_id = u.user_id
    JOIN Anime a
        ON w.anime_id = a.anime_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    for username, title, status, rating in rows:

        print(
            f"User: {username} | "
            f"Anime: {title} | "
            f"Status: {status} | "
            f"Rating: {rating}"
        )

def update_status():

    user_id = int(input("Enter User ID: "))

    anime_id = int(input("Enter Anime ID: ")) 
    print("\nAvailable Statuses")
    print("Watching")
    print("Completed")
    print("Dropped")
    print("On Hold")
    print("Plan to Watch")
    status = input(
        "Enter New Status: "
    )
    

    query = """
    UPDATE Watchlist
    SET status = %s
    WHERE user_id = %s
    AND anime_id = %s
    """

    values = (
        status,
        user_id,
        anime_id
    )

    cursor.execute(
        query,
        values
    )

    connection.commit()

    print("Status Updated Successfully!")

def update_rating():
    user_id = int(input("Enter user id:"))
    anime_id=int(input("Enter anime id:"))
    print("\nAvailable rating(1-10)")
    
    rating = input("Enter new rating: ")

    query = """
    update watchlist 
    set rating = %s
    where user_id = %s
    and anime_id = %s
    """
    values = (
        rating,
        user_id,
        anime_id,
    )

    cursor.execute(
        query,
        values
    )

    connection.commit()
    print("Ratings updated successfully")

def delete_entry():

    user_id = int(input("Enter User ID: "))
    anime_id = int(input("Enter Anime ID: "))

    query = """
    DELETE FROM Watchlist
    WHERE user_id = %s
    AND anime_id = %s
    """

    values = (
        user_id,
        anime_id
    )

    cursor.execute(query, values)

    connection.commit()

    print("Entry Deleted Successfully!")

while True:

    print("\n===== Anime Watchlist =====")

    print("1. View Anime")
    print("2. Add Anime")
    print("3. View Watchlist")
    print("4. Update Status")
    print("5. Update Rating")
    print("6. Delete Entry")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        view_anime()

    elif choice == "2":
        add_anime()

    elif choice == "3":
        view_watchlist()

    elif choice == "4":
        update_status()

    elif choice == "5":
        update_rating()

    elif choice == "6":
        delete_entry()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")