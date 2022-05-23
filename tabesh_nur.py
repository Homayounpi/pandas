import numpy as np
import pandas as pd
df_irradiation=pd.read_excel('irradiation11.xlsx')
df_irradiation['Value']=df_irradiation['Value'].astype('int64')
df_irradiation['CreationDate']=pd.to_datetime(df_irradiation['CreationDate'])
df_main=df_irradiation[['CreationDate']]
df_irradiation=df_irradiation[(df_irradiation['Value']==0) & (df_irradiation['Value']==df_irradiation['Value'].shift(1))&(df_irradiation['Value'].shift(1)==df_irradiation['Value'].shift(2))&(df_irradiation['Value'].shift(2)==df_irradiation['Value'].shift(3))&(df_irradiation['Value'].shift(3)==df_irradiation['Value'].shift(4))&(df_irradiation['Value'].shift(4)==df_irradiation['Value'].shift(5)) ]
df_activePower=pd.read_excel('activePower.xlsx')
df_activePower['CreationDate']=pd.to_datetime(df_activePower['CreationDate'])
df_activePower=df_activePower[df_activePower['Value']>=0]
activePowerStart=df_activePower['CreationDate'].min()
activePowerEnd=df_activePower['CreationDate'].max()
max_1=df_irradiation[df_irradiation['CreationDate']>activePowerStart]
max_1=max_1['CreationDate'].agg(np.min)
min_1=df_irradiation[df_irradiation['CreationDate']<activePowerEnd]
min_1=min_1['CreationDate'].agg(np.max)
endIrradition=df_main.iloc[df_main.index[df_main['CreationDate']==max_1].to_list()[0]-6].iloc[0]
startIrradition=df_main.iloc[df_main.index[df_main['CreationDate']==min_1].to_list()[0]+1].iloc[0]
df_end=pd.DataFrame({'start Production':[activePowerStart],'end Production':[activePowerEnd], 'start irradiation':[startIrradition],'end irradiation':[endIrradition]})
print(df_end.to_string())

