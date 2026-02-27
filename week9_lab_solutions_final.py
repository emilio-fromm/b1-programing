# Copyright by Emilio

import os


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, ich bin {self.name} und bin {self.age} Jahre alt."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return (f"Hey, ich bin {self.name}! "
                f"Meine Studenten-ID ist {self.student_id} "
                f"und ich bin {self.age} Jahre alt.")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return (f"Guten Tag, ich bin {self.name}. "
                f"Ich unterrichte {self.subject} "
                f"und bin {self.age} Jahre alt.")


print("=" * 40)
print("AUFGABE 1 - School Management System")
print("=" * 40)

student1 = Student("Alice", 16, "S001")
lehrer1 = Teacher("Mr. Smith", 35, "Mathematics")

print(student1.introduce())
print(lehrer1.introduce())
print(f"\nAlters-Check: Student ist {student1.age}, Lehrer ist {lehrer1.age}")


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"'{self.title}' von {self.author} [ISBN: {self.isbn}]"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"  Hinzugefuegt: {book.display_info()}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"  Entfernt: {book.display_info()}")
                return
        print(f"  FEHLER: '{title}' nicht gefunden!")

    def list_books(self):
        if len(self.books) == 0:
            print(f"  {self.name} hat keine Buecher.")
            return
        print(f"\n  Buecher in '{self.name}':")
        for i, book in enumerate(self.books, start=1):
            print(f"    {i}. {book.display_info()}")

    def search_by_title(self, keyword):
        results = [b for b in self.books if keyword.lower() in b.title.lower()]
        if results:
            print(f"\n  Suchergebnis fuer '{keyword}': {len(results)} Buch/Buecher")
            for book in results:
                print(f"    -> {book.display_info()}")
        else:
            print(f"  Keine Buecher gefunden fuer: '{keyword}'")


print("\n" + "=" * 40)
print("AUFGABE 2 - Library System")
print("=" * 40)

meine_bibliothek = Library("Stadtbibliothek")

buch1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
buch2 = Book("The Web Application Hacker's Handbook", "Stuttard & Pinto", "978-1118026472")
buch3 = Book("Hacking: The Art of Exploitation", "Jon Erickson", "978-1593271442")

print("\nBuecher hinzufuegen:")
meine_bibliothek.add_book(buch1)
meine_bibliothek.add_book(buch2)
meine_bibliothek.add_book(buch3)

meine_bibliothek.list_books()

print()
meine_bibliothek.search_by_title("Python")
meine_bibliothek.search_by_title("Hacking")

print("\nBuch entfernen:")
meine_bibliothek.remove_book("Python Crash Course")
meine_bibliothek.list_books()


def file_manager():
    print("\n" + "=" * 40)
    print("AUFGABE 3 - File Manager")
    print("=" * 40)

    aktuelles_verzeichnis = os.getcwd()
    print(f"\n  Aktuelles Verzeichnis: {aktuelles_verzeichnis}")

    ordner_name = "lab_files"

    if not os.path.exists(ordner_name):
        os.mkdir(ordner_name)
        print(f"  Ordner erstellt: '{ordner_name}'")
    else:
        print(f"  Ordner '{ordner_name}' existiert bereits")

    datei_namen = ["notizen.txt", "paswoerter_NICHT_ECHT.txt", "aufgaben.txt"]

    print(f"\n  Dateien erstellen:")
    for datei in datei_namen:
        pfad = os.path.join(ordner_name, datei)
        with open(pfad, "w") as f:
            f.write(f"Inhalt von {datei}\nErstellt fuer Week 9 Lab")
        print(f"    Erstellt: {datei}")

    print(f"\n  Dateien in '{ordner_name}':")
    for datei in os.listdir(ordner_name):
        print(f"    - {datei}")

    alter_name = os.path.join(ordner_name, "aufgaben.txt")
    neuer_name = os.path.join(ordner_name, "week9_aufgaben_erledigt.txt")

    if os.path.exists(alter_name):
        os.rename(alter_name, neuer_name)
        print(f"\n  Umbenannt: 'aufgaben.txt' -> 'week9_aufgaben_erledigt.txt'")

    print(f"\n  Dateien nach Umbenennung:")
    for datei in os.listdir(ordner_name):
        print(f"    - {datei}")

    print(f"\n  Aufraeumen:")
    for datei in os.listdir(ordner_name):
        datei_pfad = os.path.join(ordner_name, datei)
        os.remove(datei_pfad)
        print(f"    Geloescht: {datei}")

    os.rmdir(ordner_name)
    print(f"  Ordner '{ordner_name}' geloescht")
    print("\n  Alles sauber! Cleanup abgeschlossen.")


file_manager()

print("\n" + "=" * 40)
print("Alle 3 Aufgaben fertig! :)")
print("=" * 40)
