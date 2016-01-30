from __future__ import print_function


def lambda_handler(event, context):
    print(event)

    question = event['request']['intent']['slots']['question']['value']
    answer = "that sounds youj."
    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": answer
            },
            "shouldEndSession": True,
            "card": {
                "type": "Simple",
                "title": "Ask Trump: " + question,
                "content": "Trump Says: " + answer
            }
        }
    }
    return response
