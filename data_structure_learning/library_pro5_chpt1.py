class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out_patron = None
        self.holding_patrons = []

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Patron(object):
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    p1 = Patron('Bob')
    b1 = Book('Hi', 'Rob')

    assert(str(p1) == 'Bob')
    assert(str(b1) == 'Hi')

    print 'The program is running smoothly'

#DONE
