#Assignment 12.3
#August 3rd, 2023
#Jeff Haberman
#CYBR 410
#WhatABook program to allow customers to browse in-store book listings, add books to their wishlist, view store hours and locations

#Import necessary mods
import sys, time

#import mysql connector for db connection commands
import mysql.connector
from mysql.connector import errorcode

#create login credentials for mysql database connection
config = {
    'user': 'whatabook_user',
    'password': 'MySQL8IsGreat!',
    'host': '127.0.0.1',
    'database': "whatabook",
    'raise_on_warnings': True
}

#Creating Menu method for selection on lookup
def show_menu():
  #Display default menu for the application
    print("\nWelcome to WhatABook Desktop Application!\n")
    print("\nMain Menu\n")
    print("[1.] View Books")
    print("[2.] View Store Locations")
    print("[3.] My Account")
    print("[4.] Exit program")
    try:
        option = int(input("Select option [1-4]: "))

        return option
    #If invalid option is entered, program is terminated
    except ValueError:
        print("\nInvalid number, program terminated...\n")

        sys.exit(0)
#Creating Show Books method
def show_books(_cursor):
    #SELECT statement to show all books
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")

    #Put results into variable for printing
    books = _cursor.fetchall()
    
    #Print results
    print("\n -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("Book Name: {}\nAuthor: {}\nDetails: {}\n".format(book[0], book[1], book[2]))

#Creating Show Locations method
def show_locations(_cursor):
    #SELECT statement to pull locations
    _cursor.execute("SELECT store_id, locale FROM store")

    #Put results into variable for printing
    locations = _cursor.fetchall()

    #Print results
    print ("\n -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("Locale: {}\n".format(location[1]))

#Creating Validate User method
def validate_user():
    #Get Customer ID input, if invalid number then exit program
    try:
        user_id = int(input("Enter your Customer ID: "))

        if user_id < 0 or user_id > 3:
            print("\nInvalid customer number, program terminated...\n")
            sys.exit("Exiting application now")
        return user_id
    
    #If invalid option is entered, program is terminated
    except ValueError:
        print("\n Invalid number, program terminated...\n")
        sys.exit("Exiting application now")

#Creating Show Account menu method
def show_account_menu():
   #Display the menu for the user account
    try:
        print("\n-- Customer Menu --\n")
        print("[1.] View Wishlist")
        print("[2.] Add Book to Wishlist")
        print("[3.] Main Menu")
        wishlist_option = int(input("Selection an option [1-3]: "))
        return wishlist_option
    
    #If invalid option is entered, program is terminated
    except ValueError:
        print("\nInvalid number, program terminated...\n")
        sys.exit(0)
    return wishlist_option

#Creating Wishlist method
def show_wishlist(_cursor, _user_id):

    #INNER JOIN query to pull all book info for books on user's wishlist
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    #Put results into variable for printing
    wishlist = _cursor.fetchall()

    #Print results
    print("\n -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("Book Name: {}\nAuthor: {}\n".format(book[4], book[5]))

#Creating available books method
def show_books_to_add(_cursor, _user_id):
    #Query list of books to add to user's wishlist
    book_query = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    _cursor.execute(book_query)

    books_to_add = _cursor.fetchall()

    print("\n -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("Book ID: {}\nBook Name: {}\n".format(book[0], book[1]))

#INSERT statement to add selected book to wishlist   
def add_book_to_wishlist(_cursor, _user_id, _book_id):
   _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#try/catch block for handling potential MySQL database errors
try:
    #connect to the WhatABook database 
    db = mysql.connector.connect(**config)
        
    #Setting cursor for DB queries
    cursor = db.cursor()

    #
    user_selection = show_menu()
        
    while user_selection != 4:      
        if user_selection == 1:
            #Show all available books
            show_books(cursor) 

        if user_selection == 2:
            #Show all store locations
            show_locations(cursor)

        if user_selection == 3:
            #Get user input for User ID 
            my_user_id = validate_user()
            #If a valid User ID is entered, show the account menu
            account_option = show_account_menu()
    
            while account_option != 3:
                    
                #If user selects 1 then show the user's current wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                #If user selects 2, show available books and prompt user to add books to wishlist
                if account_option == 2:
                            
                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("\nEnter the Book ID you want to add: "))

                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()

                    print("\nBook ID: {} was added to your wishlist!".format(book_id))

                #If an incorrect number is selected for show_account_menu give error message
                if account_option <0 or account_option>3:
                    print("\nYou have entered an incorrect value. Please try again.\n")
                    time.sleep(3)
                    
                #Show account menu
                account_option = show_account_menu()

        if user_selection<0 or user_selection>4:
            print("\nYou have entered an incorrect value. Please try again.\n")
            time.sleep(3)

        user_selection = show_menu()
  
    sys.exit("\nEnding the application now.\n")

#MySQL error handling            
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)    

    #Close database connection
finally:
        db.close()   