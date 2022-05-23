import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
df=pd.read_excel('hl_df.xlsx')#Device_iid_hash
conect=sqlite3.connect('allStopNodes.db')
db=pd.read_sql("""SELECT * FROM sample1""",con=conect)
db['datetime']=pd.to_datetime(db['datetime'])
db['datetime']=db['datetime'].dt.weekday
df_db=db#uid
db=db.groupby('datetime').size().reset_index(name='week')
x=df_db[df_db['uid'].isin(df['Device_iid_hash'])]
x=x.groupby('datetime').size().reset_index(name='eshterak')
merg=db.merge(x,on='datetime')
print(merg.to_string())
pl=merg.plot(x='datetime',y=['week','eshterak'],kind='bar',figsize=(8,9))
plt.xticks([0,1,2,3,4,5,6],['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'])
plt.show()
























