import mysql.connector
from mysql.connector import Error

def add_new_user(connection):
    print("Add a new user")
    name = input("Enter your name: ")
    email = input("Email: ")
    id = input("ID: ")
    try:
        cursor = connection.cursor()

        select_sql = "SELECT * FROM users WHERE email = %s" # checking if the user already exists
        cursor.execute(select_sql, (email, id))
        user_exists = cursor.fetchone() 
        if user_exists:
            print("User already exists.") # returning if the user already exists
            return

       
        new_sql = "INSERT INTO users (name, email) VALUES (%s, %s)" # inserting a new user into the database
        cursor.execute(new_sql, (name, email, id))                        
        connection.commit()
        
        print("user added successfully!")

    except Error as e:
        print(f"Error: {e}")

def view_user_details(connection):
    print("View user details")
    user_id = input("Enter the user ID: ")

    try:
        
        cursor = connection.cursor()

    
        select_sql = "SELECT * FROM users WHERE id = %s"

   
        cursor.execute(select_sql, (user_id,))

       
        user = cursor.fetchone()        

        if user: # checking if the user exists
            print( user[0])  
            print( user[1])
            print( user[2])
        else:
            print("user not found.")

    except Error as e: # returning if the user doesnt exists
        print(f"Error: {e}")

def display_all_users(connection):
    try:
        
        cursor = connection.cursor()

     
        select_sql = "SELECT * FROM users"

       
        cursor.execute(select_sql)

     
        users = cursor.fetchall()

        if not users:
            print("No users found.")
        else:
            print("Users Displayed")
        
        
            for user in users:
                user_id, name, email = user # unpacking the user tuple into variables to print the user details
                print(f"{user_id}| {name}| {email}")

    except Error as e:
        print(f"Error: {e}")

 
