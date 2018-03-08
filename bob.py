def hey(phrase):
    phrase = phrase.strip()
    # An empty string means nothing was said because the string was stripped of whitespace.
    if phrase == "":
        return "Fine. Be that way!"
    # Yelled questions will be upper case and end in a question mark.
    elif phrase.isupper() and phrase[-1] == "?":
        return "Calm down, I know what I'm doing!"
    # Other questions just end in a "?".
    elif phrase[-1] == "?":
        return "Sure."
    # Yelled phrases will be uppercase.
    elif phrase.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
