def get_middle(s):
    str_len = len(s)
    if str_len % 2 != 0:
        return s[int(str_len / 2)]
    elif str_len % 2 == 0:
        return s[int(str_len / 2 - 1) : int(str_len / 2 + 1)]
    else:
        return s
