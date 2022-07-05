import git_commit_v2
# importing pandas module...to create a data frame

import pandas as pd

'''
module for git commit file
'''
# import sys
# sys.path.append("D:\damka")
# print(sys.path)


url = input("Please enter your URL: ")
git_commit_v2.git_commit(url)
# https://github.com/nasrsaab/Our_Project.git
# https://github.com/nasrsaab/Git_course.git
'''open the xlsx file and put the data in dataframe '''
df_dataframe = pd.read_excel(r"E:\Python Examples\nvidia_git_proj\book2.xlsx")
df_dataframe.to_csv(r'E:\Python Examples\nvidia_git_proj\book2.csv')

# making data frame from csv file
df_dataframe = pd.read_csv(r'E:\Python Examples\nvidia_git_proj\book2.csv', index_col="File Name")

# print the dataframe
print(df_dataframe)