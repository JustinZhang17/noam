import requests
from bs4 import BeautifulSoup
import re

wordlist = open("words2.txt", "a", encoding='UTF8')

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


def etymologyStrip(phrase=""):
    """
    Take a sentence and return a string with just the origins

    ie.
    Input: Middle English quik, from Old English cwic; akin to Old Norse kvikr living, Latin vivus living, vivere to live, Greek bios, zōē life
    Output: Middle English, Old English, Old Norse, Latin, Greek
    """
    r = ''
    for i in ETYMOLOGY_LIST:
        if i.lower() in str(phrase).lower():
            r += (i + ", ")

    if (r == ''):
        return 'Unknown'
    return r[:len(r)-2]


def getPronunciation(str="default"):
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://www.merriam-webster.com/dictionary/" + strClean
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    out = soup.find_all("span", class_="prons-entries-list-inline")

    # Returns for unknown words
    if (out is None):
        return {}

    r = []
    for x in out:
        a = x.find(['a', 'div'], class_="prons-entry-list-item")
        if (a is not None):
            r.append(a.text.strip())

    return [*set(r)]


def getPartOfSpeech(str="default"):
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://www.merriam-webster.com/dictionary/" + strClean
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    out = soup.findAll(
        'div', id=lambda x: x and x.startswith('dictionary-entry-'))

    # Returns for unknown words
    if (out is None):
        return {}

    r = []
    for x in out:
        a = x.find("h2", class_="parts-of-speech")
        if (a is not None):
            pos = a.text.strip().lower()
            if (pos == 'noun (1)' or pos == 'noun (2)' or pos == 'noun (3)' or pos == 'noun suffix'):
                r.append('noun')
            elif (pos == 'verb (1)' or pos == 'verb (2)' or pos == 'verb (3)' or pos == 'intransitive verb'):
                r.append('verb')
            elif (pos == 'adjective (1)' or pos == 'adjective (2)' or pos == 'adjective (3)' or pos == 'adjective suffix'):
                r.append('adjective')
            elif (pos == 'adverb (1)' or pos == 'adverb (2)' or pos == 'adverb (3)'):
                r.append('adverb')
            elif (pos == 'adverb or adjective' or pos == 'adjective or adverb'):
                r.append('adverb')
                r.append('adjective')
            else:
                r.append(a.text.strip().lower())
    return [*set(r)]


def getSentences(str="default"):
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://wordsinasentence.com/" + strClean + "-in-a-sentence/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    out = soup.find_all(
        "a", class_="audio-play")

    # Returns for unknown words
    if (out is None):
        return {}

    r = []
    for x in out:
        if (x is not None and x['data-keywords'].lower() != str.lower() and x['data-keywords'].lower() != str.lower() + " "):
            r.append(x['data-keywords'])

    return [*set(r)]


def getDefinition(str="default"):
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://wordsinasentence.com/" + strClean + "-in-a-sentence/"
    page = requests.get(URL)
    if (page.status_code == 404):
        URL = "https://wordsinasentence.com/" + strClean + "/"
        page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    out = soup.find(
        "p", attrs={"style": "font-style:none; font-family:; font-size:17px; color:#504A4B;padding-top: 0px; padding-bottom:5px; padding-left: 0px; padding-right: 10px;"})

    if (out is None):
        out = soup.find(
            "p", attrs={"style": "font-style:none; font-family:; font-size:17px; color:#504A4B;padding-top: 0px; padding-bottom:15px; padding-left: 0px; padding-right: 10px;"})

    if (out is None):
        out = soup.find(
            "p", attrs={"style": "font-style:none; font-family:; font-size:18px; color:#504A4B;padding-top: 0px; padding-bottom:5px; padding-left: 0px; padding-right: 10px;"})

    # Returns for unknown words
    if (out is None):
        print(str)
        return {}

    r = out.text.strip()

    return r


def getEtymology(str="default"):
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://www.etymonline.com/search?q=" + strClean
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    out = soup.find(
        "section", class_="word__defination--2q7ZH")

    # Returns for unknown words
    if (out is None):
        print(str)
        return {}

    r = out.text.strip()

    return r


for i in range(37):
    output = {}
    URL = "https://wordsinasentence.com/vocabulary-word-list?_page=" + \
        str(i + 1)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    out = soup.find_all("div", class_="pt-cv-ctf-list")

    for x in out:
        word = x.text.strip()
        if (word is not None and word.isalpha()):
            print(word.lower())
            output["name"] = word.lower()
            output["pronunciation"] = getPronunciation(word.lower())
            output["partOfSpeech"] = getPartOfSpeech(word.lower())
            output["definition"] = getDefinition(word.lower())
            output["sentences"] = getSentences(word.lower())
            output["etymology"] = etymologyStrip(getEtymology(word.lower()))

            wordlist.write(str(output) + "\n")


wordlist.close()
