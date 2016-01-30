import unittest
from mock import Mock

from lambda_handler import lambda_handler


class TestIntegrationLambdaHandler(unittest.TestCase):
    USER_QUESTION = "do you think Hillary will win the democratic nomination"
    EXPECTED_ANSWER = "that sounds YOUDJ."

    EVENT_REQUEST_JSON = {
        "session": {
            "sessionId": "SessionId.11111111-9999-4444-aaaa-888888888888",
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.ffffffff-1111-4444-bbbb-888888888888"
            },
            "user": {
                "userId": "amzn1.echo-sdk-account.AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            },
            "new": True
        },
        "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.99999999-1111-4444-bbbb-888888888888",
            "timestamp": "2016-01-30T19:36:25Z",
            "intent": {
                "name": "AskTrumpIntent",
                "slots": {
                    "question": {
                        "name": "question",
                        "value": USER_QUESTION
                    }
                }
            }
        }
    }
    CONTEXT = Mock()

    EXPECTED_RESPONSE = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": EXPECTED_ANSWER
            },
            "shouldEndSession": True,
            "card": {
                "type": "Simple",
                "title": "Ask Trump: " + USER_QUESTION,
                "content": "Trump Says: " + EXPECTED_ANSWER
            }
        }
    }

    def test_request_response(self):
        alexa_response = lambda_handler(event=self.EVENT_REQUEST_JSON, context=self.CONTEXT)

        self.assertEqual(alexa_response, self.EXPECTED_RESPONSE)
