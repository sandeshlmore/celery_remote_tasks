import pandas as pd

df = pd.read_csv('/home/sandeshmore/Desktop/Retailigence/data/pandas/pandas_poultry/category_poultry/Item_recommendation_output/cluster_stores5_rank1_item_recommendation_output/Rx_Items_Lost_Sales.csv')
df = df[(df['Store'] == 5)]
print(df['Rx_Item/Actual_Item'].nunique())
print(df.shape)
print(df.groupby('Rx_Item/Actual_Item').nunique())