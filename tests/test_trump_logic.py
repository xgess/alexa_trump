import unittest
from mock import Mock, patch

from alexa_trump import trump_logic


class TestTrumpLogic(unittest.TestCase):

    def test_starts_with_how(self):
        question = 'how do we do this'
        expected_response = 'I will build a great wall. and nobody builds walls better than me, believe me.'
        previous_logic_functions = trump_logic.trump_logic_functions
        trump_logic.trump_logic_functions = [trump_logic.how_question]

        actual_response = trump_logic.respond_to(question)
        trump_logic.trump_logic_functions = previous_logic_functions

        self.assertEqual(expected_response, actual_response)
