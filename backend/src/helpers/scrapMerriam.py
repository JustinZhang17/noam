# External Imports
import requests
from bs4 import BeautifulSoup
import re
import json

#  Internal Imports
from helper import etymologyStrip

# TODO: Figure out classification of the words (Part of Speech Groupings))
# TODO: Word difficulty Classification (Part of Speech Groupings))

# URL = "https://www.merriam-webster.com/dictionary/default"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")


def getWord(str="default"):
    global page
    global soup
    strClean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://www.merriam-webster.com/dictionary/" + strClean
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return {
        "name": getName(),
        "pronunciation": getPronunciation(),
        "partOfSpeech": getPartOfSpeech(),
        "definition": getDefinition(),
        "sentences": getSentences(),
        "etymology": getEtymology()
    }


def getName():
    out = soup.find_all("div", class_="entry-header-content")

    # Returns for unknown words
    if (out is None):
        return {}

    r = []
    for x in out:
        a = x.find("h1", class_="hword")
        if (a is not None):
            r.append(a.text.strip())
    return [*set(r)]


def getPronunciation():
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


def getPartOfSpeech():
    out = soup.findAll(
        'div', id=lambda x: x and x.startswith('dictionary-entry-'))

    # Returns for unknown words
    if (out is None):
        return {}

    r = []
    for x in out:
        a = x.find("h2", class_="parts-of-speech")
        if (a is not None):
            r.append(a.text.strip().lower())
    return [*set(r)]


def getDefinition():
    r = {}
    currPOS = ''
    # TODO: Change this depend on part of speech array to know how many entries to work with
    out = soup.findAll(
        'div', id=lambda x: x and x.startswith('dictionary-entry-'))
    for x in out:
        a = x.findAll(["span", "h2"], class_=["dtText", "parts-of-speech"])
        for y in a:
            for s in y.select('strong'):
                s.extract()
            for s in y.select('span'):
                s.extract()

            if y.text.strip() in getPartOfSpeech():
                currPOS = y.text.strip()
                r[y.text.strip()] = []
            else:
                if (len(y.text.strip()) > 3 and currPOS != ''):
                    r[currPOS].append(y.text.strip())
    return r


def getSentences():
    out = soup.find("div", id="examples")

    # Returns for unknown words
    if (out is None):
        return {}

    out = out.find("div", class_="in-sentences")

    # Returns for unknown words
    if (out is None):
        return {}

    r = {}
    if (len(getPartOfSpeech()) == 1 or out.find("span", class_="ex-header") is None):
        curr = getPartOfSpeech()[0]
        r[curr] = []
        r[curr].append(
            out.find("span", class_="sents").text.strip().split("\n", 1)[0])
        for tag in out.find("span", class_="sents").next_siblings:
            if (tag.name == "span"):
                if ("function-label" in tag['class']):
                    curr = tag.text.lower().strip()
                    r[curr] = []
                if ("sents" in tag['class']):
                    r[curr].append(tag.text.strip().split("\n", 1)[0])
    else:
        curr = out.find("span", class_="ex-header").text.lower()
        r[curr] = []

        for tag in out.find("span", class_="ex-header").next_siblings:
            if (tag.name == "span"):
                if ("function-label" in tag['class']):
                    curr = tag.text.lower().strip()
                    r[curr] = []
                if ("sents" in tag['class']):
                    r[curr].append(tag.text.strip().split("\n", 1)[0])
    return r


def getEtymology():
    out = soup.find("div", id="word-history")

    # Returns for unknown words
    if (out is None):
        return {}

    out = out.find("div", class_="etymology-content-section")

    # Returns for unknown words
    if (out is None):
        return {}

    r = {}
    a = out.find_all("p", class_="function-label")
    d = out.find_all("p", class_="et")

    if (len(a) == 0):
        if (len(getPartOfSpeech()) == 0):
            r["word"] = etymologyStrip(d[0].text.strip())
        else:
            r[getPartOfSpeech()[0]] = etymologyStrip(d[0].text.strip())
    else:
        for x in range(len(a)):
            if (a[x] is not None and d[x] is not None):
                r[a[x].text.strip().lower()] = etymologyStrip(d[x].text.strip())

    return r


wordlistCreate = open("wordlistCreate.txt", "a", encoding='UTF8')
with open("../../../assets/wordlistIterations/wordlistPrunedV4.txt", "r") as file:
    for line in file:
        r = getWord(line)
        if (r['etymology'] != {} and r['sentences'] != {} and r['definition'] != {}):
            print(r["name"])
            wordlistCreate.write(str(r) + "\n")


wordlistCreate.close()
file.close()
