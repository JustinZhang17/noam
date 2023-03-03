import ast

wordlist_prune = open("words_pruneV2.txt", "w", encoding='UTF8')

list = []
i = 0

with open("words_prune.txt", "r", encoding='UTF8') as wordlist:
    for line in wordlist:
        term = ast.literal_eval(line)

        if (term['pronounciation'] == [] or term['partOfSpeech'] == [] or term['sentences'] == []):
            continue

        if (term['name'] in list):
            print(term['name'])
            continue

        list.append(term['name'])
        wordlist_prune.write(line)

wordlist_prune.close()
wordlist.close()
