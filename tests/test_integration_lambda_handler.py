import unittest
from mock import Mock, ANY

import test_helper
from alexa_trump.lambda_handler import lambda_handler


class TestIntegrationLambdaHandler(unittest.TestCase):

    LAMBDA_CONTEXT = Mock()

    QUESTION = "do you think Hillary will win the democratic nomination?"
    ANSWER = 'i wrote a book about this. the art of the deal.'
    EXPECTED_TRUMP_RESPONSE = test_helper.ask_trump_response_dict(QUESTION, ANSWER)
    EXPECTED_TRUMP_RESPONSE['response']['outputSpeech']['text'] = ANY
    EXPECTED_TRUMP_RESPONSE['response']['card']['content'] = ANY

    EXPECTED_HELP_RESPONSE = test_helper.help_response_dict()
    EXPECTED_LAUNCH_RESPONSE = test_helper.launch_response_dict()

    def test_ask_trump_request_response(self):
        event_dict = test_helper.ask_trump_request_dict(self.QUESTION)
        alexa_response = lambda_handler(event=event_dict, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_TRUMP_RESPONSE)

    def test_help_request_response(self):
        event_dict = test_helper.help_request_dict()
        alexa_response = lambda_handler(event=event_dict, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_HELP_RESPONSE)

    def test_launch_request_response(self):
        event_dict = test_helper.launch_request_dict()
        alexa_response = lambda_handler(event=event_dict, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_LAUNCH_RESPONSE)
