'''
git a commit from the github or from the company server and set the commit in the
Excel file
'''
from datetime import date, timedelta,datetime
from pydriller import Repository
from pydriller.domain.commit import ModificationType
import xlsxwriter as xw
import argparse




def show_commit(output_file,repository,show_lats_days):

    #Create a output file
    if output_file:
        #Choose a new local path
        wb = xw.Workbook(output_file +"\outputExcel_file.xlsx")
        print("\nExcel file created in: " + output_file + "\outputExcel_file.xlsx")
    else:
        #Set in a same arg_parser.py path
        wb = xw.Workbook("outputExcel_file.xlsx")
        print("\nExcel file created in: local_python_file_path\outputExcel_file.xlsx")

    #Set worksheet name
    ws = wb.add_worksheet(name="parser_git_commit")

    #Add worksheet font format
    bold = wb.add_format({'bold': True})
    italic = wb.add_format(dict(italic=True))

    #Calculate date
    to_day = datetime.now().today()

    if show_lats_days:

        first_day = to_day - timedelta(days=show_lats_days)
        print(first_day)
        print(to_day)

    else:
        first_day = datetime.min
        print(first_day)
        print(to_day)

    print("Please wait...")
    Row_number = 0
    Col_number = 0

    ws.write(Row_number, Col_number, 'hash commit', bold)
    ws.write(Row_number, Col_number + 1, 'Commit subject', bold)
    ws.write(Row_number, Col_number + 2, 'Commit Date', bold)
    ws.write(Row_number, Col_number + 3, 'File Name', bold)

    Row_number += 1
    hash_commit = "xxxx"
    Col_n = 3

    for commit in Repository(path_to_repo=repository, since=first_day, to=to_day).traverse_commits():
        for modified_file in commit.modified_files:
            ws.write(Row_number, Col_number, commit.hash[:12])
            ws.write(Row_number, Col_number + 1, commit.msg)
            ws.write(Row_number, Col_number + 2, str(commit.author_date))
            ws.write(Row_number, Col_number + 3, modified_file.filename, italic)

            if hash_commit in commit.hash[:12]:
                Col_n = Col_n + 1
                ws.write(Row_number, Col_number + Col_n, modified_file.filename, italic)
            else:
                hash_commit = commit.hash[:12]
                Row_number += 1

    wb.close()
    print("finish...")

if __name__=='__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description='Parser commit from any repository path')

    # Add Arguments
    parser.add_argument('-o', '--output_file', type=str, default=False,
                        help='Set a local computer path to create an Excel file')
    parser.add_argument('-r', '--repository', type=str, metavar='', required=True,
                        help='Set the repository path you want to parse it')
    parser.add_argument('-d', '--show_lats_days', type=int, default=False,
                        help='show me only commits from the last \'X\' days.if not provided -'
                             ' show all commits In the repository.')
    # Parse the argument
    args = parser.parse_args()

    show_commit(args.output_file, args.repository,args.show_lats_days)
