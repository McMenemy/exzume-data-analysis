from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

df = pd.read_csv('qj2.csv')
df.rename(columns={"Overall, I am satisfied with how I did today." : "Satisfaction",
                   "I moved closer to becoming my ideal self." : "Ideal Self",
                   "I felt in control of my day." : "Control",
                   "I was productive today." : "Productivity",
                   "I experienced a lot of stress today." : "Stress",
                   "Briefly describe your day and your thoughts." : "Thoughts",
                   "Did any unusual circumstances occur today that might of had a significant influence on your results?" : "Unusual Day",
                   "How many times did you have sex?" : "Sex",
                   "How many times did you masturbate?" : "Masturbation",
                   "How many mg of caffeine did you have today? (1 cup of coffee is about 200mg, 1 cup of green tea is about 70mg, 1 cup of black tea is about 120mg, 1 can of coke is about 35 mg)" : "Caffeine",
                   "How many standard drinks of alcohol did you have? (1 standard drink is a shot of liquor, can of beer, or glass of wine)" : "Alcohol",
                   "How many grams of weed did you smoke?" : "Weed",
                   "How many minutes did you meditate today?" : "Meditation",
                   "How many minutes did you play video games today?" : "Video Games",
                   "How many minutes did you watch TV today?" : "TV",
                   "Did you visually plan your day the night before?" : "Planning",
                   "List three things you are grateful for today." : "Gratitude",
                   "About how many minutes did you spend socializing today?" : "Social",
                   "About how many of these minutes socializing were spent with close friends or family?" : "Social Close",
                   "Overall, I was satisfied with my social time today." : "Social Satisfaction",
                   "Overall, I feel this social time helped me build or strengthen supportive and rewarding relationships." : "Social Building",
                   "I contributed to the well being or happiness of someone else today." : "Helping Others",
                   "Briefly describe your social time today." : "Social Thoughts",
                   "About how many minutes did you spend working today? (minutes)" : "Work",
                   "The time I spent working today moved me closer to my long-term goals." : "Work Goals",
                   "I worked on something important to me today." : "Work Important",
                   "Briefly describe your work time today." : "Work Thoughts",
                   "About how many minutes did you spend relaxing today? (minutes)" : "Relaxation",
                   "About how many minutes did you spend doing physical activities today?" : "Exercise" }, inplace=True)
print(df)
print(df.dtypes)
print df.style

print df.describe()
print df.corr()
# print df.cov()
# print df[['Productivity','Control']].corr()

# def f(x):
#     return (x[3]/7 + x[24]/420 + x[29]/180) * x[4]
#     # - x[19]/240
# df['corr'] = df.apply(f, axis=1)
# plt.plot(df['corr'])
# plt.ylabel('Productivity')
# plt.xlabel('Time')
# # Maximum value in the data set
# MaxValue = df['Births'].max()
# # Name associated with the maximum value
# MaxName = df['Names'][df['Births'] == df['Births'].max()].values
# # Text to display on graph
# Text = str(MaxValue) + " - " + MaxName
# # Add text to graph
# plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.title('Josh: Productivity Over Time')
# #Sorted.head(1) can also be used
plt.savefig('productivity.png')


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
