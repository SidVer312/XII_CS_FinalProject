import csv
import random

artworks = []


with open('artworks.csv', 'a') as csvfile:
    print("Main File Intialized")

with open('artworks.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artwork = {
            'Title': row['Title'],
            'Artist': row['Artist'],
            'Year': int(row['Year']),
            'Medium': row['Medium'],
            'Price': float(row['Price']),
            'Status': 'Available'  
        }
        artworks.append(artwork)

artists = []

with open('artists.csv', 'a') as csvfile:
    print("Artists file intialized")

with open('artists.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artist = {
            'Name': row['Name'],
            'Nationality': row['Nationality'],
            'Style': row['Style']
        }
        artists.append(artist)

def admin_login():
    admin_password = input("Enter admin password: ")

    if admin_password == "SidShaurya":  
        return True
    else:
        print("Invalid password. Access denied.")
        return False

def display_artworks():
    for artwork in artworks:
        print("Title:", artwork['Title'])
        print("Artist:", artwork['Artist'])
        print("Year:", artwork['Year'])
        print("Medium:", artwork['Medium'])
        print("Price:", artwork['Price'])
        print("Status:", artwork['Status'])
        print("\n")

def display_artworks_by_artist(artist_name):
    filtered_artworks = []
    for artwork in artworks:
        if artwork['Artist'] == artist_name:
            filtered_artworks.append(artwork)

    if filtered_artworks:
        display_artworks(filtered_artworks)
    else:
        print("No artworks found for artist:", artist_name)

def search_artworks():
    search_term = input("Enter search term (title or artist): ")

    filtered_artworks = []
    for artwork in artworks:
        if search_term.lower() in artwork['Title'].lower() or search_term.lower() in artwork['Artist'].lower():
            filtered_artworks.append(artwork)

    if filtered_artworks:
        display_artworks(filtered_artworks)
    else:
        print("No artworks found matching search term:", search_term)

def add_artwork():
    if admin_login():
        title = input("Title: ")
        artist = input("Artist: ")
        year = int(input("Year: "))
        medium = input("Medium: ")
        price = float(input("Price: "))

        new_artwork = {
            'Title': title,
            'Artist': artist,
            'Year': year,
            'Medium': medium,
            'Price': price,
            'Status': 'Available'
        }
        artworks.append(new_artwork)

        print("Artwork added successfully.")
    else:
        print("Admin authentication failed.")

def sell_artwork():
    if admin_login():
        artwork_title = input("Enter title of the artwork to sell: ")

        found_artwork = None
        for artwork in artworks:
            if artwork['Title'] == artwork_title:
                found_artwork = artwork
                break

        if found_artwork:
            if found_artwork['Status'] == 'Available':
                found_artwork['Status'] = 'Sold'
                print("Artwork", artwork_title, "sold successfully.")
            else:
                print("Artwork", artwork_title, "is already sold.")
        else:
            print("Artwork", artwork_title, "not found.")
    else:
        print("Admin authentication failed.")

def appraise_artwork(artwork_title):
    found_artwork = None
    for artwork in artworks:
        if artwork['Title'] == artwork_title:
            found_artwork = artwork
            break

    if found_artwork:
        appraisal_value = random.randint(1000000, 999999999)
        print("Appraisal value of", artwork_title, "is approximately", appraisal_value)
    else:
        print("Artwork", artwork_title, "not found.")

def save_artworks():
    if admin_login():
      with open('artworks.csv', 'w') as csvfile:
          fieldnames = ['Title', 'Artist', 'Year', 'Medium', 'Price', 'Status']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

          writer.writeheader()
          for artwork in artworks:
              writer.writerow(artwork)
    else:
        print("Admin authentication failed.")

while True:
    print("Welcome to the Art Gallery Management System")
    print("1. Display all artworks")
    print("2. Display artworks by artist")
    print("3. Search artworks")
    print("4. Add a new artwork")
    print("5. Sell an artwork")
    print("6. Appraise an artwork")
    print("7. Save artworks")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_artworks()
    elif choice == 2:
        artist_name = input("Enter artist name: ")
        display_artworks_by_artist(artist_name)
    elif choice == 3:
        search_artworks()
    elif choice == 4:
        add_artwork()
    elif choice == 5:
        sell_artwork()
    elif choice == 6:
        artwork_title = input("Enter title of the artwork to appraise: ")
        appraise_artwork(artwork_title)
    elif choice == 7:
        save_artworks()
    elif choice == 8:
        print("Thank you for using the Art Gallery Management System")
        break
    
    print("\n")
    
