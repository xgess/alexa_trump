import random

from tagged_trumpisms import tagged_trumpism


class TrumpQuestion(object):

    def __init__(self, question):
        self.question = question.lower()
        self.question_words = self.question.split()
        self._logic_functions = list(TrumpLogicAggregator.functions)
        random.shuffle(self._logic_functions)

    def answer(self):
        lazy_answers = (logic_function(self) for logic_function in self._logic_functions)
        appropriate_answers = (answer for answer in lazy_answers if answer is not None)
        first_appropriate_answer = next(appropriate_answers)
        return first_appropriate_answer


class TrumpLogicAggregator():
    functions = []

    def __init__(self, function):
        self.functions.append(function)
        self.function = function

    def __call__(self, *args):
        return self.function(*args)


@TrumpLogicAggregator
def tagged_quotes(trump_question):
    tagged_hits = tagged_trumpism(trump_question.question_words)
    if len(tagged_hits) > 0:
        random.shuffle(tagged_hits)
        return tagged_hits[0]

@TrumpLogicAggregator
def always_acceptable(trump_question):
    return random.choice([
        "I will build a great wall. and nobody builds walls better than me, believe me.",
        "If Ivanka were'nt my daughter, perhaps I'd be dating her.",
        "The beauty of me is that I'm very rich",
        "I don't like losers",
        "I could stand in the middle of fifth avenue and shoot somebody and I wouldn't lose any voters",
        "I have the world's greatest memory. It's one thing everyone agrees on.",
        "Do you mind if I sit back a little, because your breath is very bad.",
        "I will absolutely apologize sometime in the hopefully distant future if I'm ever wrong."
    ])

@TrumpLogicAggregator
def how_question(trump_question):
    if trump_question.question.startswith('how'):
        return "I will build a great wall. and nobody builds walls better than me, believe me."

@TrumpLogicAggregator
def why_question(trump_question):
    if trump_question.question.startswith('why'):
        return "Because you're fired."

