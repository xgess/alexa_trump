from functools import wraps
import random

from tagged_trumpisms import tagged_trumpism


def respond_to(question):
    question_words = [ a.lower() for a in question.split() ]

    all_possible_answers = [ logic_function(question_words) for logic_function in trump_logic_functions ]
    return random.choice(filter(None, all_possible_answers))

trump_logic_functions = []
def trump_logic_function(logic_function):
    trump_logic_functions.append(logic_function)
    return logic_function


@trump_logic_function
def tagged_quotes(question_words):
    tagged_hits = tagged_trumpism(question_words)
    if len(tagged_hits) > 0:
        random.shuffle(tagged_hits)
        return tagged_hits[0]

@trump_logic_function
def always_acceptable(question_words):
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

@trump_logic_function
def how_question(question_words):
    if question_words[0] == 'how':
        return "I will build a great wall. and nobody builds walls better than me, believe me."

@trump_logic_function
def why_question(question_words):
    if question_words[0] == 'how':
        return "Because you're fired."

