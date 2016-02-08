from trump_question import TrumpQuestion


class AskTrumpResponder(object):
    '''Plucks off the user question from the request object,
       passes it along for answering, and formats a proper
       response for the Alexa service.
    '''

    def __init__(self, request):
        self.request = request
        self.question = self.request.question
        self._answer = None

    def response(self):
        return self._build_response()

    def _calculate_answer(self):
        if self._answer is None:
            self._answer = TrumpQuestion(self.question).answer()

    def _build_response(self):
        self._calculate_answer()
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": self._answer
                },
                "shouldEndSession": True,
                "card": {
                    "type": "Simple",
                    "title": "You asked Trump a question!",
                    "content": self.question + ' => ' + self._answer
                }
            }
        }
