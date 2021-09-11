import unittest
from core.utils.utility import Utils

dir_ = "C:/Users/Milton Savarimuthu/"


class MyTests(unittest.TestCase):
    data = 4

    def setUp(self) -> None:
        self.obj = Utils(MyTests.data)

    def test_directory_exist(self):
        self.assertTrue(self.obj.is_directory_exist(dir_))

    def test_not_a_directory(self):
        self.assertFalse(self.obj.is_directory_exist("/home"))

    def test_reverse_string(self):
        string = "Hello World!"
        rev = self.obj.reverse_string(string)
        expected = string[::-1]
        self.assertEqual(rev, expected)

    def test_catch_signal(self):
        sig = 5
        signals = self.obj.catch_signal(sig)
        print(signals)
        if len(signals) > 10 and len(signals) == 0:
            return False
        elif len(signals) == 10:
            self.assertNotIn(sig, signals)
        elif len(signals) < 10:
            self.assertIn(sig, signals)

    def test_property_data1(self):
        self.assertEqual(self.obj.data1, MyTests.data)