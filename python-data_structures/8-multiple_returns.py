#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)  # Utilise un nom clair pour la variable
    if length == 0:
        result = length, None
    else:
        result = length, list(sentence)[0]
    return result
