'''
git a commit from the github or from the company server and set the commit in the
Excel file
'''
from datetime import datetime
from pydriller import Repository
from pydriller.domain.commit import ModificationType
import xlsxwriter as xw
import argparse

parser= argparse.ArgumentParser(description='git_parser commit from GitHub')
parser.add_argument('-o','--output_file', type=str,metavar='',required=True,
                    help='Path on the computer to same created Excel file')
parser.add_argument('-r','--repository', type=str,metavar='',required=True,
                    help='Path on the repository I want the script to pase')
args=parser.parse_args()




def show_commit(output_file,repository):

    wb = xw.Workbook(output_file+"\outputExcel_file.xlsx")
    ws = wb.add_worksheet(name="parser_git_commit")

    firstDay = datetime(2022, 5, 1)
    toDay = datetime.now()

    bold = wb.add_format({'bold': True})
    italic = wb.add_format(dict(italic=True))

    Row_number = 0
    Col_number = 0

    ws.write(Row_number, Col_number, 'File Name', bold)
    ws.write(Row_number, Col_number + 1, 'Commit msg', bold)
    ws.write(Row_number, Col_number + 2, 'Commit Date', bold)
    ws.write(Row_number, Col_number + 3, 'hash commit', bold)

    Row_number += 1

    for commit in Repository(path_to_repo=repository, since=firstDay, to=toDay).traverse_commits():
        for modified_file in commit.modified_files:
            ws.write(Row_number, Col_number, modified_file.filename, italic)
            ws.write(Row_number, Col_number + 1, commit.msg)
            ws.write(Row_number, Col_number + 2, str(commit.author_date))
            ws.write(Row_number, Col_number + 3, commit.hash)

            Row_number += 1

    wb.close()

if __name__=='__main__':
    show_commit(args.output_file, args.repository)
