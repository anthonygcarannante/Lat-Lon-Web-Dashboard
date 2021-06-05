import pandas as pd
import os

cities_df = pd.read_csv("Resources/cities.csv",index_col=0)
cities_df.to_html('data3.html')

table=cities_df.to_html()
print(table)