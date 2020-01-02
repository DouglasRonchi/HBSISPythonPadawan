import unittest
from unittest.mock import Mock, patch, MagicMock

from app import Password
from app.requirements.additions import Additions


class TestAdditions(unittest.TestCase):
    def test_if_additions_is_a_instance_of_additions_class(self):
        passwd = Mock()
        additions = Additions(passwd)
        self.assertIsInstance(additions, Additions)

    @patch('app.requirements.additions.print')
    def test_if_show_addition_references_really_work(self, mock_print):
        passwd = Mock()
        passwd.get_value.return_value = 'Douglas'
        additions = Additions(passwd)
        additions.show_addition_references()

    def test_if_validate_really_work_and_return_score_in_the_end(self):
        passwd = Mock()
        passwd.get_value.return_value = 'Dn1234!#$'
        additions = Additions(passwd)
        score = additions.validate()
        self.assertEqual(score, 110)

    def test_if_validate_really_work_with_return_uppercase_letters(self):
        passwd = Mock()
        passwd.get_value.return_value = 'D1234!#$'
        additions = Additions(passwd)
        score = additions.validate()
        self.assertEqual(score, 80)

    def test_if_validate_really_work_with_return_lowercase_letters(self):
        passwd = Mock()
        passwd.get_value.return_value = 'er1234!#$'
        additions = Additions(passwd)
        score = additions.validate()
        self.assertEqual(score, 84)

    def test_if_verify_numbers_of_characters_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = '123456'
        additions = Additions(passwd)
        result = additions._verify_numbers_of_characters()
        self.assertEqual(result['count'], 6)
        self.assertEqual(result['value'], 24)

    def test_if_verify_uppercase_letters_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = 'AAabcAA'
        additions = Additions(passwd)
        result = additions._verify_uppercase_letters()
        self.assertEqual(result['count'], 4)
        self.assertEqual(result['value'], 6)

    def test_if_verify_lowercase_letters_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = 'AAabcAA'
        additions = Additions(passwd)
        result = additions._verify_lowercase_letters()
        self.assertEqual(result['count'], 3)
        self.assertEqual(result['value'], 8)

    def test_if_verify_numbers_on_password_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = 'AA123AA'
        additions = Additions(passwd)
        result = additions._verify_numbers_on_password()
        self.assertEqual(result['count'], 3)
        self.assertEqual(result['value'], 12)

    def test_if_verify_symbols_on_password_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = 'AA#$@AA'
        additions = Additions(passwd)
        result = additions._verify_symbols_on_password()
        self.assertEqual(result['count'], 3)
        self.assertEqual(result['value'], 18)

    def test_if_verify_middle_numbers_and_symbols_is_working(self):
        passwd = Mock()
        passwd.get_value.return_value = 'A32A#$@A22A'
        additions = Additions(passwd)
        result = additions._verify_middle_numbers_and_symbols()
        self.assertEqual(result['count'], 7)
        self.assertEqual(result['value'], 14)
