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
