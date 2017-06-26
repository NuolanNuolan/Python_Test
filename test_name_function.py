import unittest
from name_function import *

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('yuan','haha','lianlin')
        self.assertAlmostEqual(formatted_name,'Yuan Haha Lianlin')
unittest.main()