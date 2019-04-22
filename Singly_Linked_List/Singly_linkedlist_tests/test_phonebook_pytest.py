from ..phonebook import PhoneBook


def test_create_fullname():
    phonebook_object = PhoneBook()
    assert "Susanna Ventafridda" == phonebook_object.create_fullname("Susanna", "Ventafridda")
    assert "Susanna" == phonebook_object.create_fullname("Susanna", "")


def test_add_contact():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")


def test_remove_contact():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert ["Susanna"] == phonebook_object.find_contacts("Susanna")
    phonebook_object.remove_contact("Susanna")
    assert False == phonebook_object.find_contacts("Susanna")


def test_contact_already_exists():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert ["Susanna"] == phonebook_object.find_contacts("Susanna")
    assert True == phonebook_object.contact_already_exists("Susanna")
    assert False == phonebook_object.contact_already_exists("Jane")


def test_edit_name():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert ["Susanna"] == phonebook_object.find_contacts("Susanna")
    assert True == phonebook_object.edit_name("Susanna", "Susy")
    assert ["Susy"] == phonebook_object.find_contacts("Susy")


def test_edit_surname():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafri")
    assert ["Susanna Ventafri"] == phonebook_object.find_contacts("Susanna")
    assert True == phonebook_object.edit_surname("Susanna", "Ventafridda", "Ventafri")
    assert ["Susanna Ventafridda"] == phonebook_object.find_contacts("Ventafridda")
    assert "Contact already exists. Choose a different name" == phonebook_object.edit_surname("Susanna", "Ventafridda")


def test_find_contacts():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafri")
    phonebook_object.add_contact("Jeff", "Bezos")
    phonebook_object.add_contact("Larry", "Page")
    assert ["Susanna Ventafri"] == phonebook_object.find_contacts("Susanna")
    assert ["Jeff Bezos"] == phonebook_object.find_contacts("Jeff")
    assert ["Larry Page"] == phonebook_object.find_contacts("Page")
    assert ["Larry Page"] == phonebook_object.find_contacts("Larry", "Page")
    assert False == phonebook_object.find_contacts("Gates")
    phonebook_object.add_contact("Susanna", "Ventafridda")
    assert ["Susanna Ventafridda", "Susanna Ventafri"] == phonebook_object.find_contacts("Susanna")


def test_print_all_contact_details():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafridda")
    phonebook_object.add_contact("Larry", "Page")
    print (phonebook_object.print_all_contact_details())
    assert """Contact details of Larry Page: \n\n\nContact details of Susanna Ventafridda: \n\n\n""" == str(phonebook_object.print_all_contact_details())












