import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """ test Employee """

    def setUp(self):
        self.employee = Employee('Jack', 'Ma', 1)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 5001)

    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        self.assertEqual(self.employee.salary, 1001)


if __name__ == '__main__':
    unittest.main()
