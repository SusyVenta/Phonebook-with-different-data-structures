class Address:
    def __init__(self, address="", address_type=""):
        self.addresses = {"Home": [], "Work": [], "Other": []}

    def get_address(self, address_type, index=""):
        if index != "":
            return "\n".join(self.addresses[address_type])
        else:
            return self.addresses[address_type][int(index)]

    def get_all_addresses(self):
        all_addresses = []
        for address_type, address_list in self.addresses.items():
            for address in address_list:
                all_addresses.append("{} Address: {}".format(address_type, address))
        return "\n".join(all_addresses)

    def add_address(self, address, address_type="Home"):
        self.addresses[address_type].append(address)

    def modify_address(self, address, address_type, index):
        self.addresses[address_type][index] = address