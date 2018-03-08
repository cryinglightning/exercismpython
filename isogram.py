def is_isogram(string):
    iso_test = list()
    for letter in string:
        if letter in iso_test:
            return False
        if letter != "-" and letter != " ":
            iso_test.append((letter.lower()))
    return True
