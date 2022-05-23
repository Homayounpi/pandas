import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('t2.xlsx')
df['datetime']=pd.to_datetime(df['datetime'])
d=df[df['datetime'].dt.year==2020]
df['2020']=d.iloc[0:,5:6]
d=df[df['datetime'].dt.year==2021]
df['2021']=d.iloc[:,5:6]
#==============================
df['2020']=pd.to_datetime(df['2020'])
df['2021']=pd.to_datetime(df['2021'])
y20=df[df['2020'].dt.year==2020]
y21=df[df['2021'].dt.year==2021]

y20["dr_km"]=pd.cut(y20.dr_km,[0,5,10,15,100000],labels=['0_5','5_10','10_25','more 25'])
y21["dr_km"]=pd.cut(y21.dr_km,[0,5,10,15,100000],labels=['0_5','5_10','10_25','more 25'])
y21_grop=y21.groupby('dr_km').size().reset_index()
y20_grop=y20.groupby('dr_km').size().reset_index()
x20_=y20_grop['dr_km']
y20_=y20_grop.iloc[:,-1:]
x21_=y21_grop['dr_km']
y21_=y21_grop.iloc[:,-1:]
plt.plot(x20_,y20_)
plt.plot(x21_,y21_)
plt.legend(['2020','2021'],loc='best')
plt.show()




