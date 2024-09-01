import pandas as pd

data = {
    "Product_Id" : [101 , 102,  103 , 104 , 105 ],
    "Category"  : [ "electronics" , "clothing ", "Furniture" , "Groceris","Facny_items"],
    "Price" : [ 150 , 80 , 200 , 300 , 50],
    "stocks" : [ 30 ,100 , 20 , 15 , 200],
    "sales" : [ 200 , 150, 100, 50 , 120]

 }

df = pd.DataFrame(data)

head = df.head(10)
sub_set = df[["Product_Id" , "Price"]]
df.set_index( "Product_Id" , inplace = True)

# print(head)
# print(sub_set)
# Filter by Category
electronics = df[df['Category'] == 'Electronics']

# Filter by Price
expensive_products = df[df['Price'] > 100]

# Display the results
print(electronics)
print(expensive_products)

df.reset_index(inplace= True)

df.iloc[ :5 , :3]
# Display the results



print(sub_set)