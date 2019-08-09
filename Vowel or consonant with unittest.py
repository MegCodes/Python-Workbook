#draft
vowels = ['a','e','i','o','u']

def checker():
    letter = input('Please enter a letter you want to check: ')
    if letter in vowels:
        print("'{}' is a vowel.".format(letter))
    elif letter == 'y':
        print(" 'y' is sometimes a vowel and sometimes a consonant")
    else:
        print("'{}' is a consonant.".format(letter))

#unittest
import unittest

vowels = ['a','e','i','o','u']

def checker(letter):
    if letter in vowels:
        return "'{}' is a vowel.".format(letter)
    elif letter == 'y':
        return "'y' is sometimes a vowel and sometimes a consonant."
    else:
        return "'{}' is a consonant.".format(letter)


class testchecker(unittest.TestCase):
    def setUp(self):
        self.check1 = checker('o')
        self.check2 = checker('y')
        self.check3 = checker('x')

    def test1(self):
        self.assertEqual(self.check1, "'o' is a vowel.")

    def test2(self):
        self.assertEqual(self.check2, "'y' is sometimes a vowel and sometimes a consonant.")

    def test3(self):
        self.assertEqual(self.check3, "'x' is a consonant.")

unittest.main()

#v2
import unittest

vowels = ['a','e','i','o','u']

def checker(letter):
    if letter in vowels:
        return "'{}' is a vowel.".format(letter)
    elif letter == 'y':
        return "'y' is sometimes a vowel and sometimes a consonant."
    else:
        return "'{}' is a consonant.".format(letter)


class testchecker(unittest.TestCase):
    def setUp(self):
        self.check1 = checker('o')
        self.check2 = checker('y')
        self.check3 = checker('x')

    def test1(self):
        self.assertTrue(self.check1, vowels)

    def test2(self):
        self.assertEqual(self.check2, "'y' is sometimes a vowel and sometimes a consonant.")

    def test3(self):
        self.assertTrue(self.check3, vowels)

unittest.main()