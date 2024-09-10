import pandas as pd
import numpy as np



product_details = {
    'Product_ID': [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
    'Product_Description': ['High-end laptop', 'Smartphone', 'Office chair', 'Dining table', 'Running shoes', 
                            'Wireless headphones', 'Fitness tracker', 'Gaming console', 'Digital camera', 'Smartwatch'],
    'Supplier': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier A', 'Supplier D',
                 'Supplier E', 'Supplier F', 'Supplier G', 'Supplier H', 'Supplier B'],
    'Manufacturing_Date': pd.date_range(start="2022-01-01", periods=10, freq='ME')
}


product_df = pd.DataFrame(product_details)

product_df.to_csv("product_details.csv", index=False)


sales_data_df = pd.read_csv('sales_data.csv')


# print(sales_data_df.head().info())
# print(product_details_df.head().info())

# print(product_df.head())

# print(sales_data_df)


inner_join = pd.merge(sales_data_df,product_df, on='Product_ID' , how='inner')
# print(inner_join)


left_join = pd.merge(sales_data_df, product_df, on="Product_ID", how="left")
# print(left_join)

right_join = pd.merge(sales_data_df, product_df, on='Product_ID' , how= 'right')
# print(right_join)

outter_join = pd.merge(sales_data_df,product_df , on='Product_ID' , how= 'outer')
# print(outter_join)



sales_data_df['Revenue'] = sales_data_df['Quantity'] * sales_data_df['Price'] *(1 - sales_data_df['Discount'])


merged_df = pd.merge(sales_data_df, product_df, on="Product_ID", how='outer')

revenue_per_supplier = merged_df.groupby('Supplier')['Revenue'].sum()

# print(revenue_per_supplier)

sales_data_df['Product_ID']

products_per_supplier = merged_df.groupby('Supplier')['Product_ID'].count()
# print(products_per_supplier)


unsold_products = product_df[~product_df['Product_ID'].isin(sales_data_df['Product_ID'])]
# print(unsold_products)

region_sales_data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Sales_Goal': [5000, 7000, 6000, 8000]
}
region_sales_df = pd.DataFrame(region_sales_data)


sales_data_df['Region'] = np.random.choice(['North', 'South', 'East', 'West'], size=10)


merged_with_region = pd.merge(sales_data_df, region_sales_df, on="Region", how="left")
# print(merged_with_region)


new_sales_data = {
    "Order_ID": [11, 12],
    "Product_ID": [101, 102],
    "Product_Name": ["Laptop", "Phone"],
    "Category": ["Electronics", "Electronics"],
    "Quantity": [3, 2],
    "Price": [1200, 800],
    "Discount": [0.1, 0.2],
    "Revenue": [3000, 1600]
}

new_sales_df = pd.DataFrame(new_sales_data)


concatenated_sales = pd.concat([sales_data_df, new_sales_df], ignore_index=True)
print(concatenated_sales)




