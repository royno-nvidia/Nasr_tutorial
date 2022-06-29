'''
got the commit message from the github 
put the file name and the commit message
and the data and the hash commit
in the Excel file
and print the Excel contain 
in the data frame
'''

from datetime import datetime
from git import Commit
from pydriller import Repository
from pydriller.domain.commit import ModificationType
# importing xlxswriter to create a Excel workbook
import xlsxwriter as xw


def git_commit(URL):
    '''
    the function take the url from the user 
    and pull up the info from the web sit
    and put it in the Excel file
    '''
    wb = xw.Workbook(r"E:\Python Examples\nvidia_git_proj\book2.xlsx")
    ws = wb.add_worksheet(name="Git_commit")

    first_day = datetime(2022, 5, 1)
    to_day = datetime.now()

    row_number = 0
    col_number = 0

    bold = wb.add_format({'bold': True})
    italic = wb.add_format(dict(italic=True))

    ws.write(row_number, col_number, 'File Name', bold)
    ws.write(row_number, col_number+1, 'Commit msg', bold)
    ws.write(row_number, col_number+2, 'Commit Date', bold)
    ws.write(row_number, col_number+3, 'hash commit', bold)

    row_number += 1

    for commit in Repository(path_to_repo=URL, since=first_day, to=to_day).traverse_commits():
        for modified_file in commit.modified_files:
            ws.write(row_number, col_number,  modified_file.filename, italic)
            ws.write(row_number, col_number+1, commit.msg)
            ws.write(row_number, col_number+2, str(commit.author_date))
            ws.write(row_number, col_number+3, commit.hash)
            row_number += 1

    wb.close()



