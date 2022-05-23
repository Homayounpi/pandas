import pandas as pd
df=pd.read_excel('sample_test.xlsx')
df['time']=pd.to_datetime(df['time'])
def ty(x):
    if (x.hour>=7) & (x.hour<=10)&(x.weekday()!=6)&(x.weekday()!=5):#
        return '1'
    elif (x.hour>=17) & (x.hour<=19) & ((x.weekday()!=5) &(x.weekday()!=6)):
        return '2'
    elif (x.hour >= 7) & (x.hour <= 10) & (x.weekday() == 6)|(x.weekday() == 5):
        return '3'
    elif (x.hour >= 17) & (x.hour <= 19) & ((x.weekday()== 5)|(x.weekday() == 6)):
        return '4'
    else:
        return '5'
df['type']=df.apply(lambda x:ty(x['time']),axis=1)
df['year']=df['time'].dt.year
df['month']=df['time'].dt.month
df['week_day']=df['time'].dt.weekday
df=df.groupby(['year','month','type']).size().reset_index(name='count')
print(df.to_string())




