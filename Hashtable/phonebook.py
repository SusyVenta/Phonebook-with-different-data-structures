from .contact import Contact


class PhoneBook:
    def __init__(self):
        self.phonebook = {}
        self.contact_index = 1

    def get_size(self):
        return len(self.phonebook)

    @staticmethod
    def create_fullname(name, surname):
        if surname == "":
            fullname = str(name)
        else:
            fullname = "{} {}".format(name, surname)
        return fullname

    def add_contact(self, name, surname=""):
        if self.contact_already_exists(name, surname):
            print("Contact already exists. Choose a different name")
            return False
        new_contact = Contact(name, surname)
        self.phonebook[self.contact_index] = new_contact
        self.contact_index += 1
        return True

    def remove_contact(self, name, surname=""):
        for key, value in self.phonebook.items():
            if "{} {}".format(value.first_name, value.surname) == "{} {}".format(name, surname):
                del self.phonebook[key]
                self.contact_index -= 1
                return True
        print("trying to delete {} {}. data not found".format(name, surname))
        return False

    def contact_already_exists(self, name, surname=""):
        for key, value in self.phonebook.items():
            if (value.first_name == name) and (value.surname == surname):
                return True
        return False

    def edit_name(self, name, new_name, surname=""):
        if self.contact_already_exists(new_name, surname):
            return "Contact already exists. Choose a different name"
        for key, value in self.phonebook.items():
            if "{} {}".format(value.first_name, value.surname) == "{} {}".format(name, surname):
                value.first_name = new_name
                return True
        return False  # data not found

    def edit_surname(self, name, new_surname, surname=""):
        if self.contact_already_exists(name, new_surname):
            return "Contact already exists. Choose a different name"
        for key, value in self.phonebook.items():
            if "{} {}".format(value.first_name, value.surname) == "{} {}".format(name, surname):
                value.surname = new_surname
                return True
        return False  # data not found

    def find_contacts(self, name, surname=""):
        search_name = "{} {}".format(name, surname)
        for key, value in self.phonebook.items():
            if "{} {}".format(value.first_name, value.surname) == search_name:
                return value
        return False

    def print_all_contact_details(self):
        return_string = ""
        for key, value in self.phonebook.items():
            return_string += "".join(value.get_all_contact_details())
        return return_string

