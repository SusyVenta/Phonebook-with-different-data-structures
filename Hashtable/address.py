class Address:
    def __init__(self):
        self.addresses = {"Home": [], "Work": [], "Other": []}

    def get_address(self, address_type="Home", index=0):
        out_address = self.addresses[address_type][index]
        return out_address

    def get_all_addresses(self):
        all_addresses = []
        for address_type, address_list in self.addresses.items():
            for address in address_list:
                all_addresses.append("{} Address: {}\n".format(address_type, address))
        return "".join(all_addresses)

    def add_address(self, address, address_type="Home"):
        self.addresses[address_type].append(address)

    def modify_address(self, address, address_type="Home", index=0):
        self.addresses[address_type][index] = address