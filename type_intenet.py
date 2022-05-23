import pandas as pd
df=pd.read_csv('ChurnData.csv')
# df.to_excel('ChurnData.xlsx')
df=df[df['churn']==1]
del df['churn']
df['loglong']=df['loglong'].astype('int64')
df['logtoll']=df['logtoll'].astype('int64')
df['lninc']=df['lninc'].astype('int64')
li_max=[]
li_min=[]
def max_min(x):
    df_m=pd.DataFrame({'value':x})
    li_max.append(df_m['value'].max())
    li_min.append(df_m['value'].min())
z=df.apply(lambda x:max_min(x))
def type_(z):
    if z<3:
        return 'type_x<3'
    elif (z>=3)&(z<6):
        return 'type_3<x<6'
    elif (z>=6)&(z<10):
        return 'type_5<x<10'
    elif (z>=10)&(z<20):
        return 'type_10<x<20'
    elif (z>=20)&(z<30):
        return 'type_20<x<30'
    elif (z>=30)&(z<40):
        return 'type_30<x<40'
    elif (z>=40)&(z<50):
        return 'type_40<x<50'
    elif (z>=50)&(z<60):
        return 'type_50<x<60'
    elif (z>=60)&(z<70):
        return 'type_60<x<70'
    elif (z>=70)&(z<80):
        return 'type_70<x<80'
    elif (z>=80)&(z<90):
        return 'type_80<x<90'
    elif (z>=90)&(z<100):
        return 'type_90<x<100'
    elif (z>=100)&(z<150):
        return 'type_100<x<150'
    elif (z>=150)&(z<200):
        return 'type_150<x<200'
    elif (z>=200)&(z<250):
        return 'type_200<x<250'
    elif (z>=250)&(z<300):
        return 'type_250<x300'
    elif (z>=300)&(z<600):
        return 'type_300<x<600'
    elif (z>=600)&(z<900):
        return 'type_600<x<900'
    elif (z>=900)&(z<1200):
        return 'type_900<x<1200'
    elif (z>=1200)&(z<1600):
        return 'type_1200<x<1600'
    elif (z>1600)&(z<2000):
        return 'type_1600<x<2000'
    else:
        return 'type_x>2000'
def loglong(z):
    if z==0:
        return 'type_x=0'
    elif z==1:
        return 'type_x=1'
    elif z==2:
        return 'type_x=2'
    elif z==3:
        return 'type_x=3'
    elif z==4:
        return 'type_x=4'
    elif z==5:
        return 'type_x=5'
    elif z==6:
        return 'type_x=6'
    elif z==7:
        return 'type_x=7'
    elif z==8:
        return 'type_x=8'
    elif z==9:
        return 'type_x=9'
    else:
        return 'type_x>10'
def income(z):
    if z<=25:
        return 'type_25<'
    elif (z>25)&(z<=50):
        return 'type_25<x<50'
    elif (z>50)&(z<=100):
        return 'type_50<x<100'
    elif (z>100)&(z<=150):
        return 'type_100<x<150'
    elif (z>150)&(z<=200):
        return 'type_150<x<200'
    elif (z>200)&(z<=300):
        return 'type_200<x<300'
    elif (z>300)&(z<=400):
        return 'type_300<x<400'
    elif (400<z)&(z<=500):
        return 'type_400<x<500'
    else:
        return 'x>500'
df['tenure']=df['tenure'].apply(lambda x:type_(x))
df['age']=df['age'].apply(lambda x:type_(x))
df['address']=df['address'].apply(lambda x:type_(x))
df['income']=df['income'].apply(lambda x:income(x))
df['ed']=df['ed'].apply(lambda x:loglong(x))
df['employ']=df['employ'].apply(lambda x:type_(x))
df['longmon']=df['longmon'].apply(lambda x:type_(x))
df['tollmon']=df['tollmon'].apply(lambda x:type_(x))
df['equipmon']=df['equipmon'].apply(lambda x:type_(x))
df['cardmon']=df['cardmon'].apply(lambda x:type_(x))
df['wiremon']=df['wiremon'].apply(lambda x:type_(x))
df['longten']=df['longten'].apply(lambda x:type_(x))
df['tollten']=df['tollten'].apply(lambda x:type_(x))
df['cardten']=df['cardten'].apply(lambda x:type_(x))
df['loglong']=df['loglong'].apply(lambda x:loglong(x))
df['logtoll']=df['logtoll'].apply(lambda x:loglong(x))
df['lninc']=df['lninc'].apply(lambda x:loglong(x))
df['custcat']=df['custcat'].apply(lambda x:loglong(x))
li_type=[]
li_darsad=[]
li_count=[]
def group_by(ser):
    df_m=pd.DataFrame({'value':ser})
    df_m=df_m.groupby('value').size().reset_index(name='count')
    df_m=df_m.sort_values(['count'],ascending=False)
    x=sum(df_m['count'])
    li_type.append(df_m['value'].iloc[0])
    li_darsad.append(((df_m['count'].iloc[0])/x)*100)
    li_count.append(df_m['count'].iloc[0])
    # li_count.append(df_m['count'].iloc[0])
x=df.apply(lambda x:group_by(x))
df_plt=pd.DataFrame({'naeme':df.columns,'type':li_type,'darsad':li_darsad,'count':li_count,'max':li_max,'min':li_min})
print(df_plt)



