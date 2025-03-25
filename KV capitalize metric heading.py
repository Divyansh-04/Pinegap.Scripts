import pandas as pd

sheet_path = r"C:\Users\Divya\Downloads\Europe - Germany - KeyValues.csv"
df = pd.read_csv(sheet_path)

print(df['Metric Heading'])

for i in range(len(df)):
    if isinstance(df.at[i,'Metric Heading'], str):
        df.at[i, 'Metric Heading'] = ' '.join(df.at[i, 'Metric Heading'].title().split())

df.to_csv(r'.\data\updated KV.csv', index=False)