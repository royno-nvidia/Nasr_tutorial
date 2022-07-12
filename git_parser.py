
'''
git a commit from the github or from the company server and set the commit in the 
Excel file
'''
from datetime import datetime
from git import Commit
from pydriller import Repository
from pydriller.domain.commit import ModificationType
import pandas as pd


firstDay = datetime(2022, 5, 1)
toDay = datetime.now()

Row_number = 0
Col_number = 0


url = [r"C:\Users\a\Downloads\my-Github\Git_course"]
url2 = [r"C:\Users\a\Downloads\my-Github\Our_Project"]
url3 = ["https://github.com/nasrsaab/myFiles.git"]
url4 = ["https://github.com/nasrsaab/Git_course.git"]

for commit in Repository(path_to_repo=url, since=firstDay, to=toDay).traverse_commits():
    for modified_file in commit.modified_files:
        if Row_number != 5:
            df1 = pd.DataFrame([modified_file.filename, commit.msg, commit.author_date, commit.hash],
                               index=[0, 1, 2, 3, 4], columns=['File Name', 'Commit msg', 'Commit Date', 'hash'])
            Row_number += 1
        else:
            break


print(df1)
