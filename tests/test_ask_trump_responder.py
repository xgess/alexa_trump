import unittest
from mock import patch

import test_helper
from alexa_trump.ask_trump_responder import AskTrumpResponder
from alexa_trump.trump_question import TrumpQuestion


class TestAskTrumpResponder(unittest.TestCase):
    QUESTION = "what do you think of Ted Cruz?"
    INJECTED_ANSWER = "he is a loser."

    @patch.object(TrumpQuestion, 'answer')
    def test_properly_formatted_response(self, mock_trump_response):
        mock_trump_response.return_value = self.INJECTED_ANSWER
        request = test_helper.ask_trump_request(self.QUESTION)
        expected_response = test_helper.ask_trump_response_dict(self.QUESTION, self.INJECTED_ANSWER)

        actual_response = AskTrumpResponder(request).response()

        self.assertEqual(expected_response, actual_response)
