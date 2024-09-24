import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sales_data_df = pd.read_csv('sales_data.csv')


sales_data_df['Revenue'] = sales_data_df['Quantity'] * sales_data_df['Price'] * (1 - sales_data_df['Discount'])

# print(sales_data_df.info())
# print(sales_data_df.describe())


# print(sales_data_df['Region'].value_counts())
# print(sales_data_df['Category'].value_counts())

missing_values = sales_data_df.isnull().sum()
print(missing_values)

sales_data_df = sales_data_df.drop_duplicates()


# plt.figure(figsize=(10, 6))
# sns.histplot(sales_data_df['Price'], kde=True)
# plt.title('Price Distribution')
# plt.show()


# plt.figure(figsize=(10, 6))
# sns.countplot(x='Region', data=sales_data_df)
# plt.title('Distribution of Sales by Region')
# plt.show()


# print(sales_data_df[['Price', 'Quantity', 'Revenue']].describe())

# plt.figure(figsize=(8, 6))
# sns.scatterplot(x='Price', y='Revenue', data=sales_data_df)
# plt.title('Price vs Revenue')
# plt.show()


# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Category', y='Price', data=sales_data_df)
# plt.title('Price Distribution by Category')
# plt.show()


# plt.figure(figsize=(8, 6))
# sns.heatmap(sales_data_df[['Price', 'Quantity', 'Revenue']].corr(), annot=True, cmap='coolwarm')
# plt.title('Correlation Heatmap')
# plt.show()


sales_data_df['Order_Date'] = pd.to_datetime(sales_data_df['Order_Date'])


monthly_revenue = sales_data_df.resample('M', on='Order_Date')['Revenue'].sum()

# plt.figure(figsize=(10, 6))
# plt.plot(monthly_revenue.index, monthly_revenue.values, marker='o')
# plt.title('Monthly Revenue Over Time')
# plt.ylabel('Revenue')
# plt.show()

# 4.3 Year-over-Year (YoY) Growth
sales_data_df['Year'] = sales_data_df['Order_Date'].dt.year
yearly_revenue = sales_data_df.groupby('Year')['Revenue'].sum()
yoy_growth = yearly_revenue.pct_change() * 100

print('Year-over-Year Revenue Growth:')
# print(yoy_growth)


# 5.1 Box plot for detecting outliers in Price
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Price', data=sales_data_df)
plt.title('Price Outliers by Category')
plt.show()

# 5.2 IQR method to detect outliers in Price
Q1 = sales_data_df['Price'].quantile(0.25)
Q3 = sales_data_df['Price'].quantile(0.75)
IQR = Q3 - Q1
outliers = sales_data_df[(sales_data_df['Price'] < (Q1 - 1.5 * IQR)) | (sales_data_df['Price'] > (Q3 + 1.5 * IQR))]

print('Outliers in Price:')
# print(outliers)

# 6.1 Pair plot for numerical variables
sns.pairplot(sales_data_df[['Price', 'Quantity', 'Revenue', 'Discount']])
plt.show()

# 6.2 Violin plot for Price across different Categories
plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Price', data=sales_data_df)
plt.title('Violin Plot: Price Distribution by Category')
plt.show()

# 6.3 FacetGrid for Region-based plots
g = sns.FacetGrid(sales_data_df, col='Region', col_wrap=3, height=4)
g.map(sns.histplot, 'Revenue')
g.set_titles('{col_name}')
