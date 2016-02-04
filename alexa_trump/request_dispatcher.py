from ask_trump_responder import AskTrumpResponder
from help_responder import HelpResponder


def request_dispatcher(request):
    '''Inspect the request and dispatch it to the correct responder.
    '''

    if _asked_trump_a_question(request):
        return AskTrumpResponder(request)
    else:
        return HelpResponder()


def _asked_trump_a_question(request):
    return (request.intent == 'AskTrumpIntent' and len(request.question) > 0)
