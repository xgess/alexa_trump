import json
import os

from alexa_trump.request import Request


FIXTURE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')

def build_request_dict(question):
    with open(os.path.join(FIXTURE_DIRECTORY, 'basic_request.json')) as json_file:
        request_dict = json.load(json_file)
    request_dict['request']['intent']['slots']['question']['value'] = question
    return request_dict

def build_request(question):
    return Request(build_request_dict(question))

def build_response_dict(question, answer):
    with open(os.path.join(FIXTURE_DIRECTORY, 'basic_response.json')) as json_file:
        response_dict = json.load(json_file)

    card_content = question + ' => ' + answer
    response_dict['response']['outputSpeech']['text'] = answer
    response_dict['response']['card']['content'] = card_content

    return response_dict

def build_launch_request_dict():
    with open(os.path.join(FIXTURE_DIRECTORY, 'launch_request.json')) as json_file:
        request_dict = json.load(json_file)
    return request_dict
