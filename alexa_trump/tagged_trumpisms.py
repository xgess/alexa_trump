import random

def tagged_trumpism(question_words):
    matching_answers = [answer for answer, tags in trumpisms.items() if _overlaps(tags, question_words)]
    return matching_answers

def _overlaps(list_1, list_2):
    return bool(set(list_1) & set(list_2))

trumpisms = {
    "The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.":
        ["temperature", "earth", "china"],
    "You know, it really doesn't matter what the media write as long as you've got a young and beautiful piece of ass.":
        ["media", 'news', 'television'],
    "We're going to tax China.":
        ["tax", 'taxes', 'china'],
    "When was the last time anybody saw us beating, let's say, China in a trade deal? They kill us. I beat China all the time. All the time.":
        ['china', 'trade', 'deal', 'game', 'competition', 'competitive'],
    "I will build a great wall. and nobody builds walls better than me, believe me.":
        ['mexico', 'wall', 'immigration', 'immigrants', 'southern', 'border'],
    "They're bringing drugs. They're bringing crime. They're rapists. And some, I assume, are good people.":
        ['mexico', 'mexican', 'crime'],
    "The wall will go up and Mexico will start behaving.":
        ['mexico', 'world', 'global', 'united', 'nations', 'international'],
    "Our great African American President hasn't exactly had a positive impact on the thugs who are so happily and openly destroying Baltimore!":
        ['president', 'obama', 'baltimore', 'crime', 'black', 'african'],
    "The only kind of people I want counting my money are little short guys that wear yarmulkes every day.":
        ['money', 'jewish', 'jews', 'rich', 'wealth', 'wealthy'],
    "If I were running, The View, I'd fire Rosie O'Donnell. I mean, I'd look her right in that fat ugly face of hers and I'd say, Rosie, you're fired.":
        ["women", 'fired', 'job', 'jobs'],
    "Rosie O'Donnell's disgusting both inside and out. You take a look at her, she's a slob. She talks like a truck driver, she doesn't have her facts, she'll say anything that comes to her mind":
        ['impulsive', 'rosie', 'women', 'ladies'],
    "Arianna Huffington is unattractive both inside and out. I fully understand why her former husband left her for a man. he made a good decision.":
        ['gay', 'news', 'arianna', 'huffington', 'post', 'marriage', 'married'],
    "Hillary Clinton was the worst Secretary of State in the history of the United States. There's never been a Secretary of State so bad as Hillary. The world blew up around us. ":
        ['hillary', 'clinton', 'state', 'international', 'history'],
    "If you can't get rich dealing with politicians, there's something wrong with you.":
        ['politicians', 'money', 'rich'],
    "A certificate of live birth is not the same thing by any stretch of the imagination as a birth certificate.":
        ['barack', 'obama', 'birth', 'born', 'baby', 'kenya'],
    "He's not a war hero. He's a war hero because he was captured. I like people that weren't captured, OK.":
        ["mccain"],
    "All the women on The Apprentice flirted with me, consciously or unconsciously. That's to be expected.":
        ["apprentice", 'women', 'attractive', 'flirt'],
    "One of the key problems today is that politics is such a disgrace. Good people don't go into government.":
        ["politics", 'politicians', 'government'],
    "Part of the beauty of me is that I'm very rich. So if I need 600 million dollars, I can put 600 million dollars myself.":
        ['race', 'rich', 'money', 'candidates'],
    "Money was never a big motivation for me, except as a way to keep score.":
        ['money', 'rich', 'wealth'],
    "I have a great relationship with the Mexican people.":
        ['international', 'mexico', 'mexican'],
    "We will have so much winning if I get elected that you may get bored with winning.":
        ['win', 'lose', 'america', 'race', 'election'],
    "I have the world's greatest memory. It's one thing everyone agrees on.":
        ['when', 'memory', 'thoughts', 'history', 'fun', 'time', 'times']
}
