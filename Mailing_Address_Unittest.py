import unittest
from Mailing_Address import Addressee

class mailing_address_test(unittest.TestCase):

    def test_mailing_address(self):
        test_data= Addressee('john doe', 'baltimor street', 43, 'san francisco', 5678, 'usa')
        mailing_address_result = 'John Doe\nBaltimor Street, 43\nSan Francisco, 5678\nUSA'
        self.assertEqual(test_data.mailing_address(), mailing_address_result)


unittest.main()

