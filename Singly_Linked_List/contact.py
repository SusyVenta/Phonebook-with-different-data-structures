from .phone import Phone
from .address import Address
from .email_address import Email


class Contact:
    def __init__(self, name, surname="", n=None):
        self.first_name = name
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email_address = Email()
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_all_contact_details(self):
        contact_info = 'Contact details of {} {}: \n'.format(self.first_name, self.surname)
        contact_info += self.phone.get_all_phones() + "\n" + self.address.get_all_addresses() + "\n" + \
                        self.email_address.get_emails()
        return contact_info

    def get_name_and_surname(self):
        if self.surname != "":
            return "{} {}".format(self.first_name, self.surname)
        return self.first_name

    def set_surname(self, surname):
        self.surname = surname

    def edit_name(self, new_name):
        self.first_name = new_name

    def edit_surname(self, new_surname):
        self.surname = new_surname
