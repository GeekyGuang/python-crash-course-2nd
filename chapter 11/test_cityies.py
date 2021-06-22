import unittest
from city_function import city_info


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """test two parameters"""
        info = city_info('santiago', 'chile')
        self.assertEqual(info, 'Santiago, Chile')

    def test_city_population(self):
        """test three parameters"""
        info = city_info('santiago', 'chile', 5000000)
        self.assertEqual(info, 'Santiago, Chile - Population 5000000')


if __name__ == '__main__':
    unittest.main()
