from contact import Contact
from contact_list import Contact_List

def main():

    my_contacts = Contact_List()

    c1 = Contact('John Brown','brown@onet.pl',555234000)
    c2 = Contact('Anna May' , 'am@o2.pl' , 232000199)
    c3 = Contact('George Small' , 'smallg@google.pl' , 22299910)
    c4 = Contact('Paola Big' , 'bigpaola@poczta.pl', 100200300)

    my_contacts.add_new_contact(c1)
    my_contacts.add_new_contact(c2)
    my_contacts.add_new_contact(c3)
    my_contacts.add_new_contact(c4)

    my_contacts.display_contact_list()


if __name__ == "__main__":
    main()

        