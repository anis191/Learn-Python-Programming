# we install various python library or packages using "pip"
'''
Go to terminal:-
command for pandas --> pip install pandas
command for openpyxl --> pip install openpyxl
'''
# import any library or files in python code, Syntax --> import (library_name)
import pandas # for short cut --> import pandas as pd
df = pandas.read_excel("file_example_XLSX_10.xlsx") #this is pandas syntax
print(df)