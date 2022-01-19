import unittest
from unittest.mock import patch
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    '''
    Object for testing the Employee class.
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Special method which runs before all test methods. Unlike setUp class it is ran only once.
        '''
        print('setupClass')

    @classmethod
    def tearDownClass(cls):

        '''
        Special method which runs after all test methods. Used for cleanup.
        '''
        print('teardownClass')

    def setUp(self):
        '''
        Special method which runs before each test methods. Similar to __init__ method.
        '''
        print('setUp')
        self.emp_1 = Employee('Ngo', 'Cuong', 50000)
        self.emp_2 = Employee('Mike', 'Ross', 60000)

    def tearDown(self):
        '''
        Special method which runs after each test.
        '''
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Ngo.Cuong@email.com')
        self.assertEqual(self.emp_2.email, 'Mike.Ross@email.com')

        self.emp_1.first = 'Do'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Do.Cuong@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Ross@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Ngo Cuong')
        self.assertEqual(self.emp_2.fullname, 'Mike Ross')

        self.emp_1.first = 'Do'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Do Cuong')
        self.assertEqual(self.emp_2.fullname, 'Jane Ross')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        '''
        Tests only if our code is correct, not if the website is down.
        ''' 
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Cuong/May') # check method was called with correct url
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Ross/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()