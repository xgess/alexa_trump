class Request(object):
    '''convenience wrapper around the request made by the Alexa Skills Kit'''

    def __init__(self, event_dict):
        self.event_dict = event_dict

    @property
    def question(self):
        return self.event_dict['request']['intent']['slots']['question']['value']

    @property
    def intent(self):
        return self.event_dict['request']['intent']['name']
