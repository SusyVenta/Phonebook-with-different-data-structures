from ..phonebook import PhoneBook


def test_get_size():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafridda")
    assert 1 == phonebook_object.get_size()
    phonebook_object.add_contact("Larry")
    assert 2 == phonebook_object.get_size()


def test_create_fullname():
    phonebook_object = PhoneBook()
    assert "Susanna Ventafridda" == phonebook_object.create_fullname("Susanna", "Ventafridda")
    assert "Susanna" == phonebook_object.create_fullname("Susanna", "")


def test_add_contact():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert "Susanna" == phonebook_object.find_contacts("Susanna").get_name()


def test_remove_contact():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert "Susanna" == phonebook_object.find_contacts("Susanna").get_name()
    phonebook_object.remove_contact("Susanna")
    assert False == phonebook_object.find_contacts("Susanna")


def test_contact_already_exists():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert "Susanna" == phonebook_object.find_contacts("Susanna").get_name()
    assert True == phonebook_object.contact_already_exists("Susanna")
    assert False == phonebook_object.contact_already_exists("Jane")


def test_edit_name():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna")
    assert "Susanna" == phonebook_object.find_contacts("Susanna").get_name()
    assert True == phonebook_object.edit_name("Susanna", "Susy")
    assert "Susy" == phonebook_object.find_contacts("Susy").get_name()


def test_edit_surname():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafri")
    assert "Susanna Ventafri" == phonebook_object.find_contacts("Susanna", "Ventafri").get_name_and_surname()
    assert True == phonebook_object.edit_surname("Susanna", "Ventafridda", "Ventafri")
    assert False == phonebook_object.find_contacts("Susanna", "Ventafri")
    assert "Susanna Ventafridda" == phonebook_object.find_contacts("Susanna", "Ventafridda").get_name_and_surname()
    assert "Contact already exists. Choose a different name" == phonebook_object.edit_surname("Susanna", "Ventafridda")


def test_find_contacts():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafri")
    phonebook_object.add_contact("Jeff", "Bezos")
    phonebook_object.add_contact("Larry", "Page")
    assert "Susanna Ventafri" == phonebook_object.find_contacts("Susanna", "Ventafri").get_name_and_surname()
    assert "Jeff Bezos" == phonebook_object.find_contacts("Jeff", "Bezos").get_name_and_surname()
    assert "Larry Page" == phonebook_object.find_contacts("Larry", "Page").get_name_and_surname()
    assert False == phonebook_object.find_contacts("Gates")


def test_print_all_contact_details():
    phonebook_object = PhoneBook()
    phonebook_object.add_contact("Susanna", "Ventafridda")
    phonebook_object.add_contact("Larry", "Page")
    phonebook_object.find_contacts("Larry", "Page").phone.add_phone("33333333")
    print(str(phonebook_object.print_all_contact_details()))
    assert "Susanna Ventafridda:\n\n\n\nLarry Page:\nMobile Phone: 33333333\n\n\n\n" == str(phonebook_object.print_all_contact_details())












