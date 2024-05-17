from user import *
from library_system_connection import connect_db, Error
from book import *



def display_main_menu(connection):
    print("Welcome to the library managment system!")
    print("****")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Quit")

def display_book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def display_user_operations_menu(connection):
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")





def main():
    connection = connect_db()
    if connection is None:
        print("Failed to connect to the database.") 
        return

    try:
        while True:
            display_main_menu(connection)
            choice = input("Enter your choice: ")

            if choice == "1":
                display_book_operations_menu()
                book_choice = input("Enter your choice: ")
                if book_choice == "1":  
                    add_book(connection) # adding a book to the database

                elif book_choice == "2":  
                    borrow_book(connection) # borrowing a book

                elif book_choice == '3':  
                    return_book(connection) # returning a book

                elif book_choice == '4':  
                    search_book_by_title(connection) # searching for a book by title

                elif book_choice == '5':  
                    display_all_books(connection) # displaying all books in the database

            elif choice == "2":
                display_user_operations_menu(connection)
                user_choice = input("Enter your choice: ")
                if user_choice == "1":  
                    add_new_user(connection) # adding a user to the database

                elif user_choice == "2":  
                    view_user_details(connection) # viewing a user's details

                elif user_choice == "3":  
                    display_all_users(connection) # displaying all users

            elif choice == "3":
               
                break
            else:
                print("Invalid choice")
    finally:
        if connection and connection.is_connected(): # closing the connection to the database
            connection.close()





main() # calling the main function