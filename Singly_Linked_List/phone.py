class Phone:
    def __init__(self, phone_type="Mobile", phone=""):
        self.type = phone_type
        self.phone = phone
        self.phones = {"Mobile": [], "Home": [], "Work": []}
        self.phone_index = 0

    def get_phone(self, phone_type):
        return self.phones[phone_type]

    def get_all_phones(self):
        all_phones = []
        for phone_type, phone_list in self.phones.items():
            for phone in phone_list:
                all_phones.append("{} Phone: {}\n".format(phone_type, phone))
        return "".join(all_phones)

    def add_phone(self, phone, phone_type="Mobile"):
        self.phones[phone_type].append(phone)

    def has_only_one_phone(self, phone_list):
        return len(phone_list) == 1

    def get_user_index(self):
        index_phone_to_modify = int(input("More than one phone number recorded\nPlease type 1 to modify the "
                                          "first, 2 for the second, etc.")) - 1
        return index_phone_to_modify

    def is_valid_user_input(self, phone_list):
        user_index = self.get_user_index()
        if not (len(phone_list) - 1 >= user_index > 0):
            print("The number you chose is not correct. Please choose again")
            return False
        self.phone_index = user_index
        return True

    def modify_phone(self, phone, phone_type="Mobile"):
        if self.has_only_one_phone(self.phones[phone_type]):
            self.phones[phone_type][0] = phone
        else:
            if self.is_valid_user_input(self.phones[phone_type]):
                self.phones[phone_type][self.phone_index] = phone
