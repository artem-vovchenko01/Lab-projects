'''
Модуль опису Класу Html_Page для створенняHTML-сторінок
'''
import re
from book import Book
class Html_Page:
    '''
    Клас для створення HTML-сторінок
    '''
    def __init__(self, title, header):
        self.title = title
        self.heading = header
        self.f = open("Lab4/books.html","w")
        self.f.close()
        self.f = open("Lab4/books.html", "a")

    def generate_heading(self, color):
        '''
        Генерує заголовок сторінки
        '''
        self.f.write("<html>\n")
        self.f.write("<head>\n")
        self.f.write("<title>" + self.title + "</title>\n")
        self.f.write("</head>\n")
        self.f.write(f'<body bgcolor="{color}">\n')
        self.f.write("<h1 align=center>" + self.heading + "</h1>\n")
    def generate_body(self):
        '''
        Порожня функція - перевизначається в дочірньому класі
        '''
        pass
    def generate_trailer(self):
        '''
        Генерує завершальний код сторінки
        '''
        self.f.write("</body>\n")
        self.f.write("</html>\n")
    def generate(self,color):
        '''
        Збірання всієї сторінки із частин
        '''
        self.generate_heading(color)
        self.generate_body()
        self.generate_trailer()
        self.f.close()

titles = []
authors = []
subjects = []
urls = []

class Sorted_Page(Html_Page, Book):
    '''
    Створює HTML–сторінку зі списком книг, індексованих за автором
    '''
    def __init__(self, method, file):
        Book.__init__(self)
        Html_Page.__init__(self, f"Python Books: by {method}", f"<i>Python Books: indexed by {method}</i>")
        self.f = open(f"Lab4/{file}.html", "w")
        bk = Book()
        self.set_book_list(bk.sort(bk.parseBooks()[0], method))
    def set_book_list(self, lst):
        self.book_list = lst
    def generate_body(self):
        '''
        Створити таблицю
        '''
        self.f.write("<hr>\n")
        self.f.write("<table border=0 width=" + '"' + "80%" + '"' + ">\n")
        self.f.write("""
        <tr>
        <th>Author</th>
        <th>Title</th>
        <th>Subject</th>
        <th>Link</th>
        </tr>
        """)
        
        for book in self.book_list:
            author = book["author"]
            title = book["title"]
            subject = book["subject"]
            link = book["url"]

            self.f.write(f"""<tr> 
            <td align="center">{author}</td>
            <td align="center">{title}</td>
            <td align="center">{subject}</td>
            <td align="center"">{link}</td>
            </tr>""")

        self.f.write("</table>\n \n<hr>\n")
        self.f.write("<p>There are " + str( Book.parseBooks(self)[1] ) + " books in the list</p>\n")
    def generate_trailer(self):
        Html_Page.generate_trailer(self)


if __name__ == "__main__":
    p = Html_Page("Це заголовок", "<i>Це заголовок зверху сторінки</i>")
    p.generate("lightblue")
    new_p = Sorted_Page("author","books_by_author")
    new_p.generate("lightblue")
    new_p2 = Sorted_Page("subject","books_by_subject")
    new_p2.generate("lightblue")
    new_p3 = Sorted_Page("title","books_by_title")
    new_p3.generate("lightblue")