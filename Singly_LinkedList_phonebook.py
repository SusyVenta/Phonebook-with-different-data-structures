class Contact:
    def __init__(self, name, surname="", n=None):
        self.first_name = name
        self.surname = surname
        self.phone = []
        self.address = []
        self.email_address = []
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_all_contact_details(self):
        contact_info = '"Contact details of {} {}: \n"'.format(self.first_name, self.surname)
        for index, phone in enumerate(self.phone):
            contact_info += "phone {}: {}\n".format(index+1, phone)
        for index, address in enumerate(self.address):
            contact_info += "address {}: {}\n".format(index+1, address)
        for index, email in enumerate(self.email_address):
            contact_info+= "email {}: {}\n".format(index+1, email)
        return contact_info

    def get_name_and_surname(self):
        if self.surname != "":
            return "{} {}".format(self.first_name, self.surname)
        return self.first_name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_email_address(self):
        return self.email_address

    def set_surname(self, surname):
        self.surname = surname

    def add_phone(self, phone):
        self.phone.append(phone)

    def add_address(self, address):
        self.address.append(address)

    def add_email_address(self, email):
        self.email_address.append(email)

    def edit_phone(self, index, new_phone):
        try:
            self.phone[index] = new_phone
            return True
        except IndexError:
            return False

    def edit_address(self, index, new_address):
        try:
            self.address[index] = new_address
            return True
        except IndexError:
            return False

    def edit_email(self, new_email, index):
        try:
            self.email_address[index] = new_email
            return True
        except IndexError:
            return False

    def edit_name(self, new_name):
        self.first_name = new_name

    def edit_surname(self, new_surname):
        self.surname = new_surname


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

new_linkedList = PhoneBook()
new_linkedList.add_contact("Susanna Ventafridda")
new_linkedList.add_contact("Susanna", "Ventafridda")
new_linkedList.add_contact(12)
print("size="+str(new_linkedList.get_size()))
new_linkedList.remove_contact(8)
print("size="+str(new_linkedList.get_size()))
print(new_linkedList.remove_contact(12))
print("size="+str(new_linkedList.get_size()))
new_linkedList.add_contact("susanna", "ventafridda")
new_linkedList.add_contact("paolo")
print("size="+str(new_linkedList.get_size()))
print(new_linkedList.find_contact("susanna"))
print("printing values:")
print(new_linkedList.print_all_contact_details())
print("size="+str(new_linkedList.get_size()))
print(new_linkedList.add_contact_phone("susanna ventafridda", "33333 3333"))
print(new_linkedList.add_contact_phone("susanna ventafridda", "0000 3333"))
print(new_linkedList.add_contact_address("susanna ventafridda", "rue js, 7, lux"))
print(new_linkedList.add_contact_email("susanna ventafridda", "aaa@amazon.lu"))
print(new_linkedList.print_all_contact_details())
print(new_linkedList.edit_contact_phone("susanna ventafridda", "555 555 555", 0))
print(new_linkedList.edit_surname("susanna ventafridda", "venta"))
print(new_linkedList.print_all_contact_details())
