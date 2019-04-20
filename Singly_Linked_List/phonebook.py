from .contact import Contact


class PhoneBook:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    @staticmethod
    def create_fullname(name, surname):
        if surname == "":
            fullname = str(name)
        else:
            fullname = "{} {}".format(name, surname)
        return fullname

    # add new node at the beginning of the sequence
    def add_contact(self, name, surname=""):
        print ("fullname" + self.create_fullname(name, surname))
        if self.contact_already_exists(self.create_fullname(name, surname)):
            print("Contact already exists. Choose a different name")
            return False
        new_contact = Contact(str(name), str(surname), self.root)
        self.root = new_contact
        self.size += 1

    def remove_contact(self, name, surname=""):
        this_node = self.root
        previous_node = None
        fullname = self.create_fullname(name, surname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                if previous_node:
                    previous_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                previous_node = this_node
                this_node = this_node.get_next()
        print ("trying to delete {}. data not found".format(fullname))
        return False  # data not found

    def contact_already_exists(self, fullname):
        this_node = self.root
        while this_node:
            if str(fullname) == this_node.get_name_and_surname():
                return True
            else:
                this_node = this_node.get_next()
        return False

    def edit_name(self, name, new_name, surname=""):
        fullname = self.create_fullname(name, surname)
        if not self.contact_already_exists(fullname):
            return "Contact already exists. Choose a different name"
        this_node = self.root
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.edit_name(new_name)
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def edit_surname(self, name, new_surname, surname=""):
        fullname = self.create_fullname(name, surname)
        if not self.contact_already_exists(fullname):
            return "Contact already exists. Choose a different name"
        this_node = self.root
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.edit_surname(new_surname)
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    # finds all contacts containing a string
    def find_contacts(self, name="", surname=""):
        this_node = self.root
        returned_contacts = []
        while this_node:
            search_name = self.create_fullname(name, surname)
            if search_name in this_node.get_name_and_surname():
                returned_contacts.append(this_node.get_name_and_surname())
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()
        if returned_contacts:
            return returned_contacts
        return False

    def print_all_contact_details(self):
        this_node = self.root
        return_string = ""
        while this_node:
            return_string += this_node.get_all_contact_details()
            this_node = this_node.get_next()
        print(return_string)
        return return_string

