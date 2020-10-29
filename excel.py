from openpyxl import Workbook
from datetime import datetime

def save_excel(b2b, see, diffs):
    wb = Workbook()
    b2b_sheet = wb.active
    b2b_sheet.title = "B2B"
    see_sheet = wb.create_sheet(title="SEE")

    for val in b2b:
        b2b_sheet.append([val["bgm"], val["content"]])

    for val in see:
        see_sheet.append([val["bgm"], val["content"]])

    for diff in diffs:
        diffs_sheet = wb.create_sheet(title="ID"+diff["bgm"])
        for row in diff["diff"]:
            diffs_sheet.append([row[0], row[1], row[2]])

    wb.save_excel(filename = "./diff-" + datetime.today().strftime('%Y%m%d%H%M%S') + ".xlsx")
