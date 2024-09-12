import pandas as pd

sales_data_df = pd.read_csv('sales_data.csv')
productdf = pd.read_csv('product_details.csv')

null_on_sales = sales_data_df.isnull().sum()

nul_on_product = productdf.isnull().sum()

# print(f"{nul_on_product} \n {null_on_sales}")

sales_data_df['Revenue'] = sales_data_df['Quantity'] * sales_data_df['Price'] *(1 - sales_data_df['Discount'])


pivot_table = pd.pivot_table(sales_data_df, values='Revenue', index='Region', columns='Category', aggfunc='sum')
# print(pivot_table)


melted_df = sales_data_df.melt(id_vars=['Order_ID', 'Product_ID'], value_vars=['Quantity', 'Price', 'Revenue'])
# print(melted_df)


stacked_df = pivot_table.stack()
# print(stacked_df)

unstacked_df = stacked_df.unstack()
# print(unstacked_df)

sales_data_df['Discounted_Price'] = sales_data_df.apply(lambda x: x['Price'] * (1 - x['Discount']), axis=1)

# sales_data_df = sales_data_df.applymap(lambda x: round(x, 2) if isinstance(x, (float, int)) else x)

# print(sales_data_df.head())

sales_data_df['Order_Date'] = pd.to_datetime(sales_data_df['Order_Date'])


sales_data_df['Year'] = sales_data_df['Order_Date'].dt.year
sales_data_df['Month'] = sales_data_df['Order_Date'].dt.month
sales_data_df['Day_of_Week'] = sales_data_df['Order_Date'].dt.day_name()

# print(sales_data_df[['Order_Date', 'Year', 'Month', 'Day_of_Week']].head())


monthly_revenue = sales_data_df.resample('ME', on='Order_Date')['Revenue'].sum()
# print(monthly_revenue)

sales_data_df = sales_data_df.drop_duplicates()


sales_data_df['Category'] = sales_data_df['Category'].str.strip().str.lower().str.capitalize()


sales_data_df['Region'] = sales_data_df['Region'].str.strip().str.title()

print(sales_data_df.head())
