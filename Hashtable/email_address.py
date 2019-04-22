class Email:
    def __init__(self):
        self.email_addresses = []

    def get_emails(self):
        if len(self.email_addresses) > 0:
            emails = "E-mail addresses:\n" + "\n".join(self.email_addresses)
            return emails
        else:
            return ""

    def get_email(self, index=0):
        return self.email_addresses[index]

    def add_email(self, email):
        self.email_addresses.append(email)

    def modify_email(self, index, email):
        self.email_addresses[index] = email
