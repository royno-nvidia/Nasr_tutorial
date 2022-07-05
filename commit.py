'''
git a commit from the github or from the company server and set the commit in the
Excel file
'''
from datetime import datetime

from pydriller import Repository
from pydriller.domain.commit import ModificationType
import xlsxwriter as xw
import pandas as pd


wb = xw.Workbook("Excel_File.xlsx")
ws = wb.add_worksheet(name="Git_commit")

firstDay = datetime(2022, 5, 1)
toDay = datetime.now()


bold = wb.add_format({'bold': True})
italic = wb.add_format(dict(italic=True))


def show_commit(url):
    Row_number = 0
    Col_number = 0

    ws.write(Row_number, Col_number, 'File Name', bold)
    ws.write(Row_number, Col_number + 1, 'Commit msg', bold)
    ws.write(Row_number, Col_number + 2, 'Commit Date', bold)
    ws.write(Row_number, Col_number + 3, 'hash commit', bold)


    Row_number += 1

    for commit in Repository(path_to_repo=url, since=firstDay, to=toDay).traverse_commits():
        for modified_file in commit.modified_files:
            ws.write(Row_number, Col_number, modified_file.filename, italic)
            ws.write(Row_number, Col_number + 1, commit.msg)
            ws.write(Row_number, Col_number + 2, str(commit.author_date))
            ws.write(Row_number, Col_number + 3, commit.hash)

            Row_number += 1

    wb.close()


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     url = [r"C:\Users\a\Downloads\my-Github\Git_course"]
#     url2 = [r"C:\Users\a\Downloads\my-Github\Our_Project"]
#     url3 = ["https://github.com/nasrsaab/myFiles.git"]
#     url4 = ["https://github.com/nasrsaab/Git_course.git"]
#     print_hi(url4)
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
