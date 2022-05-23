import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('t2.xlsx')
df['datetime']=pd.to_datetime(df['datetime'])
y20=df[df['datetime'].dt.year==2020]
y21=df[df['datetime'].dt.year==2021]
y20["dr_km"]=pd.cut(y20.dr_km,[0,5,10,15,100000],labels=['0_5','5_10','10_25','more 25'])
y21["dr_km"]=pd.cut(y21.dr_km,[0,5,10,15,100000],labels=['0_5','5_10','10_25','more 25'])
y21_grop=y21.groupby('dr_km').size().reset_index(name='2021')
y20_grop=y20.groupby('dr_km').size().reset_index(name='2020')
merg=pd.merge(y21_grop,y20_grop,on='dr_km')
merg.plot(x='dr_km',y=['2021','2020'],kind='bar')
plt.show()



















