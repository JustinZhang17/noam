# External Imports
import requests
from bs4 import BeautifulSoup

#  Internal Imports
from strips import etymologyStrip

URL = "https://www.merriam-webster.com/dictionary/squeeze"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# TODO: Figure out classification of the words (Part of Speech Groupings))
# TODO: Word difficulty Classification (Part of Speech Groupings))


def getName():
    out = soup.find_all("div", class_="entry-header-content")
    r = []
    for x in out:
        a = x.find("h1", class_="hword")
        if (a is not None):
            r.append(a.text.strip())
    return [*set(r)]


def getPronunciation():
    out = soup.find_all("span", class_="prons-entries-list-inline")
    r = []
    for x in out:
        a = x.find("a", class_="prons-entry-list-item")
        if (a is not None):
            r.append(a.text.strip())
    return [*set(r)]


def getPartOfSpeech():
    out = soup.findAll(
        'div', id=lambda x: x and x.startswith('dictionary-entry-'))
    r = []
    for x in out:
        a = x.find("h2", class_="parts-of-speech")
        if (a is not None):
            r.append(a.text.strip().lower())
    return [*set(r)]


def getDefinition():
    pass


def getSentences():
    out = soup.find("div", id="examples")

    # Returns for unknown words
    if (out is None):
        return {}

    out = out.find("div", class_="in-sentences-container")
    print(out)
    pass


def getEtymology():
    out = soup.find("div", id="word-history")

    # Returns for unknown words
    if (out is None):
        return {}

    out = out.find("div", class_="etymology-content-section")
    r = {}
    a = out.find_all("p", class_="function-label")
    d = out.find_all("p", class_="et")

    for x in range(len(a)):
        if (a[x] is not None and d[x] is not None):
            # TODO: Implement etymologyStrip
            r[a[x].text.strip().lower()] = etymologyStrip(d[x].text.strip())

    return r


def getDifficulty():
    pass


print(getName())
print(getPronunciation())
print(getPartOfSpeech())
print(getEtymology())
# getSentences()
