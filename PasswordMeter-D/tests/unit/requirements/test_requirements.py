import unittest
from unittest.mock import Mock, patch

from app.requirements.requirements import Requirements


class TestRequirements(unittest.TestCase):
    def test_if_requirement_is_instance_of_requirements_class(self):
        passwd = Mock()
        requirements = Requirements(passwd)
        self.assertIsInstance(requirements, Requirements)

    def test_if_password_argument_appropriately_work(self):
        passwd = Mock()
        requirements = Requirements(passwd)
        self.assertEqual(requirements._password, passwd)

    def test_if_get_score_returns_score_property(self):
        passwd = Mock()
        requirements = Requirements(passwd)
        result = requirements.get_score_validated()
        self.assertEqual(result, requirements._score)

    @patch('app.requirements.requirements.print')
    def test_show_score_total_points_should_print_somethings(self, mock_print):
        passwd = Mock()
        requirements = Requirements(passwd)
        requirements.show_score_total_points()

    @patch('app.requirements.requirements.print')
    def test_when_rate_is_greater_then_100_points(self, mock_print):
        passwd = Mock()
        requirements = Requirements(passwd)
        requirements._score = 101
        requirements.show_score_total_points()
