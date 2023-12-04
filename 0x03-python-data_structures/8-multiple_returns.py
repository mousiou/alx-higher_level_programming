#!/usr/bin/python3

def multiple_returns(sentence):
    tup = (len(sentence), )
    if len(sentence) > 0:
        tup = tup + (sentence[0], )
    else:
        tup = tup + (None, )
    return tup
