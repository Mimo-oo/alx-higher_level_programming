#!/usr/bin/python3


def best_score(a_dictionary):
    score = 0
    h_score = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > score:
                score = value
                h_score = key
    return h_score
