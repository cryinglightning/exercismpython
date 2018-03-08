def is_pangram(sentence):
    sentence = sentence.lower()
    alpha = list("qwertyuiopasdfghjklzxcvbnm")
    count = list()
    for char in sentence:
        if char in alpha and char not in count:
            count.append(char)
    if len(count) < 26:
        return False
    else:
        return True
