from ..Common_elements.phone import Phone
from ..Common_elements.address import Address
from ..Common_elements.email_address import Email


class Contact:
    def __init__(self, name, surname=""):
        self.first_name = name
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email_address = Email()

    def get_all_contact_details(self):
        contact_info = '{} {}:\n{}\n{}\n{}\n'.format(self.first_name, self.surname, self.phone.get_all_phones(),
                                                     self.address.get_all_addresses(), self.email_address.get_emails())
        return contact_info

    def get_name(self):
        return self.first_name

    def get_surname(self):
        return self.surname

    def get_name_and_surname(self):
        if self.surname != "":
            return "{} {}".format(self.first_name, self.surname)
        return self.first_name

    def set_surname(self, surname):
        self.surname = surname

    def set_name(self, new_name):
        self.first_name = new_name
