import pandas as pd
import numpy as np

# file = r"C:\Users\Divya\Downloads\Yahoo finance mapping - top3_stock_search_results_in_parallel.csv"
data = r"C:\Users\Divya\Downloads\Yahoo data divyansh.csv"
# db = r"C:\Users\Divya\Downloads\Yahoo finance database.csv"

# df = pd.read_csv(file)
dfdata = pd.read_csv(data)
# dfdb = pd.read_csv(db)


# Example function to convert financial values
def convert_financial_value(val):
    if isinstance(val, str):
        val = val.strip().upper().replace(',', '')
        if val.endswith('T'):
            return float(val[:-1]) * 1e12
        elif val.endswith('B'):
            return float(val[:-1]) * 1e9
        elif val.endswith('M'):
            return float(val[:-1]) * 1e6
        elif val == '--':
            return np.nan
    try:
        return float(val)
    except:
        return np.nan

dfdata['Revenue_TTM'] = dfdata['Revenue_TTM'].apply(convert_financial_value)
dfdata['db_revenue'] = dfdata['db_revenue'].apply(convert_financial_value)

# Preview results
print(dfdata[['Revenue_TTM', 'db_revenue']].head())


print(dfdata)

out = r"C:\Users\Divya\Downloads\divyansh_converted_1.csv"

# print("data ", dfdata.columns)
dfdata.to_csv(data, index=False)