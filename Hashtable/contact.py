from .phone import Phone
from .address import Address
from .email_address import Email


class Contact:
    def __init__(self, name, surname=""):
        self.first_name = name
        self.surname = surname
        self.phone = Phone()
        self.address = Address()
        self.email_address = Email()
        self.contact = {"name and surname": [name, surname], "phone": self.phone, "address": self.address, "emails": self.email_address}

    def get_all_contact_details(self):
        name = self.contact["name and surname"][0]
        surname = self.contact["name and surname"][1]
        contact_info = ['{} {}'.format(name, surname), self.phone.get_all_phones(), self.address.get_all_addresses(),
                        self.email_address.get_emails()]
        return contact_info

    def get_name(self):
        return self.contact["name and surname"][0]

    def get_surname(self):
        return self.contact["name and surname"][1]

    def get_name_and_surname(self):
        name = self.contact["name and surname"][0]
        surname = self.contact["name and surname"][1]
        if self.contact["name and surname"][1] != "":
            return "{} {}".format(name, surname)
        return name

    def set_surname(self, surname):
        self.contact["name and surname"][1] = surname

    def set_name(self, new_name):
        self.contact["name and surname"][0] = new_name
