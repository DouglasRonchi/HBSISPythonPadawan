def accum(e):
    res = ""
    i = 0
    while i < len(e):
        n = 0
        while n < i + 1:
            if n == 0:
                res += e[i].upper()
            else:
                res += e[i].lower()
            n += 1
        res += "-"
        i += 1
    return res[:len(res) - 1]
