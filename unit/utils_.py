import unittest
from core.utils.utility import Utils

dir_ = "C:/Users/Milton Savarimuthu/"


class MyTests(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = Utils(4)

    def test_directory_exist(self):
        self.assertTrue(self.obj.is_directory_exist("C:"))

    # def tearDown(self) -> None:
    #     self.obj = None

