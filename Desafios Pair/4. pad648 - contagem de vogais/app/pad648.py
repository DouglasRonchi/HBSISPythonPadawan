import re


def vowel_count(word):
    return len(re.findall('[a,e,i,o,u]', word))
