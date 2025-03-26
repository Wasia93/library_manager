import json

# File to store library data
LIBRARY_FILE = "library.txt"

# Load library from file (if exists)
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    })
    print("Book added successfully!")
    save_library(library)

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            save_library(library)
            return
    print("Book not found!")

# Search for a book
def search_book(library):
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter the search term: ").strip().lower()
    matches = [book for book in library if book["title"].lower() == query or book["author"].lower() == query]
    
    if matches:
        print("Matching Books:")
        for book in matches:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books found!")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for index, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("""
        Welcome to your Personal Library Manager!
        1. Add a book
        2. Remove a book
        3. Search for a book
        4. Display all books
        5. Display statistics
        6. Exit
        """)
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
