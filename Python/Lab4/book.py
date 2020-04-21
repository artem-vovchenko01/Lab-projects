import re
class Book():
    def parseBooks(self):
        book = {}
        books = []
        count = 0
        counter = 0
        with open("Lab4/book_list.txt") as f:
            text = f.readlines()
        
        for line in text:
            if re.search(r"\s*title\s*:\s*", line) != None:
                if count == 1:
                    books.append(book)
                    book = {}
                    count = 0 
                newline = re.sub(r"\s*title\s*:\s*", "", line)
                self.setTitile(book, newline[:-1])
                count += 1
                counter += 1
                
            if re.search(r"\s*author\s*:\s*", line) != None:
                newline = re.sub(r"\s*author\s*:\s*", "", line)
                self.setAuthor(book, newline[:-1])

            if re.search(r"\s*subject\s*:\s*", line) != None:
                newline = re.sub(r"\s*subject\s*:\s*", "", line)
                self.setSubject(book, newline[:-1])

            if re.search(r"\s*url\s*:\s*", line) != None:
                newline = re.sub(r"\s*url\s*:\s*", "", line)
                self.setURL(book, newline)
            
        books.append(book)
        book = {}
        books = [books, counter]
        return books

    def setTitile(self, book, title):
        book["title"] = title
    
    def setAuthor(self, book, author):
        book["author"] = author

    def setSubject(self, book, subject):
        book["subject"] = subject

    def setURL(self, book, url):
        book["url"] = url

    def sort(self, books, method):
        books = sorted(books, key = lambda k: k[f"{method}"])
        return books