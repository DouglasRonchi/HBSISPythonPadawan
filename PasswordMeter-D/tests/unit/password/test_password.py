import unittest

from app.password.password import Password


class TestPassword(unittest.TestCase):
    def test_if_password_is_a_instance_of_password(self):
        password = Password('ABC')
        self.assertIsInstance(password, Password)

    def test_if_get_value_return_self_password(self):
        password = Password('ABC')
        result = password.get_value()
        self.assertEqual(result, 'ABC')

