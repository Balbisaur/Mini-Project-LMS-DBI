from library_system_connection import connect_db, Error

def add_book(connection):
    try:
        title = input("Enter the title of the book: ")
        book_id = input("Enter the id of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        publication_date = input("Enter the publication date of the book: ")

        if not title or not book_id or not isbn or not publication_date: # checking if the user has entered all the fields
            print("Inalid input, must include all fields.") 
            return

        sql = "INSERT INTO books (title, isbn, publication_date) VALUES (%s, %s, %s)" # inserting a new book into the database
        values = (title, book_id, isbn, publication_date)

        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        print("Book added successfully!")
    except Error as e:
        print(f"Error: {e}")


def borrow_book(connection):
    print("Borrowing a book")
    user_id = input("Enter your id: ")
    book_id = input("Enter the books id you'd like to borrow: ")

    
    if not user_id.isdigit() or not book_id.isdigit():
        print(" Numbers only bucko.")
        return

    try:
        
        cursor = connection.cursor()

        update_sql = "UPDATE books SET availability = 0 WHERE id = %s AND availability = 1" # updating the availability of the book to 0
        cursor.execute(update_sql, (book_id,))
        if cursor.rowcount == 0: # checking if the book exists
            raise ValueError(" Book does not exist.")

       
        insert_sql = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)" # inserting the borrowed book into the database
        cursor.execute(insert_sql, (user_id, book_id))

        
        connection.commit()
        print("Book borrowed successfully!") # returning if the book is borrowed successfully

    except Error as e:
        print(f"Error: {e}")

def return_book(connection):
    print("Return a book")
    user_id = input("Enter the user ID ")
    book_id = input("Enter the book ID ")


    try:
       
        cursor = connection.cursor()

       
        update_book_sql = "UPDATE books SET availability = 1 WHERE id = %s" # updating the availability of the book to 1
        cursor.execute(update_book_sql, (book_id,))
        if cursor.rowcount == 0: # checking if the book exists
            raise ValueError(" Book not found.")

        
        update_borrowed_sql = "UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s AND return_date IS NULL" # updating the return date of the book to the current date
        cursor.execute(update_borrowed_sql, (user_id, book_id))
        if cursor.rowcount == 0: 
            raise ValueError(" Book not borrowed by the specified user.") # returning if the book is returned successfully

        
        connection.commit()
        print("Book returned successfully!")

    except Error as e:
        print(f"Error: {e}")

def display_all_books(connection):
    try:
      
        cursor = connection.cursor()

        select_sql = "SELECT * FROM books"
        cursor.execute(select_sql)

   
        books = cursor.fetchall()

        for book in books:
            book_id, title, isbn, publication_date, availability = book
            print(f"{book_id}| {title}| {isbn}| {publication_date}| {'Available' if availability else 'Not Available'}") # DISPLAYING ALL BOOKS IN THE DATABASE

    except Error as e:
        print(f"Error: {e}")

   




def search_book_by_title(connection):
    print("Search for a book by title")
    title = input("Enter the title of the book: ")

    try:
     
        cursor = connection.cursor()
        search_sql = "SELECT * FROM books WHERE title LIKE %s" # searching for a book by title
        cursor.execute(search_sql, (title)) 

  
        books = cursor.fetchall()

        if not books:
            print("No books found.")
        else:
            
           

          
            for book in books:
                book_id, title, isbn, publication_date, availability = book
                print(f"{book_id}| {title}| {isbn}| {publication_date}| {'Available' if availability else 'Not Available'}")

    except Error as e:
        print(f"Error: {e}")

  