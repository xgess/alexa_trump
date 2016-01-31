import unittest
from mock import Mock

import test_helper
from alexa_trump.lambda_handler import lambda_handler


class TestIntegrationLambdaHandler(unittest.TestCase):

    QUESTION = "do you think Hillary will win the democratic nomination?"
    ANSWER = "that sounds YOUDJ."

    EVENT_REQUEST_DICT = test_helper.build_request_dict(QUESTION)
    EXPECTED_RESPONSE_DICT = test_helper.build_response_dict(QUESTION, ANSWER)

    LAMBDA_CONTEXT = Mock()

    def test_request_response(self):
        alexa_response = lambda_handler(event=self.EVENT_REQUEST_DICT, context=self.LAMBDA_CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_RESPONSE_DICT)
