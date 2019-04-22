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
            if value["name and surname"] == [name, surname]:
                del self.phonebook[key]
                self.contact_index -= 1
                return True
        print("trying to delete {} {}. data not found".format(name, surname))
        return False

    def contact_already_exists(self, name, surname=""):
        for key, value in self.phonebook.items():
            if (value.contact["name and surname"][0] == name) and (value.contact["name and surname"][1] == surname):
                return True
        return False

    def edit_name(self, name, new_name, surname=""):
        if self.contact_already_exists(new_name, surname):
            return "Contact already exists. Choose a different name"
        for key, value in self.phonebook.items():
            if value["Name and surname"] == [name, surname]:
                value["Name and surname"][0] = new_name
                return True
        return False  # data not found

    def edit_surname(self, name, new_surname, surname=""):
        if self.contact_already_exists(name, new_surname):
            return "Contact already exists. Choose a different name"
        for key, value in self.phonebook.items():
            if value["Name and surname"] == [name, surname]:
                value["Name and surname"][1] = new_surname
                return True
        return False  # data not found

    # finds all contacts containing a string
    def find_contacts(self, name, surname=""):
        returned_contacts = []
        search_name = "{} {}".format(name, surname)
        for key, value in self.phonebook.items():
            if "{} {}".format(value["Name and surname"][0], value["Name and surname"][1]) == search_name:
                returned_contacts.append(key)
        if returned_contacts:
            return returned_contacts
        return False

    def print_all_contact_details(self):
        return_string = ""
        for key, value in self.phonebook.items():
            return_string += " ".join(value.get_all_contact_details())
        print(return_string)
        return return_string

