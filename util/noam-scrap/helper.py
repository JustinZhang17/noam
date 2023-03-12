# External Imports
import re

ETYMOLOGY_LIST = [
    "Middle English",
    "Middle French",
    "Old English",
    "Old Norse",
    "Latin",
    "Greek",
    "Late Latin",
    "Anglo-French",
    "Germanic",
    "Japanese",
    "Dutch",
    "German",
    "French",
    "Old French",
    "African",
    "Americas",
    "Arabic",
    "Austronesian",
    "Basque",
    "Iberian",
    "Celtic",
    "Chinese",
    "Etruscan",
    "Iranian",
    "Italic",
    "Semitic",
    "Turkic",
    "Sanskrit",
    "New Latin",
    "Spanish"
]


def etymology_strip(phrase=""):
    """
    Take a sentence and return a string with just the origins

    ie.
    Input: Middle English quik, from Old English cwic; akin to Old Norse kvikr living, Latin vivus living, vivere to live, Greek bios, zōē life
    Output: Middle English, Old English, Old Norse, Latin, Greek
    """
    r = ''
    for i in ETYMOLOGY_LIST:
        if i.lower() in phrase.lower():
            r += (i + ", ")

    if (r == ''):
        return 'Unknown'
    return r[:len(r)-2]


def contains_alpha(s):
    return re.match(r'^[a-zA-Z]+$', s)
