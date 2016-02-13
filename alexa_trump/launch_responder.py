class LaunchResponder(object):
    TEXT = "To gain all the wisdom of the Donald, begin " \
           "by asking a single question. So, how can I help you?"

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
                "shouldEndSession": False,
                "card": {
                    "type": "Simple",
                    "title": "Ask Trump a question!",
                    "content": "There's just so much he can help you with."
                }
            }
        }
