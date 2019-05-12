from .phonebook import PhoneBook
import csv
import time


def add_all_contact_info(hashmap):
    with open("/home/susy/Scrivania/git_repo_Phonebook_implementations/Phonebook-with-different-data-structures"
              "/Singly_Linked_List/LinkedList_Resources/100_contacts.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip headers
                line_count += 1
            else:
                # add name and surname, cols 1, 2
                hashmap.add_contact(row[0], row[1])
                # add address, col 3
                hashmap.find_contacts(row[0], row[1]).address.add_address(row[3])
                # add phones, cols 8, 9
                hashmap.find_contacts(row[0], row[1]).address.add_phone(row[8])
                hashmap.find_contacts(row[0], row[1]).address.add_phone(row[9], "Home")
                # add email, col 10
                hashmap.find_contacts(row[0], row[1]).address.add_email(row[10])
                # go to next line
                line_count += 1


start = time.time()
new_hashmap = PhoneBook()
add_all_contact_info(new_hashmap)
end = time.time()
print("Execution time: {}".format(end-start))
