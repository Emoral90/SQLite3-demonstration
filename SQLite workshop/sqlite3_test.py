import sqlite3

connection = sqlite3.connect('chinook.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS albums (AlbumId REAL, Title TEXT, ArtistId REAl)")
cursor.execute("CREATE TABLE IF NOT EXISTS artists (ArtistId REAl, Name TEXT)")

def get_album_list(cursor):
    cursor.execute("SELECT Title FROM albums")
    records = cursor.fetchall()
    if len(records) == 0:
        print("No titles in database")
        return None
    for i in range(len(records)):
        print(f"{i+1} - {records[i][0]}")
    

def get_name_list(cursor):
    cursor.execute("SELECT Name FROM artists")
    records = cursor.fetchall()
    if len(records) == 0:
        print("No names in database")
        return None
    for i in range(len(records)):
        print(f"{i+1} - {records[i][0]}")

def get_name(cursor):
    cursor.execute("SELECT Name FROM artists")
    records = cursor.fetchall()
    if len(records) == 0:
        print("No names in database")
        return None
    for i in range(len(records)):
        print(f"{i+1} - {records[i][0]}")
    choice = 0
    while choice < 1 or choice > len(records):
        choice = int(input("Artist ID: "))
    return records[choice-1][0]

def get_title(cursor):
    cursor.execute("SELECT Title FROM albums")
    records = cursor.fetchall()
    if len(records) == 0:
        print("No titles in database")
        return None
    for i in range(len(records)):
        print(f"{i+1} - {records[i][0]}")
    choice = 0
    while choice < 1 or choice > len(records):
        choice = int(input("Album ID: "))
    return records[choice-1][0]

choice = None
while choice != "10":
    print()
    print("1) Display Albums")
    print("2) Display Artists")
    print("3) Add Album")
    print("4) Add Artists")
    print("5) Update Album")
    print("6) Delete Artist")
    print("7) Delete Album")
    print("8) Search for Album by Artist")      ## Search by INTERSECT or UNION keyword
    # print("9) Search for Artist by Album")
    print("10) Quit")
    choice = input("> ")
    print()

    if choice == "1":
        # Display Albums
        cursor.execute("SELECT * FROM albums ORDER BY AlbumId ASC")
        print("{:>10}  {:>50}  {:>10}".format("Album ID", "Title", "Artist ID"))
        print("=======================================================================================\n")
        for line in cursor.fetchall():
            print("{:>10}  {:>50}  {:>10}".format(line[0], line[1], line[2]))
            print("---------------------------------------------------------------------------------------")
        print("{:>10}  {:>50}  {:>10}".format("Album ID", "Title", "Artist ID"))
        print("=======================================================================================\n")
    
    elif choice == "2": 
        # Display Artists
        cursor.execute("SELECT * FROM artists ORDER BY ArtistId ASC")
        print("{:>10}  {:>50}".format("Artist ID", "Name"))
        print("=======================================================================================\n")
        for line in cursor.fetchall():
            print("{:>10}  {:>50}".format(line[0], line[1]))
            print("---------------------------------------------------------------------------------------")
        print("{:>10}  {:>50}".format("Artist ID", "Name"))
        print("=======================================================================================\n")

    elif choice == "3":
        # Add New Album info
        try:
            get_album_list(cursor)
            print("Album ID - Album Title\n")
            get_name_list(cursor)
            print("Artist ID - Artist Name\n")

            album_id = int(input("Album ID: "))
            title = input("Title: ")
            artist_id = int(input("Artist ID: "))
            values = (album_id, title, artist_id)
            cursor.execute("INSERT INTO albums VALUES (?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid Album ID!")

    elif choice == "4":
        # Add New Artist info
        try:
            get_name_list(cursor)
            print("Artist ID - Artist Name\n")
            artist_id = int(input("Artist ID: "))
            name = input("Name: ")
            values = (artist_id, name)
            cursor.execute("INSERT INTO artists VALUES (?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid Artist ID!")

    elif choice == "5":
        # Update Album title
        try:
            get_album_list(cursor)
            print("Album ID - Album Title\n")
            album_id = int(input("Album ID: "))
            title = input("Title: ")
            values = (title, album_id)
            cursor.execute("UPDATE albums SET Title = ? WHERE AlbumId = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid Title!")
        except ValueError:
            print("Invalid Album ID!")

    elif choice == "6":
        # Delete Artist
        name = get_name(cursor)
        print("Artist ID - Artist Name\n")
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM artists WHERE Name = ?", values)
        connection.commit()
        print()

    elif choice == "7":
        # Delete Album
        title = get_title(cursor)
        print("Artist ID - Artist Name\n")
        if title == None:
            continue
        values = (title, )
        cursor.execute("DELETE FROM albums WHERE Title = ?", values)
        connection.commit()
        print()

    elif choice == "8":
        # Search for Album by Artist
        search_album_choice = None
        while search_album_choice != "3":
            print("1) Search by Artist ID")
            # print("2) Search by Artist name")
            print("3) Return to Main Menu")
            search_album_choice = input("> ")
            print()
            if search_album_choice == "1":
                try:
                    # artist_id = int(input("Artist ID: "))
                    # values = (artist_id, )
                    cursor.execute("SELECT Title, ArtistId FROM albums INTERSECT SELECT ArtistId, Name FROM artists") # WHERE ArtistId = ? ", values)
                    connection.commit()
                except ValueError:
                    print("Invalid Artist ID!")
        continue

    # elif choice == "9":
    #     # Search for Artist by Album
    #     pass
connection.close()