from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

df = pd.read_csv('qj2.csv')
print(df)
print(df.dtypes)

# ## CREATE/GET DATA
# # The inital set of baby names and bith rates
# names = ['Bob','Jessica','Mary','John','Mel']
# births = [968, 155, 77, 578, 973]
#
# # merge lists together using zip function
# BabyDataSet = list(zip(names,births))
# print(BabyDataSet)
#
# df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
# print(df)
#
# df.to_csv('births1880.csv',index=False,header=False)
#
# #Notice the r before the string. Since the slashes are special characters, prefixing the string with a r will escape the whole string.
# Location = r'births1880.csv'
# df = pd.read_csv(Location)
# print(df)
#
# df = pd.read_csv(Location, names=['Names', 'Births'])
# print(df)
#
# # delete csv file
# # import os
# # os.remove(Location)
#
# ## PREP DATA
# # Check data type of the columns
# print(df.dtypes)
# # Check data type of Births column
# print(df.Births.dtype)
#
# ## ANALYZE DATA
# # Method 1 to find baby name with highest birth rate
# Sorted = df.sort_values(['Births'], ascending=False)
# print(Sorted)
# print(Sorted.head(1))
# # Method 2
# print(df['Births'].max())
#
# ## PRESENT DATA
# # Create graph
# plt.plot(df['Births'])
# plt.ylabel('Number of Births')
# plt.xlabel('Name')
# # Maximum value in the data set
# MaxValue = df['Births'].max()
# # Name associated with the maximum value
# MaxName = df['Names'][df['Births'] == df['Births'].max()].values
# # Text to display on graph
# Text = str(MaxValue) + " - " + MaxName
# # Add text to graph
# plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
# plt.title('Birth Name Frequencies')
# #Sorted.head(1) can also be used
# plt.savefig('birth.png')
