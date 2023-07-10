from unittest import TestCase

from functions import scoring, find_card_order


class Test(TestCase):
    def test_find_card_order(self):
        result = find_card_order('2-Heart', '3-Spade')
        expected = 'lower'
        self.assertEqual(expected, result)

    def test_alphabet_number(self):
        result = find_card_order('K-Dia', 'Q-Heart')
        expected = 'higher'
        self.assertEqual(expected, result)


class Test(TestCase):
    def test_scoring(self):
        my_score, co_score = scoring('higher', 0, 0)
        self.assertEqual(1, my_score)
        self.assertEqual(0, co_score)

    def test_scoring_twice(self):
        my_score, co_score = scoring('higher', 0, 0)
        my_score, co_score = scoring('lower', 1, 0)
        self.assertEqual(1, my_score)
        self.assertEqual(1, co_score)
