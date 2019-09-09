import pandas as pd
import seaborn as sns

home_data = pd.read_csv(r'https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge-f2019/master/home_ownership_data.csv')
loan_data = pd.read_csv(r'https://raw.githubusercontent.com/McGillAISociety/mais-202-coding-challenge-f2019/master/loan_data.csv')

data = pd.merge(home_data, loan_data, on="member_id")
average = data.groupby(data.home_ownership).loan_amnt.mean()
average = average.reset_index()

figure = sns.barplot(x = 'home_ownership', y = 'loan_amnt', data = average, color = 'steelblue')
figure.set(xlabel='Home ownership', ylabel='Average loan amount ($)', title = 'Average loan amounts per home ownership')

average
