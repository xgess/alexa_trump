from ask_trump_responder import AskTrumpResponder
from help_responder import HelpResponder
from launch_responder import LaunchResponder
from stop_responder import StopResponder


def request_dispatcher(request):
    '''Inspect the request and dispatch it to the correct responder.
    '''

    if _asked_trump_a_question(request):
        return AskTrumpResponder(request)
    elif _opened_app_without_an_intent(request):
        return LaunchResponder()
    elif request.is_stop_or_cancel:
        return StopResponder()
    else:
        return HelpResponder()


def _asked_trump_a_question(request):
    return (request.intent == 'AskTrumpIntent' and len(request.question) > 0)

def _opened_app_without_an_intent(request):
    return request.is_launch
