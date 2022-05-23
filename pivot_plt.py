import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
conect=sqlite3.connect('impressions.db')
db=pd.read_sql("""SELECT * FROM sample1""",con=conect)
db=db[['sdk_ts','device_id']]
db['sdk_ts']=pd.to_datetime(db['sdk_ts'])
db['hour']=db['sdk_ts'].dt.hour
d=db.groupby([db['sdk_ts'].dt.weekday,db['hour'],db['device_id']]).size().reset_index(name='count')
d=d.groupby([d['sdk_ts'],db['hour']]).size().reset_index(name='count')
d.pivot(index='sdk_ts',columns='hour',values='count').plot(kind='bar',figsize=(15,9))
plt.xticks([0,1,2,3,4,5,6],['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'])
# plt.legend(['single element'])
# plt.legend(loc='lower left')
# plt.legend(ncol=4)
plt.legend(bbox_to_anchor=(1,1))
print(d.to_string())
plt.show()

































