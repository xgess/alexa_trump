from response import Response
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

    def _calculate_answer(self):
        if self._answer is None:
            self._answer = TrumpQuestion(self.question).answer()

    def response(self):
        self._calculate_answer()
        return Response(
            speech_text=self._answer,
            reprompt_text=None,
            end_session=True,
            card_title="You asked Trump a question!",
            card_content=self.question + ' => ' + self._answer
        )
