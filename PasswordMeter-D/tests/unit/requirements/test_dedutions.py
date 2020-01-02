import unittest
from unittest.mock import Mock, patch

from app import Dedutions


class TestDedutions(unittest.TestCase):
    def test_dedutions_is_instance_of_dedutions_class(self):
        passwd = Mock()
        passwd.get_value.return_value = 'Maria'
        dedution = Dedutions(passwd)
        self.assertIsInstance(dedution, Dedutions)

    @patch('app.requirements.dedutions.print')
    def test_show_dedution_references(self, mock_print):
        passwd = Mock()
        passwd.get_value.return_value = 'Maria'
        dedution = Dedutions(passwd)
        dedution.show_dedution_references()

    def test_if_validate_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'Maria'
        dedution = Dedutions(passwd)
        result = dedution.validate()
        self.assertEqual(result, -11)

    def test_if_verify_letters_only_really_work_with_letters(self):
        passwd = Mock()
        passwd.get_value.return_value = 'AnhUi'
        dedution = Dedutions(passwd)
        result = dedution._verify_letters_only()
        self.assertEqual(result['count'], 5)
        self.assertEqual(result['value'], 5)

    def test_if_verify_letters_only_really_work_without_letters(self):
        passwd = Mock()
        passwd.get_value.return_value = '2598#$#'
        dedution = Dedutions(passwd)
        result = dedution._verify_letters_only()
        self.assertEqual(result['count'], 0)
        self.assertEqual(result['value'], 0)

    def test_if_verify_numbers_only_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = '35945'
        dedution = Dedutions(passwd)
        result = dedution._verify_numbers_only()
        self.assertEqual(result['count'], 5)
        self.assertEqual(result['value'], 5)

    def test_if_verify_consecutive_uppercase_letters_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'abcDEF'
        dedution = Dedutions(passwd)
        result = dedution._verify_consecutive_uppercase_letters()
        self.assertEqual(result['count'], 2)
        self.assertEqual(result['value'], 4)

    def test_if_verify_consecutive_lowercase_letters_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'abcDEF'
        dedution = Dedutions(passwd)
        result = dedution._verify_consecutive_lowercase_letters()
        self.assertEqual(result['count'], 2)
        self.assertEqual(result['value'], 4)

    def test_if_verify_consecutive_numbers_on_password_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'abc15555DEF'
        dedution = Dedutions(passwd)
        result = dedution._verify_consecutive_numbers_on_password()
        self.assertEqual(result['count'], 4)
        self.assertEqual(result['value'], 8)

    def test_if_verify_sequential_letters_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'abcdef15555'
        dedution = Dedutions(passwd)
        result = dedution._verify_sequential_letters()
        self.assertEqual(result['count'], 4)
        self.assertEqual(result['value'], 12)

    def test_if_verify_sequential_numbers_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'abc12345'
        dedution = Dedutions(passwd)
        result = dedution._verify_sequential_numbers()
        self.assertEqual(result['count'], 3)
        self.assertEqual(result['value'], 9)

    def test_if_verify_sequential_symbols_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'ab@#$%#55'
        dedution = Dedutions(passwd)
        result = dedution._verify_sequential_symbols()
        self.assertEqual(result['count'], 2)
        self.assertEqual(result['value'], 6)

    def test_if_verify_sequential_symbols_with_3_or_more_really_work(self):
        passwd = Mock()
        passwd.get_value.return_value = 'ab@@@@@@55'
        dedution = Dedutions(passwd)
        result = dedution._verify_sequential_symbols()
        self.assertEqual(result['count'], 3)
        self.assertEqual(result['value'], 9)
