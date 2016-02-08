import unittest
from mock import Mock, patch

from alexa_trump.trump_question import TrumpQuestion, how_question


class TestTrumpQuestion(unittest.TestCase):

    def test_starts_with_how(self):
        question = 'how do we do this'
        expected_response = 'I will build a great wall. and nobody builds walls better than me, believe me.'

        trump_question = TrumpQuestion(question)
        trump_question._logic_functions = [how_question]
        actual_response = trump_question.answer()

        self.assertEqual(expected_response, actual_response)
