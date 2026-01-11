from ebook import E_book

def main():

    my_ebook = E_book("Wiedźmin", "Sapkowski", 300)

    my_ebook.open_a_book()
    my_ebook.book_status()
    my_ebook.swipe_page_up()
    my_ebook.swipe_page_up()
    my_ebook.book_status()
    my_ebook.close_a_book()
    my_ebook.swipe_page_up()

if __name__ == "__main__":
    main()



