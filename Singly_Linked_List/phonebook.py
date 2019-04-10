from contact import Contact


class PhoneBook:
    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def create_fullname(self, name, surname):
        if surname == "":
            fullname = name
        else:
            fullname = "{} {}".format(name, surname)
        return fullname

    # add new node at the beginning of the sequence
    def add_contact(self, name, surname=""):
        if not self.contact_already_exists(self.create_fullname(name, surname)):
            return "Contact already exists. Choose a different name"
        new_contact = Contact(str(name), str(surname), self.root)
        self.root = new_contact
        self.size += 1

    def remove_contact(self, name, surname=""):
        this_node = self.root
        previous_node = None
        if surname != "":
            fullname = "{} {}".format(name, surname)
        else:
            fullname = str(name)
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
        return False  # data not found

    def add_contact_address(self, fullname, address):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.add_address(str(address))
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def add_contact_phone(self, fullname, phone_number):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.add_phone(str(phone_number))
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def add_contact_email(self, fullname, email):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.add_email_address(str(email))
                return True
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def edit_contact_phone(self, fullname, new_phone, index=0):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                return True if this_node.edit_phone(index, new_phone) else False
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def edit_contact_address(self, fullname, new_address, index=0):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                return True if this_node.edit_address(index, new_address) else False
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def edit_contact_email(self, fullname, new_email, index=0):
        this_node = self.root
        fullname = str(fullname)
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                return True if this_node.edit_email(index, new_email) else False
            else:
                this_node = this_node.get_next()
        return False  # data not found

    def contact_already_exists(self, fullname):
        this_node = self.root
        while this_node:
            if str(fullname) in this_node.get_name_and_surname():
                return False
            else:
                this_node = this_node.get_next()
        return True

    def edit_name(self, name, new_name, surname=""):
        fullname = self.create_fullname(name, surname)
        if not self.contact_already_exists(fullname):
            return "Contact already exists. Choose a different name"
        this_node = self.root
        while this_node:
            if this_node.get_name_and_surname() == fullname:
                this_node.edit_name(new_name)
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
            else:
                this_node = this_node.get_next()
        return False  # data not found

    # finds all contacts containing a string
    def find_contact(self, *argv):
        this_node = self.root
        returned_contacts = []
        while this_node:
            search_name = " ".join(argv)
            if search_name in this_node.get_name_and_surname():
                returned_contacts.append(this_node.get_name_and_surname())
                this_node = this_node.get_next()
            else:
                this_node = this_node.get_next()
        if returned_contacts:
            return returned_contacts
        return False

    def get_input_prompt(self, search_result):
        user_input = input("More than one contact corresponding:\n {}\nPlease type 1 to choose the first, "
                     "2 for the second...".format(" ,".join(search_result)))
        return user_input

    def valid_user_input(self, search_result):
        user_input = self.get_input_prompt(search_result)
        while not (int(user_input) <= len(search_result)):
            print("The number you chose is not correct. Please choose again")
            self.valid_user_input(search_result)
        out_index = int(user_input) -1
        return out_index

    def find_contact_info(self, name, surname=""):
        fullname = self.create_fullname(name, surname)
        search_result = self.find_contact(fullname)
        if self.find_contact(fullname) and len(search_result) != 1:
            contact_to_modify = search_result[self.valid_user_input(search_result)]
        else:
            contact_to_modify = search_result[0]
        this_node = self.root
        while this_node:
            if this_node.get_name_and_surname() == contact_to_modify:
                contact_details = "{}".format(this_node.get_all_contact_details)
                return contact_details
            else:
                this_node = this_node.get_next()
        return False

    def print_all_contact_details(self):
        this_node = self.root
        while this_node:
            print(this_node.get_all_contact_details())
            this_node = this_node.get_next()

