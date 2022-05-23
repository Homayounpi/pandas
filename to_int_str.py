import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('33.csv')
y=df.shape[0]
df=df[df['Area'].str.isnumeric()]
df['Area']=df['Area'].astype('int64')
df['1']=df['Area']+1
df['Area']=pd.to_numeric(df['Area'],errors='coerce')
# =============================================================
plt.bar(['Parking','Warehouse','Elevator'],[df.groupby('Parking').agg(np.size).loc[True].iloc[1],df.groupby('Warehouse').agg(np.size).loc[True].iloc[1],df.groupby('Elevator').agg(np.size).loc[True].iloc[1]])
plt.show()

