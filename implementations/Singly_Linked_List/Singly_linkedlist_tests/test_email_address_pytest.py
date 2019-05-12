from ..email_address import Email


def test_get_emais():
    email_object = Email()
    expected_emails = ""
    assert expected_emails == email_object.get_emails()
    email_object.email_addresses = ["aa@amail.com", "bb@bmail.com", "cc@cmail.com"]
    expected_emails = "E-mail addresses:\naa@amail.com\nbb@bmail.com\ncc@cmail.com"
    assert expected_emails == email_object.get_emails()


def test_add_email():
    email_object = Email()
    assert "" == email_object.get_emails()
    email_object.add_email("aa@amail.com")
    assert "E-mail addresses:\naa@amail.com" == email_object.get_emails()


def test_modify_email():
    email_object = Email()
    email_object.email_addresses = ["aa@amail.com"]
    assert "aa@amail.com" == email_object.get_email(0)
    email_object.modify_email(0, "bb@bmail.com")
    assert "bb@bmail.com" == email_object.get_email(0)
