# Project Title  : Art Gallery Management System
# Version        : 1.0 2023-2024
# Developed By   : Siddhartha Verma, Shaurya Saxena
# Guide          : Ms. Hema Jain
# Last Updated On: 2023-11-19


import csv
import random
import pickle

# Define lists to store artwork data
artworks = []
with open('artworks.csv', 'a') as csvfile:
  print("File ready")

with open("password.bin", 'wb') as passwordfile:
    password = "SidShaurya"
    pickle.dump(password, passwordfile)    

with open('artworks.csv', 'r+') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artwork = {
            'ArtID': int(row['ArtID']),
            'Title': row['Title'],
            'Artist': row['Artist'],
            'Year': int(row['Year']),
            'Medium': row['Medium'],
            'Price': float(row['Price']),
            'Status': 'Available'  #A 'Status' field to track whether an artwork is available or sold
        }
        artworks.append(artwork)

artists = []

with open('artists.csv', 'a') as csvfile:
  print("artists file ready")

with open('artists.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        artist = {
            'Name': row['Name'],
            'Nationality': row['Nationality'],
            'Style': row['Style']
        }
        artists.append(artist)

sold_artworks = []

with open('sold_artworks.csv', 'a') as csvfile:
    print("sold artworks file ready")

with open('sold_artworks.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sold_artwork = {
            'ArtID': int(row['ArtID']),
            'Title': row['Title'],
            'Artist': row['Artist'],
            'Year': int(row['Year']),
            'Medium': row['Medium'],
            'Price': float(row['Price']),
            'Status': 'Sold'
        }
        sold_artworks.append(sold_artwork)

def admin_login():
    admin_password = input("Enter admin password: ")

    with open("password.bin", 'rb') as passwordfile:
        correct_password = pickle.load(passwordfile)

    if admin_password == correct_password:  # password protection
        return True
    else:
        print("Invalid password. Access denied.")
        return False

def display_artworks():
    for artwork in artworks:
        print("ArtID:", artwork['ArtID'])
        print("Title:", artwork['Title'])
        print("Artist:", artwork['Artist'])
        print("Year:", artwork['Year'])
        print("Medium:", artwork['Medium'])
        print("Price:", artwork['Price'])
        print("Status:", artwork['Status'])
        print("\n")

# Display artworks by artist
def display_artworks_by_artist(artist_name):
    filtered_artworks = []
    for artwork in artworks:
        if artwork['Artist'] == artist_name:
            filtered_artworks.append(artwork)

    if filtered_artworks:
        for artwork in filtered_artworks:
          print("ArtID:", artwork['ArtID'])
          print("Title:", artwork['Title'])
          print("Artist:", artwork['Artist'])
          print("Year:", artwork['Year'])
          print("Medium:", artwork['Medium'])
          print("Price:", artwork['Price'])
          print("Status:", artwork['Status'])
          print("\n")
    else:
        print("No artworks found for artist:", artist_name)

# Search artworks by title or artist
def search_artworks():
    search_term = input("Enter search term (title or artist): ")

    filtered_artworks = []
    for artwork in artworks:
        if search_term.lower() in artwork['Title'].lower() or search_term.lower() in artwork['Artist'].lower():
            filtered_artworks.append(artwork)

    if filtered_artworks:
        for artwork in filtered_artworks:
          print("ArtID:", artwork['ArtID'])
          print("Title:", artwork['Title'])
          print("Artist:", artwork['Artist'])
          print("Year:", artwork['Year'])
          print("Medium:", artwork['Medium'])
          print("Price:", artwork['Price'])
          print("Status:", artwork['Status'])
          print("\n")
    else:
        print("No artworks found matching search term:", search_term)

