from ask_trump_responder import AskTrumpResponder


def request_dispatcher(request):
    '''Inspect the request and dispatch it to the correct responder.
    '''

    if request.intent == 'AskTrumpIntent':
        return AskTrumpResponder(request)
