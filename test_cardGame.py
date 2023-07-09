from unittest import TestCase

from cardGame import find_card_order


class Test(TestCase):
    def test_find_card_order(self):
        result = find_card_order('2-Heart', '3-Spade')
        expected = 'lower'
        self.assertEqual(expected, result)
    def test_alphabet_number(self):
        result = find_card_order('K-Dia','Q-Heart')
        expected = 'higher'
        self.assertEqual(expected, result)