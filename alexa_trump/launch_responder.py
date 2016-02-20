from response import Response

class LaunchResponder(object):
    SPEECH_TEXT = "To gain all the wisdom of the Donald, begin " \
           "by asking a single question. So, how can I help you?"
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
