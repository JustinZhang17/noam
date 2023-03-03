<div align="center">
    <img src="assets/logo-color.png" alt="Logo" width="100" height="100" style="margin-bottom: -2rem;">

  <h2 align="center">Project Noam</h2>

  <p align="center">
    Word Scrapper - Wordlist Creator
  </p>
</div>

## About The Project

### In-progress Tasks

- [ ] Finishing Pruning the word list
- [ ] Remove Duplicates from the prune list
- [ ] Handle Cors whitelisting/blacklisting from FE to BE
- [ ] Scrap Definitions
- [ ] FE Design

## Getting Started

### Prerequisites

```
pip install Django
pip install pipenv (used in backend folder for virtual env) (> pipenv shell)
```

### Installation

<!-- USAGE EXAMPLES -->

### Usage

<!-- LICENSE -->

### License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- ACKNOWLEDGMENTS -->

### Acknowledgments

### Environment

[![](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white)]()
[![](https://img.shields.io/badge/FastApi-000000?style=for-the-badge&logo=FastApi&logoColor=white)]()
[![](https://img.shields.io/badge/React-000000?style=for-the-badge&logo=react&logoColor=white)]()
[![](https://img.shields.io/badge/Node.js-000000?style=for-the-badge&logo=node.js&logoColor=white)]()
[![](https://img.shields.io/badge/HTML5-000000?style=for-the-badge&logo=HTML5&logoColor=white)]()
[![](https://img.shields.io/badge/CSS3-000000?style=for-the-badge&logo=CSS3&logoColor=white)]()
[![](https://img.shields.io/badge/Typescript-000000?style=for-the-badge&logo=typescript&logoColor=white)]()
[![](https://img.shields.io/badge/Webpack-000000?style=for-the-badge&logo=webpack&logoColor=white)]()
[![](https://img.shields.io/badge/Babel-000000?style=for-the-badge&logo=babel&logoColor=white)]()
[![](https://img.shields.io/badge/Chakra_UI-000000?style=for-the-badge&logo=chakraui&logoColor=white)]()
[![](https://img.shields.io/badge/Framer-000000?style=for-the-badge&logo=framer&logoColor=white)]()
[![](https://img.shields.io/badge/Axios-000000?style=for-the-badge&logo=Axios&logoColor=white)]()
[![](https://img.shields.io/badge/Beautiful_Soup-000000?style=for-the-badge&logo=Python&logoColor=white)]()
[![](https://img.shields.io/badge/Netlify-000000?style=for-the-badge&logo=Netlify&logoColor=white)]()

### Other Notes

Pruning the First Word List

```
wordlistPrune = open("wordlistPruneV2.txt", "r+")
with open("wordlistPrunedV1.txt") as file:
    for line in file:
        if (containsAlpha(line.rstrip()) and len(line.rstrip()) > 3):
            word = getWord(line.rstrip())
            if (len(word['name']) > 0 and len(word['pronunciation']) > 0 and len(word['partOfSpeech']) > 0):
                if (not word['name'][0] in wordlistPrune.read()):
                    wordlistPrune.write(word['name'][0] + "\n")
wordlistPrune.close()
file.close()
```

Pruning the Second Word List

```
wordlistPrune = open("wordlistPrunedV3.txt", "w")
buf = []
with open("wordlistPrunedV2.txt", "r") as file:
    for line in file:
        if (len(line) > 0):
            buf.append(line)
    buf = list(dict.fromkeys(buf))
    for l in buf:
        wordlistPrune.write(l)
wordlistPrune.close()
file.close()
```
