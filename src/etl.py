import pandas as pd

#extract
customers=pd.read_csv("data/customers.csv")
orders=pd.read_csv("data/orders.csv")

#tansform
marged= pd.merge(customers,orders,on='customer_id',how='inner')

summery=marged.groupby(["customer_id","name"])['amount'].sum()

#load
summery.to_csv('output/customers_sales_summery.csv',index=False)

print("ETL pipeline execuated sucessfully")