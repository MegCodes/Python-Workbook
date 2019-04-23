class Addressee():

    def __init__(self, addressee, street, box, city, postal_code, country):
        self.addressee = addressee.title()
        self.street = street.title() + f', {str(box)}'
        self.city = city.title() + f', {str(postal_code)}'
        self.country = country.upper()

    def mailing_address(self):
        formatted_address = f"{self.addressee}\n{self.street}\n{self.city}\n{self.country}"
        return formatted_address