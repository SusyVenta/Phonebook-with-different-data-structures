from .contact import Contact


# class PhoneBook == HashTable
# collision resolution technique: quadratic probing
class PhoneBook:
    def __init__(self):
        # initial capacity set to 16 as in Java HashMap
        self.initial_size = 16
        self.current_size = 16
        self.phone_book_buckets = [None]*self.initial_size
        self.phone_book_data = [None]*self.initial_size
        # load factor set to 2/3 of the storing capacity as in Java and Python
        self.load_factor = 0.75
        self.number_of_contacts = 0

    def calculate_load_factor(self):
        return self.number_of_contacts/self.current_size

    def check_if_resize_needed(self):
        if self.calculate_load_factor() >= self.load_factor:
            self.phone_book_buckets.append([None]*self.initial_size)
            self.phone_book_data.append([None]*self.initial_size)
            self.current_size += self.current_size

    def hash_function(self, key):
        # remainder method
        unicode = 0
        position_index = 1
        for char in key:
            unicode += (ord(char) * position_index)
            position_index += 1
        return unicode % self.current_size

    def is_collision(self, hash_value):
        pass

    def rehash(self, old_hash, skip_value=1):
        new_hash = old_hash + skip_value
        if self.is_collision(new_hash):
            skip_value += 2
            self.rehash(new_hash, skip_value)
        return new_hash % self.current_size

    def insert(self, key, data):
        hash_value = self.hash_function(key)
        # if bucket is empty --> fill with new key
        # put data at same index in second array
        if self.phone_book_buckets[hash_value] == None:
            self.phone_book_buckets[hash_value] = key
            self.phone_book_data[hash_value] = data
        else:
            if self.phone_book_buckets[hash_value] == key:
                self.phone_book_data[hash_value] = data  # replace data if key is the same
            else:
                next_slot = self.rehash(hash_value)
                while self.phone_book_buckets[next_slot] != None and \
                        self.phone_book_buckets[next_slot] != key:
                    next_slot = self.rehash(next_slot)

                if self.phone_book_buckets[next_slot] == None:
                    self.phone_book_buckets[next_slot] = key
                    self.phone_book_data[next_slot] = data
                else:
                    self.phone_book_data[next_slot] = data  # replace


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

