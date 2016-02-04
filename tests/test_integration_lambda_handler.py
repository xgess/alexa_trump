import unittest
from mock import Mock, ANY

import test_helper
from alexa_trump.lambda_handler import lambda_handler


class TestIntegrationLambdaHandler(unittest.TestCase):

    LAMBDA_CONTEXT = Mock()

    QUESTION = "do you think Hillary will win the democratic nomination?"
    ANSWER = 'i wrote a book about this. the art of the deal.'
    EXPECTED_TRUMP_RESPONSE = test_helper.build_response_dict(QUESTION, ANSWER)
    EXPECTED_TRUMP_RESPONSE['response']['outputSpeech']['text'] = ANY
    EXPECTED_TRUMP_RESPONSE['response']['card']['content'] = ANY

    EXPECTED_HELP_RESPONSE = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "To gain all the wisdom of the Donald, begin by asking a single question."
            },
            "shouldEndSession": True,
            "card": {
                "type": "Simple",
                "title": "Ask Trump a question!",
                "content": "There's just so much he can help you with."
            }
        }
    }

    def test_request_response_question(self):
        event_dict = test_helper.build_request_dict(self.QUESTION)
        alexa_response = lambda_handler(event=event_dict, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_TRUMP_RESPONSE)

    def test_request_response_help(self):
        event_dict = test_helper.build_launch_request_dict()
        alexa_response = lambda_handler(event=event_dict, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_HELP_RESPONSE)
