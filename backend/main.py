from fastapi import FastAPI
from fastapi.responses import FileResponse
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
import uvicorn
import ast
import random
import hashlib

wb = Workbook()
ws = wb.active

filePath = "../assets/word_bank.txt"
app = FastAPI()

apiKeys = ["94dbb126ff4e9700d201333b897b027505dfd2874f873b947f7e374592e3d96ddb369d9014908257decdf965a327582da4774cc5b687c386dd1a9785fafa3605"]


def pro_str(arr=[]):
    s = ""
    for pro in arr:
        s += "\\ " + pro + " \\" + " or "
    return s[:-4]


def pos_str(arr=[]):
    s = ""
    for pos in arr:
        s += pos + ", "
    return s[:-2]


@app.get("/wordlist")
async def get_wordlist(api_key: str = "", size: int = 200):

    # FIXME: return more useful error messages for Client Side
    if (size < 1 or size > 600):
        return {"Status_Code": 404}

    # FIXME: return more useful error messages for Client Side
    if (hashlib.sha512(api_key.encode()).hexdigest() not in apiKeys):
        return {"Status_Code": 404}

    list_name: int = random.getrandbits(64)

    lines: list = open("../assets/word_bank.txt", "r",
                       encoding='UTF8').read().splitlines()

    random.shuffle(lines)

    font_family: str = "Times New Roman"

    ws["A1"] = 'Word'
    ws["B1"] = 'Pronunciation'
    ws["C1"] = 'Part Of Speech'
    ws["D1"] = 'Definition'
    ws["E1"] = 'Sentence'
    ws["F1"] = 'Etymology'

    ws["A1"].font = Font(size=13, bold=True, name=font_family)
    ws["B1"].font = Font(size=13, bold=True, name=font_family)
    ws["C1"].font = Font(size=13, bold=True, name=font_family)
    ws["D1"].font = Font(size=13, bold=True, name=font_family)
    ws["E1"].font = Font(size=13, bold=True, name=font_family)
    ws["F1"].font = Font(size=13, bold=True, name=font_family)

    for i in range(size):
        term = ast.literal_eval(lines[i])
        ws["A" + str(i+2)] = term['name']
        ws["B" + str(i+2)] = pro_str(term['pronunciation'])
        ws["C" + str(i+2)] = pos_str(term['partOfSpeech'])
        ws["D" + str(i+2)] = term['definition']
        ws["E" + str(i+2)] = term['sentences'][0]
        ws["F" + str(i+2)] = term['etymology']

        ws["A" + str(i+2)].font = Font(name=font_family)
        ws["B" + str(i+2)].font = Font(name=font_family)
        ws["C" + str(i+2)].font = Font(name=font_family)
        ws["D" + str(i+2)].font = Font(name=font_family)
        ws["E" + str(i+2)].font = Font(name=font_family)
        ws["F" + str(i+2)].font = Font(name=font_family)

    wb.save(str(list_name) + ".xlsx")
    return FileResponse(path=(str(list_name) + ".xlsx"), filename="Noam-Wordlist-" + str(size) + ".xlsx")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
