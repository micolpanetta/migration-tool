from openpyxl import Workbook
from datetime import datetime

def save_excel(b2b, see, diffs):
    wb = Workbook()
    b2b_sheet = wb.active
    b2b_sheet.title = "B2B"
    see_sheet = wb.create_sheet(title="SEE")
    result_sheet = wb.create_sheet(title="Result")


    for val in b2b:
        b2b_sheet.append([val["bgm"], val["content"]])

    for val in see:
        see_sheet.append([val["bgm"], val["content"]])

    for diff in diffs:
        diffs_sheet = wb.create_sheet(title="ID"+diff["bgm"])
        diffs_sheet.append(["B2B Message", "Seeburger Message", "Result", "Note",
                            "", "Segment", "Counter", "Result", "", "Numero KO"])
        for row in diff["diff"]:
            diffs_sheet.append([row[0], row[1], row[2]])

    wb.save(filename = "./diff.xlsx")

#    wb.save(filename = "./diff-" + datetime.today().strftime('%Y%m%d%H%M%S') + ".xlsx")
