import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conection=sqlite3.connect('impressions.db')
df=pd.read_sql("SELECT * FROM sample1",con=conection)
id=df.groupby("device_id").size().reset_index(name='count')
count_in=id.groupby('count').size().reset_index(name='count_1')
plo_t=count_in.plot(x='count',y='count_1',kind='bar')
plt.show()
x=pd.Series([4,5,6,7],index=['a','b','c','d'])#
# print(x.values)
# print(x.index)
print(x.to_string())
