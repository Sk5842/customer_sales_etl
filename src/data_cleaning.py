import pandas as pd

df=pd.read_csv("data/customer_dirty.csv")

df['city']=df['city'].fillna('unkown')
df['name']=df['name'].fillna('missing name')
df['email']=df['email'].fillna("noemail@gmail.com")
df['name']=df['name'].str.strip()

df.to_csv("output/cleaned_customers.csv",index=False)

print("Data cleaned sucessfully")


