from request import Request
from request_dispatcher import request_dispatcher


def lambda_handler(event, context):
    '''lambda entry point
    '''

    request = Request(event)
    responder = request_dispatcher(request)

    return dict(responder.response())
