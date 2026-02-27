# Copyright by Emilio

import os


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return (f"Hey, I'm {self.name}! "
                f"My student ID is {self.student_id} "
                f"and I am {self.age} years old.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return (f"Hello, I am {self.name}. "
                f"I teach {self.subject} "
                f"and I am {self.age} years old.")


print("=" * 40)
print("TASK 1 - School Management System")
print("=" * 40)

student1 = Student("Alice", 16, "S001")
teacher1 = Teacher("Mr. Smith", 35, "Mathematics")

print(student1.introduce())
print(teacher1.introduce())
print(f"\nAge check: Student is {student1.age}, Teacher is {teacher1.age}")


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"'{self.title}' by {self.author} [ISBN: {self.isbn}]"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"  Added: {book.display_info()}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"  Removed: {book.display_info()}")
                return
        print(f"  ERROR: '{title}' not found!")

    def list_books(self):
        if len(self.books) == 0:
            print(f"  {self.name} has no books.")
            return
        print(f"\n  Books in '{self.name}':")
        for i, book in enumerate(self.books, start=1):
            print(f"    {i}. {book.display_info()}")

    def search_by_title(self, keyword):
        results = [b for b in self.books if keyword.lower() in b.title.lower()]
        if results:
            print(f"\n  Search results for '{keyword}': {len(results)} book(s)")
            for book in results:
                print(f"    -> {book.display_info()}")
        else:
            print(f"  No books found for: '{keyword}'")


print("\n" + "=" * 40)
print("TASK 2 - Library System")
print("=" * 40)

my_library = Library("City Library")

book1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
book2 = Book("The Web Application Hacker's Handbook", "Stuttard & Pinto", "978-1118026472")
book3 = Book("Hacking: The Art of Exploitation", "Jon Erickson", "978-1593271442")

print("\nAdding books:")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.list_books()

print()
my_library.search_by_title("Python")
my_library.search_by_title("Hacking")

print("\nRemoving book:")
my_library.remove_book("Python Crash Course")
my_library.list_books()


def file_manager():
    print("\n" + "=" * 40)
    print("TASK 3 - File Manager")
    print("=" * 40)

    current_directory = os.getcwd()
    print(f"\n  Current directory: {current_directory}")

    folder_name = "lab_files"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"  Folder created: '{folder_name}'")
    else:
        print(f"  Folder '{folder_name}' already exists")

    file_names = ["notes.txt", "fake_passwords.txt", "tasks.txt"]

    print(f"\n  Creating files:")
    for file in file_names:
        path = os.path.join(folder_name, file)
        with open(path, "w") as f:
            f.write(f"Content of {file}\nCreated for Week 9 Lab")
        print(f"    Created: {file}")

    print(f"\n  Files in '{folder_name}':")
    for file in os.listdir(folder_name):
        print(f"    - {file}")

    old_name = os.path.join(folder_name, "tasks.txt")
    new_name = os.path.join(folder_name, "week9_tasks_completed.txt")

    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"\n  Renamed: 'tasks.txt' -> 'week9_tasks_completed.txt'")

    print(f"\n  Files after renaming:")
    for file in os.listdir(folder_name):
        print(f"    - {file}")

    print(f"\n  Cleaning up:")
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        os.remove(file_path)
        print(f"    Deleted: {file}")

    os.rmdir(folder_name)
    print(f"  Folder '{folder_name}' deleted")
    print("\n  Cleanup completed successfully.")


file_manager()

print("\n" + "=" * 40)
print("All 3 tasks completed! :)")
print("=" * 40)
