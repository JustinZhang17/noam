import os
from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import FileResponse
from openpyxl import Workbook
from openpyxl.styles import Font
import uvicorn
import ast
import random
import hashlib

filePath = "../assets/word_bank.txt"
app = FastAPI()

apiKeys = ["cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"]


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
async def get_wordlist(api_key: str = "", size: int = 200, background_tasks: BackgroundTasks = BackgroundTasks):

    hashed: int = hashlib.sha512(api_key.encode()).hexdigest()

    # FIXME: return more useful error messages for Client Side
    if (size < 1 or size > 600 or hashed not in apiKeys):
        return {"Status_Code": 404}

    list_name: int = random.getrandbits(64)

    lines: list = open("../assets/word_bank.txt", "r",
                       encoding='UTF8').read().splitlines()

    random.shuffle(lines)

    wb = Workbook()
    ws = wb.active

    font_family: str = "Times New Roman"

    set_sheet_style(ws, font_family)

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

    # Runs after the response is sent
    background_tasks.add_task(delete_file, list_name)
    background_tasks.add_task(wb.close)

    return FileResponse(path=(str(list_name) + ".xlsx"), filename="Noam-Wordlist-" + str(size) + ".xlsx", media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


def set_sheet_style(ws, font_family: str):
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


def delete_file(list_name: int):
    os.remove(str(list_name) + ".xlsx")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
