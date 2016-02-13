class Request(object):
    '''convenience wrapper around the request made by the Alexa Skills Kit'''

    def __init__(self, event):
        self.event = event

    @property
    def question(self):
        return self.event['request']['intent']['slots']['question']['value']

    @property
    def intent(self):
        if self._intent_request:
            return self.event['request']['intent']['name']

    @property
    def launch_request(self):
        return self._type == 'LaunchRequest'

    @property
    def _type(self):
        return self.event['request']['type']

    @property
    def _intent_request(self):
        return self._type == 'IntentRequest'
