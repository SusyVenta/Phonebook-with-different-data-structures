from Common_elements.address import Address
from unittest import TestCase


class TestAddress(TestCase):
    def test_get_address(self):
        address_object = Address()
        address_object.addresses = {"Home": ["7 rue JS, Luxembourg"], "Work": ["via Resegone, Carnate"], "Other":
            ["10, rue de la Gare, Luxembourg", "8, av. Liberté, Luxembourg"]}
        expected_address = "7 rue JS, Luxembourg"
        assert expected_address == address_object.get_address()
        assert "7 rue JS, Luxembourg" == address_object.get_address("Home")
        assert "via Resegone, Carnate" == address_object.get_address("Work")
        assert "8, av. Liberté, Luxembourg" == address_object.get_address("Other", 1)

    def test_get_all_addresses(self):
        address_object = Address()
        address_object.addresses = {"Home": [], "Work": [], "Other":
            ["10, rue de la Gare, Luxembourg", "8, av. Liberté, Luxembourg"]}
        assert "Other Address: 10, rue de la Gare, Luxembourg\nOther Address: 8, av. Liberté, Luxembourg\n" == address_object.get_all_addresses()
        address_object.addresses = {"Home": [], "Work": [], "Other": []}
        assert "" == address_object.get_all_addresses()

    def test_add_address(self):
        address_object = Address()
        address_object.addresses = {"Home": ["7 rue JS, Luxembourg"], "Work": ["via Resegone, Carnate"], "Other":
            ["10, rue de la Gare, Luxembourg", "8, av. Liberté, Luxembourg"]}
        address_object.add_address("test added address with no address type")
        assert address_object.addresses["Home"] == ["7 rue JS, Luxembourg", "test added address with no address type"]
        address_object.add_address("new Work Address", "Work")
        assert address_object.addresses["Work"] == ["via Resegone, Carnate", "new Work Address"]

    def test_modify_addresses(self):
        address_object = Address()
        address_object.addresses = {"Home": ["7 rue JS, Luxembourg"], "Work": ["via Resegone, Carnate"], "Other":
            ["10, rue de la Gare, Luxembourg", "8, av. Liberté, Luxembourg"]}
        address_object.modify_address("new address replacing home")
        assert address_object.addresses["Home"] == ["new address replacing home"]
        address_object.addresses = {"Home": ["7 rue JS, Luxembourg"], "Work": ["via Resegone, Carnate"], "Other":
            ["10, rue de la Gare, Luxembourg", "8, av. Liberté, Luxembourg"]}
        address_object.modify_address("new Other Address index 1", "Other", 1)
        assert address_object.addresses["Other"][1] == "new Other Address index 1"
