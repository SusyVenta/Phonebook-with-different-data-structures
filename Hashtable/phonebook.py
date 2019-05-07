from .contact import Contact


# class PhoneBook == HashTable
# collision resolution technique: quadratic probing
class PhoneBook:
    def __init__(self):
        # initial capacity set to 16 as in Java HashMap
        self.initial_size = 16
        self.current_size = 16
        # self.phone_book_buckets contains the keys
        self.phone_book_buckets = [None]*self.initial_size
        # self.phone_book_data contains the keys
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

    def is_collision(self, hash_value, key):
        return self.phone_book_buckets[hash_value] != None and self.phone_book_buckets[hash_value] != key

    def is_bucket_empty(self, hash_value):
        return self.phone_book_buckets[hash_value] == None

    def write_key_and_data(self, hash_value, key, data):
        self.phone_book_buckets[hash_value] = key
        self.phone_book_data[hash_value] = data

    def if_empty_bucket_write_key_and_data(self, hash_value, key, data):
        # if bucket is empty --> fill with new key
        # put data at same index in second array
        if self.is_bucket_empty(hash_value):
            self.write_key_and_data(hash_value, key, data)
            return True
        return False

    def replace_data_if_key_is_the_same(self, hash_value, key, data):
        if self.phone_book_buckets[hash_value] == key:
            self.phone_book_data[hash_value] = data
            return True
        return False

    def rehash_until_no_collision_found(self, hash_value, key, skip_value=1):
        next_slot = self.rehash(hash_value, skip_value)
        if self.is_collision(next_slot, key):
            skip_value += 2
            self.rehash_until_no_collision_found(next_slot, key, skip_value)
        return next_slot

    def rehash(self, old_hash, skip_value=1):
        # quadratic probing: uses a skip consisting of successive perfect squares
        new_hash = (old_hash + skip_value) % self.current_size
        return new_hash

    def add_contact(self, key, data):
        hash_value = self.hash_function(key)
        if not self.if_empty_bucket_write_key_and_data(hash_value, key, data):
            if not self.replace_data_if_key_is_the_same(hash_value, key, data):
                free_slot = self.rehash_until_no_collision_found(hash_value, key)
                if not self.if_empty_bucket_write_key_and_data(free_slot, key, data):
                    self.replace_data_if_key_is_the_same(free_slot, key, data)

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

