
class E_book:

    def __init__(self,title,author,no_pages):
        self.title = title
        self.author = author
        self.no_pages = no_pages
        self.current_page = 0
        self.open = False


    def open_a_book(self):
        self.open = True
    
    def close_a_book(self):
        self.open = False
        
    def swipe_page_up(self):
        if self.open == True:
            if self.current_page < self.no_pages:
                self.current_page +=1
            else:
                print("End of book")
        else:
            print('The book is closed')

    def swipe_page_down(self):
        if self.open == True:
            if self.current_page > 0:
                self.current_page -= 1
        else:
            print('The book is closed')

    def book_status(self):

        print(f'Title:{self.title}\n'
              f'Author:{self.author}\n'
              f'Page numbers:{self.no_pages}\n'
              f'Current page no.:{self.current_page}')
    
    
