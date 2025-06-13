import pandas as pd

sheet_path = r"C:\Users\Divya\Downloads\China expansion - KeyValues(1-500).csv"
dest_path =r'.\data\exp'

df = pd.read_csv(sheet_path)

print(df['Metric Heading'].unique())

for i in range(len(df)):
    if isinstance(df.at[i,'Metric Heading'], str):
        pass

df.to_csv(dest_path, index=False)
