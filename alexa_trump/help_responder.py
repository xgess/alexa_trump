class HelpResponder(object):
    TEXT = "Just ask Alexa to Ask Trump your question. " \
            "Think of it like a magic 8 ball, but helpful. " \
            "So, what burning question do you have for donald? "\
            "Ask it right now."
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
