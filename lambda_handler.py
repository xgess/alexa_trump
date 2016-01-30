
def lambda_handler(event, context):
    question = event['request']['intent']['slots']['question']['value']
    answer = "that sounds YOUDJ."

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
