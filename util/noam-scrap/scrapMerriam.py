# External Imports
import requests
from bs4 import BeautifulSoup
import re
import json

#  Internal Imports
from helper import etymology_strip


def get_word(str="default"):
    global page
    global soup
    str_clean = re.sub('[^a-zA-Z]+', '', str)
    URL = "https://www.merriam-webster.com/dictionary/" + str_clean
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return {
        "name": get_name(),
        "pronunciation": get_pronunciation(),
        "partOfSpeech": get_part_of_speech(),
        "definition": get_definition(),
        "sentences": get_sentences(),
        "etymology": get_etymology()
    }


def get_name():
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


def get_pronunciation():
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


def get_part_of_speech():
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


def get_definition():
    r = {}

    # pos = part of speech
    curr_pos = ''
    out = soup.findAll(
        'div', id=lambda x: x and x.startswith('dictionary-entry-'))
    for x in out:
        a = x.findAll(["span", "h2"], class_=["dtText", "parts-of-speech"])
        for y in a:
            for s in y.select('strong'):
                s.extract()
            for s in y.select('span'):
                s.extract()

            if y.text.strip() in get_part_of_speech():
                curr_pos = y.text.strip()
                r[y.text.strip()] = []
            else:
                if (len(y.text.strip()) > 3 and curr_pos != ''):
                    r[curr_pos].append(y.text.strip())
    return r


def get_sentences():
    out = soup.find("div", id="examples")

    # Returns for unknown words
    if (out is None):
        return {}

    out = out.find("div", class_="in-sentences")

    # Returns for unknown words
    if (out is None):
        return {}

    r = {}
    if (len(get_part_of_speech()) == 1 or out.find("span", class_="ex-header") is None):
        curr = get_part_of_speech()[0]
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


def get_etymology():
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
        if (len(get_part_of_speech()) == 0):
            r["word"] = etymology_strip(d[0].text.strip())
        else:
            r[get_part_of_speech()[0]] = etymology_strip(d[0].text.strip())
    else:
        for x in range(len(a)):
            if (a[x] is not None and d[x] is not None):
                r[a[x].text.strip().lower()] = etymology_strip(d[x].text.strip())

    return r


wordlistCreate = open("wordlistCreate.txt", "a", encoding='UTF8')
with open("../../../assets/wordlistIterations/wordlistPrunedV4.txt", "r") as file:
    for line in file:
        r = get_word(line)
        if (r['etymology'] != {} and r['sentences'] != {} and r['definition'] != {}):
            print(r["name"])
            wordlistCreate.write(str(r) + "\n")


wordlistCreate.close()
file.close()

# Pruning the First Word List

# ```
# wordlistPrune = open("wordlistPruneV2.txt", "r+")
# with open("wordlistPrunedV1.txt") as file:
#     for line in file:
#         if (containsAlpha(line.rstrip()) and len(line.rstrip()) > 3):
#             word = getWord(line.rstrip())
#             if (len(word['name']) > 0 and len(word['pronunciation']) > 0 and len(word['partOfSpeech']) > 0):
#                 if (not word['name'][0] in wordlistPrune.read()):
#                     wordlistPrune.write(word['name'][0] + "\n")
# wordlistPrune.close()
# file.close()
# ```

# Pruning the Second Word List

# ```
# wordlistPrune = open("wordlistPrunedV3.txt", "w")
# buf = []
# with open("wordlistPrunedV2.txt", "r") as file:
#     for line in file:
#         if (len(line) > 0):
#             buf.append(line)
#     buf = list(dict.fromkeys(buf))
#     for l in buf:
#         wordlistPrune.write(l)
# wordlistPrune.close()
# file.close()
# ```
