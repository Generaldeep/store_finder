import unittest
from find_store import find_by_address, find_by_zip


class TestStringMethods(unittest.TestCase):

    def json_is_returned(self):
        print('ello')
        zip = '94132'
        units = 'mi'
        return_output = 'text'
        result = find_by_zip(zip, units, return_output)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
