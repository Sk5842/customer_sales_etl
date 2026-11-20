import pandas as pd

df=pd.read_csv("output/customers_sales_summery.csv")

df['sales_ranking']=df["amount"].rank(method="dense",ascending=True)

print(df)

df.to_csv("output/customer_sales_ranked.csv")