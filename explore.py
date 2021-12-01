import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('bored_apes.csv', parse_dates=['SaleDate']).rename(columns={'index': 'TokenId'})

print(df.head(10))

date_map = df[['TokenId', 'SaleDate']].groupby(pd.Grouper(key='SaleDate', freq='30D')).agg({'TokenId': list}).to_dict(orient='index')

date_map_formatted = {}
for i, date in enumerate(date_map):
    date_map_formatted[str(i+1)] = date_map[date]['TokenId']

def find_date_group(token_id, map):
    for k in map:
        if token_id in map[k]:
            return k
    return 'NaN'

df['DateGroup'] = 'NaN'
df['DateGroup'] = df.apply(lambda x: find_date_group(x['TokenId'], date_map_formatted), axis=1)

print(df)

ax = sns.boxplot(x="DateGroup", y="LastSalePrice", data=df)

print(df.describe())
