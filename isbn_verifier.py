def verify(isbn):
    isbn = isbn.replace("-", "")
    i_l = list(isbn)
    if len(i_l) != 10:
        return False
    else:
        if i_l[9] in ("X", "x"):
            i_l[9] = 10
        else:
            pass
        try:
            i_l = list(map(int, i_l))
            if 0 == isbn_form(i_l):
                return True
            elif 0 != isbn_form(i_l):
                return False
        except ValueError:
            return False


def isbn_form(isbn_list):
    i_l = isbn_list
    return (i_l[0] * 10
            + i_l[1] * 9
            + i_l[2] * 8
            + i_l[3] * 7
            + i_l[4] * 6
            + i_l[5] * 5
            + i_l[6] * 4
            + i_l[7] * 3
            + i_l[8] * 2
            + i_l[9] * 1) % 11
