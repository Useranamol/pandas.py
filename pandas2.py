import pandas as pd
import numpy as np

# Create a synthetic dataset
data = {
    "Order_ID": np.arange(1, 11),  # 10 orders
    "Product_ID": np.random.randint(100, 200, size=10),
    "Product_Name": np.random.choice(["Laptop", "Phone", "Chair", "Table", "Shoes"], size=10),
    "Category": np.random.choice(["Electronics", "Furniture", "Clothing"], size=10),
    "Sub_Category": np.random.choice(["Laptops", "Phones", "Chairs", "Tables", "Footwear"], size=10),
    "Quantity": np.random.randint(1, 5, size=10),
    "Price": np.random.uniform(50, 500, size=10),
    "Discount": np.random.uniform(0, 0.3, size=10),
    "Order_Date": pd.date_range(start="2023-01-01", periods=10, freq='D'),
    "Region": np.random.choice(["North", "South", "East", "West"], size=10),
    "Customer_Segment": np.random.choice(["Consumer", "Corporate", "Home Office"], size=10)
}

df = pd.DataFrame(data)


# print(df.head(10))


df.to_csv("sales_data.csv", index=False)

df = pd.read_csv("sales_data.csv")

df['Revenue'] = df['Quantity'] * df['Price'] * (1 - df['Discount'])

total_revenue = df['Revenue'].sum()




# print("Total revenue : $" , total_revenue)


average_price = df['Price'].mean()
min_price = df['Price'].min()
max_price = df['Price'].max()

# print(f"Average Price: {average_price}")
# print(f"Min Price: {min_price}")
# print(f"Max Price: {max_price}")

total_quantity_per_product = df.groupby('Product_Name')['Quantity'].sum()
# print(total_quantity_per_product)

category_group = df.groupby('Category').agg({
    'Revenue': 'sum',
    'Quantity': 'sum',
    'Discount': 'mean'
})

# print(category_group)

categorry_region = df.groupby('Region').agg({
    'Revenue' : 'sum',
    'Quantity' : 'sum'
})

# print(categorry_region)

customer_segment_category = df.groupby('Customer_Segment').agg({
    'Revenue' : 'sum',
    'Quantity' : 'sum'
}).sort_values(by= 'Revenue', ascending=False)

# print(customer_segment_category)

top_products = df.groupby(['Category', 'Product_Name']).agg({
    'Revenue': 'sum'
}).sort_values(by='Revenue', ascending=False).groupby('Category').head(3)

# print(top_products)

multi_agg = df.groupby(['Category']).agg({
    'Revenue' : [ 'sum' , 'mean' , 'median' , 'std'],
    'Quantity' : [ 'sum' , 'mean' , 'max']

})

# print(multi_agg)

Aggregration_products = df.groupby('Product_Name').agg({
    'Revenue' : 'sum',
    'Order_ID' : 'count',
    'Discount' : 'mean'

})
# print(Aggregration_products)

pivot_table_revenue = pd.pivot_table(df, values='Revenue', index='Region', columns='Category', aggfunc='sum')
# print(pivot_table_revenue)

df['Order_Date'] = pd.to_datetime(df['Order_Date'])


df['Month'] = df['Order_Date'].dt.month

pivot_table_quantity = pd.pivot_table(df, values='Quantity', index='Month', columns='Customer_Segment', aggfunc='mean')
# print(pivot_table_quantity)


monthly_sales = df.groupby('Month').agg({
    'Revenue': 'sum',
    'Quantity': 'sum'
})

# print(monthly_sales)

df['Year'] = df['Order_Date'].dt.year

yearly_sales = df.groupby('Year')['Revenue'].sum()
yearly_growth = yearly_sales.pct_change() * 100 

# print(yearly_growth)

def categorize_revenue(revenue):
    return 'High Revenue' if revenue > 500 else 'Low Revenue'

df['Revenue_Category'] = df['Revenue'].apply(categorize_revenue)

custom_grouping = df.groupby('Revenue_Category').agg({
    'Revenue': 'sum',
    'Quantity': 'sum'
})

# print(custom_grouping)

def categorize_revenue(revenue):
    return 'High Revenue' if revenue > 500 else 'Low Revenue'

df['Revenue_Category'] = df['Revenue'].apply(categorize_revenue)

custom_grouping = df.groupby('Revenue_Category').agg({
    'Revenue': 'sum',
    'Quantity': 'sum'
})

# print(custom_grouping)

different_agg = df.groupby('Category').agg({
    'Revenue': ['sum', 'mean'],
    'Quantity': ['sum', 'max']
})

# print(different_agg)

df['Cumulative_Revenue'] = df['Revenue'].cumsum()

print(df[['Order_Date', 'Revenue', 'Cumulative_Revenue']])



