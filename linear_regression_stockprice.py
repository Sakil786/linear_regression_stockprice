import torch
import pandas as pd

data=pd.read_csv('stock_price.csv')
print(data.shape)
print(data.columns.to_list())