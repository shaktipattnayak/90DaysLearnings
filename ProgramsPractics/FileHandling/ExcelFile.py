from openpyxl import Workbook, load_workbook


def write_excel(filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "SampleSheet"

    ws.append(["ID", "Name", "Score"])

    data = ([
        [1, "Shakti", 80],
        [2, "Shiva", 60],
        [3, "Priya", 40],
        [4, "Sujeet", 86],
        [5, "Tribhuvan", 74],

    ])

    for row in data:
        ws.append(row)
    
    wb.save(filename)
    print(f"File Saved: {filename}")


write_excel("TestSpreadsheet.xlsx")