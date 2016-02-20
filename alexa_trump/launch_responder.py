class LaunchResponder(object):
    TEXT = "To gain all the wisdom of the Donald, begin " \
           "by asking a single question. So, how can I help you?"
    REPROMPT = "for example, try something like, what do you think of ben carson?"

    def response(self):
        return self._build_response()

    def _build_response(self):
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": self.TEXT
                },
                "reprompt": {
                    "outputSpeech": {
                        "type": 'PlainText',
                        "text": self.REPROMPT
                    }
                },
                "shouldEndSession": False,
                "card": {
                    "type": "Simple",
                    "title": "Ask Trump a question!",
                    "content": "There's just so much he can help you with."
                }
            }
        }
