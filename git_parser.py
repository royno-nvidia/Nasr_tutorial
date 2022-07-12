
'''
git a commit from the github or from the company server and set the commit in the 
Excel file
'''
from datetime import datetime
from git import Commit
from pydriller import Repository
from pydriller.domain.commit import ModificationType
import xlsxwriter as xw
import pandas as pd

wb_workbook = xw.Workbook("book1233.xlsx")
ws_worksheet = wb_workbook.add_worksheet(name="Git_commit")


def git_commit(url_webset):
    '''Function to git commit from the web sit to the xlsx file...'''

    first_day = datetime(2022, 5, 1)
    to_day = datetime.now()

    row_number = 0
    col_number = 0

    bold = wb_workbook.add_format({'bold': True})
    italic = wb_workbook.add_format(dict(italic=True))

    ws_worksheet.write(row_number, col_number, 'File Name', bold)
    ws_worksheet.write(row_number, col_number+1, 'Commit msg', bold)
    ws_worksheet.write(row_number, col_number+2, 'Commit Date', bold)
    ws_worksheet.write(row_number, col_number+3, 'hash commit', bold)

    row_number += 1
   # url = [r"C:\Users\a\Downloads\my-Github\Git_course"]
    # url2 = [r"C:\Users\a\Downloads\my-Github\Our_Project"]
    # url3 = ["https://github.com/nasrsaab/myFiles.git"]
    # url4 = ["https://github.com/nasrsaab/Git_course.git"]

    for commit in Repository(path_to_repo=url_webset, since=first_day, to=to_day).traverse_commits():
        for modified_file in commit.modified_files:
            ws_worksheet.write(row_number, col_number,
                               modified_file.filename, italic)
            ws_worksheet.write(row_number, col_number+1, commit.msg)
            ws_worksheet.write(row_number, col_number+2,
                               str(commit.author_date))
            ws_worksheet.write(row_number, col_number+3, commit.hash)
            row_number += 1

    wb_workbook.close()


'''open the xlsx file and put the data in dataframe '''
df_dataframe = pd.read_excel("book1233.xlsx")
df_dataframe.to_csv('book1233.csv')
df_dataframe = pd.read_csv('book1233.csv')

# print the dataframe
print(df_dataframe)
