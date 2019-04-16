from ..phone import Phone


def test_get_phone():
    phone_object = Phone()
    phone_object.phones = {"Mobile": ["+00 000 000"], "Home": ["+11 111", "+22 222 222"], "Work": []}
    assert ["+00 000 000"] == phone_object.get_phone("Mobile")
    assert [] == phone_object.get_phone("Work")


def test_get_all_phones():
    phone_object = Phone()
    phone_object.phones = {"Mobile": ["+00 000 000"], "Home": ["+11 111", "+22 222 222"], "Work": []}
    expected_phones = "Mobile Phone: +00 000 000\nHome Phone: +11 111\nHome Phone: +22 222 222\n"
    assert expected_phones == phone_object.get_all_phones()


def test_add_phone():
    phone_object = Phone()
    assert "" == phone_object.get_all_phones()
    phone_object.add_phone("+44 4444444", "Mobile")
    assert ["+44 4444444"] == phone_object.get_phone("Mobile")


def test_has_only_one_phone():
    phone_object = Phone()
    phone_object.phones = {"Mobile": ["+00 000 000"], "Home": ["+11 111", "+22 222 222"], "Work": []}
    assert True == phone_object.has_only_one_phone(phone_object.phones["Mobile"])
    assert False == phone_object.has_only_one_phone(phone_object.phones["Home"])


def test_modify_phone():
    phone_object = Phone()
    phone_object.phones = {"Mobile": ["+00 000 000"], "Home": ["+11 111", "+22 222 222"], "Work": []}
    phone_object.modify_phone("44444", "Mobile")
    assert ["44444"] == phone_object.get_phone("Mobile")
