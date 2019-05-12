from ..contact import Contact


def test_get_all_contact_details():
    contact_object = Contact("Susanna")
    expected_contacts = "Contact details of Susanna : \n\n\n"
    assert expected_contacts == contact_object.get_all_contact_details()
    contact_object.phone.add_phone("333 333")
    expected_contacts = "Contact details of Susanna : \nMobile Phone: 333 333\n\n\n"
    assert expected_contacts == contact_object.get_all_contact_details()


def test_get_name_and_surname():
    contact_object = Contact("Susanna")
    assert "Susanna" == contact_object.get_name_and_surname()
    contact_object = Contact("Susanna", "Ventafridda")
    assert "Susanna Ventafridda" == contact_object.get_name_and_surname()


def test_set_surname():
    contact_object = Contact("Susanna")
    assert "Susanna" == contact_object.get_name_and_surname()
    contact_object.set_surname("Ventafridda")
    assert "Susanna Ventafridda" == contact_object.get_name_and_surname()


def test_edit_name():
    contact_object = Contact("Susanna")
    assert "Susanna" == contact_object.get_name_and_surname()
    contact_object.edit_name("Susy")
    assert "Susy" == contact_object.get_name_and_surname()


def test_edit_surname():
    contact_object = Contact("Susanna", "Venta")
    assert "Susanna Venta" == contact_object.get_name_and_surname()
    contact_object.edit_surname("Ventafridda")
    assert "Susanna Ventafridda" == contact_object.get_name_and_surname()