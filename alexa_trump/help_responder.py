from response import Response

class HelpResponder(object):
    SPEECH_TEXT = "Just ask Alexa to Ask Trump your question. " \
            "Think of it like a magic 8 ball, but helpful. " \
            "So, what burning question do you have for donald? "\
            "Ask it right now."
    REPROMPT = "for example, try something like, what do you think of ben carson?"
    CARD_TITLE = "Ask Trump a question!"
    CARD_CONTENT = "There's just so much he can help you with."
    END_SESSION = False

    def response(self):
        return Response(
            speech_text=self.SPEECH_TEXT,
            reprompt_text=self.REPROMPT,
            end_session=self.END_SESSION,
            card_title=self.CARD_TITLE,
            card_content=self.CARD_CONTENT
        )
