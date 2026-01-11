class Contact_List:
    def __init__(self):
        self.contacts = []


    def add_new_contact(self, contact):
        self.contacts.append(contact)

    def display_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Email: {contact.email}")
            print(f"Phone: {contact.telephone}")
            print()
        