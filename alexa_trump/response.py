from UserDict import UserDict

class Response(UserDict):
    BASE_DATA = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": None
            },
            "shouldEndSession": None
        }
    }

    def __init__(self, speech_text, end_session=True, card_title=None, card_content=None, reprompt_text=None):
        self.data = self.BASE_DATA
        self.data['response']['shouldEndSession'] = end_session
        self.data['response']['outputSpeech']['text'] = speech_text

        if card_title is not None and card_content is not None:
            self._add_card_node(card_title, card_content)
        if reprompt_text is not None:
            self._add_reprompt_node(reprompt_text)

    def _add_card_node(self, title, content):
        self.data['response']['card'] = {
            "type": "Simple",
            "title": title,
            "content": content
        }

    def _add_reprompt_node(self, text):
        self.data['response']['reprompt'] = {
            "outputSpeech": {
                "type": 'PlainText',
                "text": text
            }
        }
