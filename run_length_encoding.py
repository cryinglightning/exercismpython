import re


def decode(string):
    decoded_str = ""
    decoded_list = []
    letters = re.split("\d+", string)
    letters = list(filter(None, letters))
    occurrences = re.split("[^\d]+", string)
    occurrences = list(filter(None, occurrences))
    for j, i in enumerate(letters):
        try:
            decoded_list.extend(i[0] * int(occurrences[j]) + i[1:])
        except IndexError:
            decoded_list.extend(occurrences + letters)
    return decoded_str.join(decoded_list)


def encode(string):
    decoded_list = list(string)
    encoded_string = ""
    encoded_list = []
    counter = 0
    for i, char in enumerate(decoded_list):
        try:
            if decoded_list[i] == decoded_list[i+1]:
                counter += 1
            elif counter > 0:
                encoded_list.append(str(counter + 1) + decoded_list[i])
                counter = 0
            else:
                encoded_list.append(decoded_list[i])
                counter = 0
        except IndexError:
            if counter > 0:
                encoded_list.append(str(counter + 1) + decoded_list[i])
                counter = 0
            else:
                encoded_list.append(decoded_list[i])
                counter = 0
    return encoded_string.join(encoded_list)
