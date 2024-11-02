import pandas

df0 = pandas.read_csv('data/daily_sales_data_0.csv', parse_dates=['date'])
df1 = pandas.read_csv('data/daily_sales_data_1.csv', parse_dates=['date'])
df2 = pandas.read_csv('data/daily_sales_data_2.csv', parse_dates=['date'])

df_list = [df0, df1, df2]
outputs = {'Sales': [], 'Date': [], 'Region': []}
num_outputs = 0
output_idx = []

for df in df_list:
    rows = len(df)
    df['price'] = df['price'].replace('[$]', '', regex=True).astype(float)
    for i in range(rows):
        if df.at[i, 'product'] == 'pink morsel':
            outputs['Sales'].append(df.at[i, 'price'] * df.at[i, 'quantity'])
            outputs['Date'].append(df.at[i, 'date'])
            outputs['Region'].append(df.at[i, 'region'])
            output_idx.append(num_outputs)
            num_outputs += 1

output_df = pandas.DataFrame(data=outputs)
print(output_df)
output_df.to_csv('data/output.csv', index=False)