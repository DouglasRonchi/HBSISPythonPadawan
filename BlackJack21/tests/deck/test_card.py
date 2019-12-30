import unittest
from unittest.mock import Mock

from app.deck.card import Card, Ace, Two, Three, Four, Five, Six, Eight, Nine, Ten, J, Q, K, Seven


class TestCards(unittest.TestCase):
    def test_card_should_be_a_instance_of_card(self):
        name = Mock()
        value = Mock()
        card = Card(name, value)
        self.assertIsInstance(card, Card)

    def test_card_should_receive_a_number_and_one_value(self):
        name = 'A'
        value = 1
        card = Card(name, value)
        self.assertEqual(card.name, name)
        self.assertEqual(card.value, value)

    def test_if_property_name_getter_really_works(self):
        name = Mock()
        value = Mock()
        card = Card(name, value)
        self.assertEqual(card.name, name)

    def test_if_property_name_setter_really_works(self):
        name = Mock()
        value = Mock()
        card = Card(name, value)
        new_name = Mock()
        card.name = new_name
        self.assertEqual(card.name, new_name)

    def test_if_property_value_getter_really_works(self):
        name = Mock()
        value = Mock()
        card = Card(name, value)
        self.assertEqual(card.value, value)

    def test_if_property_value_setter_really_works(self):
        name = Mock()
        value = Mock()
        card = Card(name, value)
        new_value = Mock()
        card.value = new_value
        self.assertEqual(card.value, new_value)

    def test_if_ace_is_a_really_ace(self):
        ace = Ace()
        self.assertEqual(ace.name, 'A')
        self.assertEqual(ace.value, 1)

    def test_if_two_is_a_really_two(self):
        two = Two()
        self.assertEqual(two.name, '2')
        self.assertEqual(two.value, 2)

    def test_if_three_is_a_really_three(self):
        three = Three()
        self.assertEqual(three.name, '3')
        self.assertEqual(three.value, 3)

    def test_if_four_is_a_really_four(self):
        four = Four()
        self.assertEqual(four.name, '4')
        self.assertEqual(four.value, 4)

    def test_if_five_is_a_really_five(self):
        five = Five()
        self.assertEqual(five.name, '5')
        self.assertEqual(five.value, 5)

    def test_if_six_is_a_really_six(self):
        six = Six()
        self.assertEqual(six.name, '6')
        self.assertEqual(six.value, 6)

    def test_if_seven_is_a_really_seven(self):
        seven = Seven()
        self.assertEqual(seven.name, '7')
        self.assertEqual(seven.value, 7)

    def test_if_eight_is_a_really_eight(self):
        eight = Eight()
        self.assertEqual(eight.name, '8')
        self.assertEqual(eight.value, 8)

    def test_if_nine_is_a_really_nine(self):
        nine = Nine()
        self.assertEqual(nine.name, '9')
        self.assertEqual(nine.value, 9)

    def test_if_ten_is_a_really_ten(self):
        ten = Ten()
        self.assertEqual(ten.name, '10')
        self.assertEqual(ten.value, 10)

    def test_if_j_is_a_really_j(self):
        j = J()
        self.assertEqual(j.name, 'J')
        self.assertEqual(j.value, 10)

    def test_if_q_is_a_really_q(self):
        q = Q()
        self.assertEqual(q.name, 'Q')
        self.assertEqual(q.value, 10)

    def test_if_k_is_a_really_k(self):
        k = K()
        self.assertEqual(k.name, 'K')
        self.assertEqual(k.value, 10)
