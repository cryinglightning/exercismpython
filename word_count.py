import re


def word_count(phrase):
    phrase = re.sub(r"[^\w']", " ", phrase).replace("_", " ").lower()
    word_dict = {}
    for word in phrase.split():
        word = word.strip("\'")
        if word in word_dict:
            word_dict[word] = word_dict[word]+1
        else:
            word_dict[word] = 1
    return word_dict