# Add a new artwork
def add_artwork():
    if admin_login():
        title = input("Title: ")
        artist = input("Artist: ")
        year = int(input("Year: "))
        medium = input("Medium: ")
        price = float(input("Price: "))

        new_artwork = {
            'ArtID': len(artworks) + 1,
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

# Sell an artwork
def sell_artwork():
    if admin_login():
        artworkID = int(input("Enter ID of artwork to sell: "))

        found_artwork = None
        for artwork in artworks:
            if int(artwork['ArtID']) == artworkID:
                found_artwork = artwork
                break

        if found_artwork:
            if found_artwork['Status'] == 'Available':
                found_artwork['Status'] = 'Sold'
                sold_artworks.append(found_artwork)
                artworks.remove(found_artwork)
                for artwork in artworks:
                    if artwork['ArtID'] > found_artwork['ArtID']:
                        artwork['ArtID'] -= 1
                
                print("Artwork", found_artwork["Title"], "sold successfully.")
        else:
            print("Artwork", found_artwork["Title"], "not found.")
    else:
        print("Admin authentication failed.")

#Remove an artwork
def remove_artwork(artworkID):
    found_artwork = None
    for artwork in artworks:
        if int(artwork['ArtID']) == artworkID:
            found_artwork = artwork
            break

    if found_artwork:
        artworks.remove(found_artwork)
        for artwork in artworks:
            if artwork['ArtID'] > found_artwork['ArtID']:
                artwork['ArtID'] -= 1
    else:
        print("Artwork not found.")

# Appraise an artwork
def appraise_artwork(artworkID):
    found_artwork = None
    for artwork in artworks:
        if int(artwork['ArtID']) == artworkID:
            found_artwork = artwork
            break

    if found_artwork:
        appraisal_value = random.randint(1000000, 999999999)
        print("Appraisal value of", found_artwork["Title"], "is approximately", appraisal_value)
    else:
        print("Artwork not found.")


#Edit Artwork Details
def edit_artwork():
    if admin_login():
        artworkID = int(input("Enter ID of artwork to edit: "))

        found_artwork = None
        for artwork in artworks:
            if int(artwork['ArtID']) == artworkID:
                found_artwork = artwork
                break

        if found_artwork:
            print("1. Edit Title")
            print("2. Edit Artist")
            print("3. Edit Year")
            print("4. Edit Medium")
            print("5. Edit Price")
            print("6. Edit Status")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                found_artwork['Title'] = input("Enter new title: ")
            elif choice == 2:
                found_artwork['Artist'] = input("Enter new artist: ")
            elif choice == 3:
                found_artwork['Year'] = int(input("Enter new year: "))
            elif choice == 4:
                found_artwork['Medium'] = input("Enter new medium: ")
            elif choice == 5:
                found_artwork['Price'] = float(input("Enter new price: "))
            elif choice == 6:
                found_artwork['Status'] = input("Enter new status: ")
            else:
                print("Invalid choice.")
            print("Artwork", found_artwork["Title"], "edited successfully.")
        else:
            print("Artwork not found.")
# Save artworks to CSV file
def save_artworks():
    if admin_login():
        with open('artworks.csv', 'w') as csvfile:
          fieldnames = ['ArtID','Title', 'Artist', 'Year', 'Medium', 'Price', 'Status']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

          writer.writeheader()
          for artwork in artworks:
              writer.writerow(artwork)
        with open('sold_artworks.csv', 'w') as csvfile:
          fieldnames = ['ArtID','Title', 'Artist', 'Year', 'Medium', 'Price', 'Status']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

          writer.writeheader()
          for artwork in sold_artworks:
              writer.writerow(artwork)
    else:
        print("Admin authentication failed.")

#change admin password
def change_password():
    if admin_login():
        new_password = input("Enter new password: ")
        with open("password.bin", 'wb') as passwordfile:
            pickle.dump(new_password, passwordfile)
        print("Password changed successfully.")
    else:
        print("Admin authentication failed.")

while True:
    print("Welcome to the Art Gallery Management System")
    print("1. Display all artworks")
    print("2. Display artworks by artist")
    print("3. Search artworks")
    print("4. Add a new artwork")
    print("5. Remove an artwork")
    print("6. Sell an artwork")
    print("7. Appraise an artwork")
    print("8. Edit Artworks")
    print("9. Save artworks")
    print("10. Change admin password")
    print("11. Exit")

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
        artworkID = int(input("Enter ID of artwork to remove: "))
        remove_artwork(artworkID)
    elif choice == 6:
        sell_artwork()
    elif choice == 7:
        artworkID = int(input("Enter ID of artwork to appraise: "))
        appraise_artwork(artworkID)
    elif choice == 8:
        edit_artwork()
    elif choice == 9:
        save_artworks()
    elif choice == 10:
        change_password()
    elif choice == 11:
        print("Thank you for using the Art Gallery Management System")
        break
    
    print("\n")


