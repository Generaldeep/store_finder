
import unittest
from find_store_testing_file import find_by_zip, find_by_address


class FindByZipTest(unittest.TestCase):
    def test_zip_json(self):
        result = find_by_zip('95670', 'mi', 'json')
        valid_find = """{"dist": 0.8685548151643981, "key": 1619, "Address": "10881 Olson Dr"}"""
        self.assertEqual(result, valid_find)

    def test_zip_text(self):
        result = find_by_zip('95670', 'mi', 'text')
        valid_find = {'dist': 0.8685548151643981,
                      'key': 1619, 'Address': '10881 Olson Dr'}
        self.assertEqual(result, valid_find)

    def test_zip_unit_mi(self):
        result = find_by_zip('95670', 'mi', 'text')
        valid_find = {'dist': 0.8685548151643981,
                      'key': 1619, 'Address': '10881 Olson Dr'}
        self.assertEqual(result, valid_find)

    def test_zip_unit_km(self):
        result = find_by_zip('95670', 'km', 'text')
        valid_find = {'dist': 1.397803480989827,
                      'key': 1619, 'Address': '10881 Olson Dr'}
        self.assertEqual(result, valid_find)


class FindByAddress(unittest.TestCase):
    def test_address_json(self):
        result = find_by_address('1122 14th, oakland', 'mi', 'json')
        valid_find = """{"dist": 1.6862598515806686, "key": 1758, "Address": "2700 Fifth Street"}"""
        self.assertEqual(result, valid_find)

    def test_address_text(self):
        result = find_by_address('1122 14th, oakland', 'mi', 'text')
        valid_find = {'dist': 1.6862598515806686,
                      'key': 1758, 'Address': '2700 Fifth Street'}
        self.assertEqual(result, valid_find)

    def test_address_unit_mi(self):
        result = find_by_address('1122 14th, oakland', 'mi', 'json')
        valid_find = """{"dist": 1.6862598515806686, "key": 1758, "Address": "2700 Fifth Street"}"""
        self.assertEqual(result, valid_find)

    def test_address_unit_km(self):
        result = find_by_address('1122 14th, oakland', 'km', 'json')
        valid_find = """{"dist": 2.7137721756187703, "key": 1758, "Address": "2700 Fifth Street"}"""
        self.assertEqual(result, valid_find)


if __name__ == "__main__":
    unittest.main()
