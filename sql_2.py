import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
red=pd.read_excel('t1.xlsx')
df=pd.DataFrame(red)
newdf=pd.cut(df.dr_km,[0,5,10,25,1000000],labels=['0to5','5 to 10','10 to 25',' more 25'])
cont=pd.DataFrame(newdf).groupby('dr_km').size().reset_index(name='count')
plt_1=cont.plot(x='dr_km',y='count',kind='bar')
#======================================================
red['time']=pd.to_datetime(red['leaving_datetime'])
c=red.groupby(red['time'].dt.day).size().reset_index(name='count')
print(c.plot(kind='bar'))
plt.show()































