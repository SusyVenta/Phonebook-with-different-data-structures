from .phonebook import PhoneBook
import csv
import time


def add_all_contact_info(linkedlist):
    with open("/home/susy/Scrivania/git_repo_Phonebook_implementations/Phonebook-with-different-data-structures"
              "/Singly_Linked_List/00_contacts.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # skip headers
                line_count += 1
            else:
                # add name and surname, cols 1, 2
                linkedlist.add_contact(row[0], row[1])
                # add address, col 3
                linkedlist.find_contacts(row[0], row[1]).address.add_address(row[3])
                # add phones, cols 8, 9
                linkedlist.find_contacts(row[0], row[1]).address.add_phone(row[8])
                linkedlist.find_contacts(row[0], row[1]).address.add_phone(row[9], "Home")
                # add email, col 10
                linkedlist.find_contacts(row[0], row[1]).address.add_email(row[10])
                # go to next line
                line_count += 1


start = time.time()
new_linkedList = PhoneBook()
add_all_contact_info(new_linkedList)
end = time.time()
print("Execution time: {}".format(end-start))

