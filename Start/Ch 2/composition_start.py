# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    
class Chapter:
    def __init__(self, name, pagecount) -> None:
        self.name = name
        self.pagecount = pagecount

class Book():
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        # result = 0 
        # for ch in self.chapters:
        #     result += ch.pagecount
        # return result
        return sum([ch.pagecount for ch in self.chapters])


a1 = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, a1)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.get_book_page_count())
