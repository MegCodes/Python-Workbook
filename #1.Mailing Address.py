class Addressee():

    def __init__(self, addressee, street, box, city, postal_code, country):
        self.addressee = addressee.title()
        self.street = street.title()
        self.box = str(box)
        self.city = city.title()
        self.postal_code = str(postal_code)
        self.country = country.upper()

    def mailing_address(self):
        formatted_address = self.addressee, self.street, self.box, self.city, self.postal_code, self.country
        for element in formatted_address:
            print(element)


