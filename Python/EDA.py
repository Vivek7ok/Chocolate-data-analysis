import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_sales = pd.read_csv("D:\\Data_set\\Data_set_14\\Data\\sales.csv")
df_customers = pd.read_csv("D:\\Data_set\\Data_set_14\\Data\\customers.csv")
df_calendar = pd.read_csv("D:\\Data_set\\Data_set_14\\Data\\calendar.csv")
df_product = pd.read_csv("D:\\Data_set\\Data_set_14\\Data\\products.csv")
df_stores = pd.read_csv("D:\\Data_set\\Data_set_14\\Data\\stores.csv")

df_sales = df_sales.rename(columns={'order_date':'date'})

df = df_sales.merge(df_customers,on='customer_id',how='left')
df = df.merge(df_calendar,on='date',how='left')
df = df.merge(df_product,on='product_id',how='left')
df = df.merge(df_stores,on='store_id',how='left')

print(df_sales.columns)
print(df_customers.head())
print(df_calendar.head())
print(df_product.head())
print(df_stores.head())

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.columns)


sns.barplot(data=df,x='category',y='revenue',estimator=np.sum,hue='country')
plt.show()
#show the revenue by category to find out most selling category and whcih country are the most buying the catgeroy

sns.barplot(data=df,x='country',y='revenue',estimator=np.sum,hue='gender')
plt.show()
#show the revenue by category to find out most selling category and whcih gender are the most buying the catgeroy

sns.lineplot(data=df,x='year',y='revenue',estimator=np.sum)
plt.show()
#show total revenue by year

df.groupby('year')['order_id'].count().plot(kind='line')
plt.show()
#show every year number of order

sns.countplot(data=df,x='loyalty_member',hue='country')
plt.show()
#show the how many layaltly member are in every country
