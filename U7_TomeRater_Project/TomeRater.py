class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('Email Address updated')

    def __repr__(self):
        print('User '+self.name+' email: '+self.email+' Books read: '+str(len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user and self.email == other_user.email:
            print("users are identical")

    def read_book(self, book, rating='None'):
        #print('in the read_book function')
        self.books[book] = rating

    def get_average_rating(self):
        cnt = 0
        total = 0
        for rating in self.books:
            total += rating
            cnt += 1
        return total / cnt

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title  

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("This book's isbn has been updated")

    def add_rating(self, rating):
        print(rating)
        if rating <= 4 and rating > 0:
            self.ratings.append(rating)
            print('rating added')
        else:
            print("Invalid Rating")
        #for val in self.ratings:
        print(len(self.ratings))

    def __repr__(self):
        return (self.title+' isbn: '+str(self.isbn)) 

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print("The books are the same")

    def get_average_rating(self):
        #cnt = len(self.ratings)
        cnt = 0
        total = 0
        print(cnt)
        for rating in self.ratings:
            total += rating
            cnt += 1
        return total / cnt

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return (self.title+', a '+self.level+' manual on '+self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title,isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self,book,email,rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book,rating)
            add_book = Book(book.title,book.isbn)
            add_book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email! "+email)

    def add_user(self, name, email, user_books = 'None'):
        new_user = User(name, email)
        self.users[email] = new_user 
        if user_books != 'None':
            for book in user_books:
                self.add_book_to_user(book, email, rating=0 )

    def print_catalog(self):
        print('*** Our Catalog ***')
        for book in self.books:
            print(book)

    def print_users(self):
        print('*** Our Users ***')
        for user in self.users:
            print(user)

    def most_read_book(self):
        key_max = max(self.books.keys(), key=(lambda k: self.books[k]))
        return key_max

    def highest_rated_book(self):
        for item in self.books:
            Book.get_average_rating(item)

    def most_positive_user(self):
        for user in self.users:
            self.users[user].get_average_rating()

