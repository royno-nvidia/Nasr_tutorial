'''
git a commit from the github or from the company server and set the commit in the
Excel file
'''
from datetime import date, timedelta,datetime
from pydriller import Repository
from pydriller.domain.commit import ModificationType
import xlsxwriter as xw
import pandas as pd



def show_commit(args):

    # Create a output file
    if args.output_file:
        # The user choosed a new local path through the flag (-o)
        Outputdata = args.output_file +"/outputExcel_file.xlsx"
        wb = xw.Workbook(Outputdata)
        print("\nExcel file created in: " + args.output_file + "/outputExcel_file.xlsx")
    else:
        # Set in a same arg_parser.py path
        Outputdata = "outputExcel_file.xlsx"
        wb = xw.Workbook(Outputdata)
        print("\nExcel file created in: local_python_file_path/outputExcel_file.xlsx")

    # Set worksheet name
    ws = wb.add_worksheet(name="parser_git_commit")

    # Add worksheet font format
    bold = wb.add_format({'bold': True})
    italic = wb.add_format(dict(italic=True))

    if args.show_lats_days:
        # The user defined to show only commits from the last 'X' days through the flag (-d)
        to_day = datetime.now().today()
        first_day = to_day - timedelta(days=args.show_lats_days)
        print(first_day)
        print(to_day)

    else:
        # Show all the commits
        first_day = None
        to_day = None


    print("Please wait...")
    Row_number = 0
    Col_number = 0

    # Set the titles in the firs row in the Excel file
    ws.write(Row_number, Col_number, 'hash commit', bold)
    ws.write(Row_number, Col_number + 1, 'Commit subject', bold)
    ws.write(Row_number, Col_number + 2, 'Commit Date', bold)
    ws.write(Row_number, Col_number + 3, 'File Name', bold)



    for commit in Repository(path_to_repo=args.repository, since=first_day, to=to_day).traverse_commits():
                Row_number += 1

                ws.write(Row_number, Col_number, commit.hash[:12])
                ws.write(Row_number, Col_number + 1, commit.msg)
                ws.write(Row_number, Col_number + 2, str(commit.author_date))
                ws.write(Row_number, Col_number + 3, ','.join([mf.filename for mf in commit.modified_files]), italic)

    wb.close()
    print("finish...")

    # open the xlsx file and put the data in dataframe
    df_dataframe = pd.read_excel(Outputdata)

    # print the dataframe
    print(df_dataframe)





