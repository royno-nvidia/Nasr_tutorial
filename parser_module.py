import git_parser
# importing pandas module...to create a data frame

import pandas as pd

'''
module for git commit file
'''


url = input("Please enter your URL: ").strip()
git_parser.show_commit(url)
# https://github.com/nasrsaab/Our_Project.git
# https://github.com/nasrsaab/Git_course.git


'''open the xlsx file and put the data in dataframe '''
df_dataframe = pd.read_excel('Excel_File1.xlsx')

# print the dataframe
print(df_dataframe)