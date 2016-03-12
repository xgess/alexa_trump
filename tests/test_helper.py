import json
import os

from alexa_trump.request import Request


FIXTURE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')

def _read_fixture_to_dict(fixture_file_name):
    with open(os.path.join(FIXTURE_DIRECTORY, fixture_file_name)) as json_file:
        file_as_dict = json.load(json_file)
    return file_as_dict


def launch_request_dict():
    return _read_fixture_to_dict('launch_request.json')

def launch_request():
    return Request(launch_request_dict())

def launch_response_dict():
    return _read_fixture_to_dict('launch_response.json')


def help_request_dict():
    return _read_fixture_to_dict('help_request.json')

def help_request():
    return Request(help_request_dict())

def help_response_dict():
    return _read_fixture_to_dict('help_response.json')


def stop_request_dict():
    return _read_fixture_to_dict('stop_request.json')

def stop_request():
    return Request(stop_request_dict())

def stop_response_dict():
    return _read_fixture_to_dict('stop_response.json')


def cancel_request_dict():
    return _read_fixture_to_dict('cancel_request.json')

def cancel_request():
    return Request(cancel_request_dict())

def cancel_response_dict():
    return _read_fixture_to_dict('cancel_response.json')


def ask_trump_request_dict(question):
    request_dict = _read_fixture_to_dict('ask_trump_request.json')
    request_dict['request']['intent']['slots']['question']['value'] = question
    return request_dict

def ask_trump_request(question):
    return Request(ask_trump_request_dict(question))

def ask_trump_response_dict(question, answer):
    response_dict = _read_fixture_to_dict('ask_trump_response.json')
    card_content = question + ' => ' + answer
    response_dict['response']['outputSpeech']['text'] = answer
    response_dict['response']['card']['content'] = card_content
    return response_dict
