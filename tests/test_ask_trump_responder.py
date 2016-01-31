import unittest
from mock import Mock

import test_helper
from alexa_trump.ask_trump_responder import AskTrumpResponder


class TestAskTrumpResponder(unittest.TestCase):
    QUESTION = "what do you think of Ted Cruz?"
    INJECTED_ANSWER = "he is a loser."

    def test_properly_formatted_response(self):
        request = test_helper.build_request(self.QUESTION)
        expected_response = test_helper.build_response_dict(self.QUESTION, self.INJECTED_ANSWER)

        trump = AskTrumpResponder(request)
        trump._answer = self.INJECTED_ANSWER
        actual_response = trump.response()

        self.assertEqual(expected_response, actual_response)
