import git_parser
import argparse

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


git_parser.show_commit(args)
