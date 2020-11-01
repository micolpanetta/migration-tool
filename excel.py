from openpyxl import Workbook
from openpyxl.styles import Font
from datetime import datetime

def save_excel(b2b, see, ids):
    wb = Workbook()
    b2b_sheet = wb.active
    b2b_sheet.title = "B2B"
    see_sheet = wb.create_sheet(title="SEE")
    result_sheet = wb.create_sheet(title="Result")
    result_sheet.append(["Key", "Number of KO", "Result Counter"])

    for val in b2b:
        b2b_sheet.append([val["bgm"], val["content"]])

    for val in see:
        see_sheet.append([val["bgm"], val["content"]])

    for val in ids:
        result_sheet.append([ val["bgm"], val["ko_count"], val["unh_unt_result"] ])

    for id in ids:
        sheet = wb.create_sheet(title="ID"+id["bgm"])

        sheet.append(["B2B Message", "Seeburger Message", "Result", "Note",
                      "", "Segment", "Counter", "Result", "", "Numero KO"])

        for b2b_see_result in id["diff"]:
            sheet.append([b2b_see_result[0], b2b_see_result[1], b2b_see_result[2]])

        sheet['J2'] = id["ko_count"]
        sheet['F2'] = "UNH"
        sheet['F3'] = "UNT"
        sheet['G2'] = id["b2b_unh_counter"]
        sheet['G3'] = id["b2b_unt_counter"]
        sheet['H2'] = id["unh_unt_result"]

        #sheet['A1'].font = Font(bold=True)
        #sheet['B1'].font = Font(bold=True)
        #sheet['C1'].font = Font(bold=True)
        #sheet['D1'].font = Font(bold=True)
        #sheet['F1'].font = Font(bold=True)
        #sheet['G1'].font = Font(bold=True)
        #sheet['H1'].font = Font(bold=True)
        #sheet['J1'].font = Font(bold=True)


#    wb.save(filename = "./diff-" + datetime.today().strftime('%Y%m%d%H%M%S') + ".xlsx")
    wb.save(filename = "./diff.xlsx")
