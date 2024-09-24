import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sales_data_df = pd.read_csv('sales_data.csv')

sales_data_df['Revenue'] = sales_data_df['Quantity'] * sales_data_df['Price'] *(1 - sales_data_df['Discount'])

region_revenue = sales_data_df.groupby('Region')['Revenue'].sum().reset_index()

# plt.figure(figsize=(8, 6))
# sns.barplot(x='Region', y='Revenue', data=region_revenue)
# plt.title('Total Revenue per Region')
# plt.ylabel('Revenue')
# plt.xlabel('Region')
# # plt.show()


# category_revenue = sales_data_df.groupby('Category')['Revenue'].sum().reset_index()

# plt.figure(figsize=(8, 6))
# sns.barplot(x='Category', y='Revenue', data=category_revenue)
# plt.title('Total Revenue per Category')
# plt.ylabel('Revenue')
# plt.xlabel('Category')
# # plt.show()

# region_category_revenue = sales_data_df.groupby(['Region', 'Category'])['Revenue'].sum().unstack()

# region_category_revenue.plot(kind='bar', stacked=True, figsize=(10, 6))
# plt.title('Revenue by Region and Category')
# plt.ylabel('Revenue')
# # plt.show()

sales_data_df['Order_Date'] = pd.to_datetime(sales_data_df['Order_Date'])

sales_data_df['Month'] = sales_data_df['Order_Date'].dt.time



# monthly_revenue = sales_data_df.resample('M', on='Order_Date')['Revenue'].sum()

# plt.figure(figsize=(10, 6))
# plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
# plt.title('Monthly Revenue Over Time')
# plt.ylabel('Revenue')
# # plt.show()




# monthly_region_revenue = sales_data_df.groupby(['Region', pd.Grouper(key='Order_Date', freq='M')])['Revenue'].sum().unstack()

# plt.figure(figsize=(10, 6))
# for region in monthly_region_revenue.columns:
#     plt.plot(monthly_region_revenue.index, monthly_region_revenue[region], marker='o', label=region)

# plt.title('Monthly Revenue by Region')
# plt.ylabel('Revenue')
# plt.legend()
# # plt.show()

# 3.1 Histogram of Prices
# plt.figure(figsize=(8, 6))
# plt.hist(sales_data_df['Price'], bins=20, edgecolor='black')
# plt.title('Price Distribution')
# plt.xlabel('Price')
# plt.ylabel('Frequency')
# # plt.show()

# # 3.2 KDE plot for Revenue
# plt.figure(figsize=(8, 6))
# sns.kdeplot(sales_data_df['Revenue'], shade=True)
# plt.title('Revenue Distribution (KDE)')
# plt.xlabel('Revenue')
# # plt.show()

# 4.1 Scatter plot between Price and Revenue
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='Price', y='Revenue', data=sales_data_df)
# plt.title('Price vs Revenue')
# plt.show()

# # 4.2 Scatter plot with categories differentiated by color
# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='Price', y='Revenue', hue='Category', data=sales_data_df)
# plt.title('Price vs Revenue by Category')
# plt.show()

# 5.1 Heatmap for correlation between numerical features
plt.figure(figsize=(8, 6))
sns.heatmap(sales_data_df[['Price', 'Quantity', 'Revenue']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 5.2 Heatmap for revenue by Region and Category
region_category_revenue = sales_data_df.pivot_table(values='Revenue', index='Region', columns='Category', aggfunc='sum')

plt.figure(figsize=(10, 6))
sns.heatmap(region_category_revenue, annot=True, cmap='YlGnBu', fmt=".0f")
plt.title('Revenue Heatmap (Region vs Category)')
plt.show()






