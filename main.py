import pandas as pd

# Example DataFrame (with some issues)
data = {
    "Product_Id": [101, 102, 103, 104, 105, 106],
    "Category": ["electronics", "clothing ", "Furniture", None, "Facny_items", "electronics"],
    "Price": [150, 80, 200, 300, None, 150],
    "stocks": [30, 100, 20, 15, 200, 30],
    "sales": [200, 150, 100, 50, 120, None]
}

df = pd.DataFrame(data)


missing_values = df.isnull().sum()

df['Price'].fillna(df['Price'].median(), inplace=True)


df.dropna(subset=['Category'], inplace=True)

df['Price'] = df['Price'].astype(float)
df['sales'] = df['sales'].astype(float)


df['Category'] = df['Category'].astype('category')

df['Category'] = df['Category'].str.strip().str.lower().str.capitalize()


df.drop_duplicates(inplace=True)


df.rename(columns={'stocks': 'Stock'}, inplace=True)


# print(df)
print(missing_values)