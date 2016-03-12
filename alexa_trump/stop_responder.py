from response import Response

class StopResponder(object):
    END_SESSION = True

    def response(self):
        return Response(
            speech_text="",
            end_session=self.END_SESSION,
        )
