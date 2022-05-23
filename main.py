import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
# df=pd.read_excel('Book1.xlsx')
# print(df[df['id']>5])
#=================================
# v=pd.DataFrame({"name":["ali","mmad","hasan"],'age':[22,23,24],"city":["tehran","tehran","semnan"]})
# print(v)
# print(v.describe())
#=================================
# x=pd.Series([22,34,23],name="age")
# print(x.describe())
#====================================
# s=pd.Series(np.random.rand(10))
# s[::2]=np.nan
# print(s.describe())
# print(s)
#======================================
# x=pd.DataFrame(np.random.rand(10,5),columns=["a","b",'c',"d","e"])
# print(x)
# print(x.describe())
# c=pd.DataFrame(["a","a","a","b","b","b",np.nan,"b"]).describe()
# print(c)
#=============================
# x=pd.DataFrame({"name":["ali","mmad","hasan"],'age':[12,13,14]})
# print(x.describe(include="all"))#include=object,number\
#==============================================================
# x=pd.Series(np.random.randn(5))
# print(x.idxmax(),x.idxmin())
#=======================================
# x=pd.DataFrame(np.random.randn(5,3),columns=['a','b','c'])
# print(x.idxmin(),x.idxmax(),sep="\n")
#============================================
# x=pd.DataFrame(np.random.rand(5,3),columns=["a","b","c","d"])
# print(x.idxmax(axis=0))
# print(x.idxmin(axis=1))
#=========================================
# df=pd.read_excel('Book1.xlsx')
# print(df.head(2),df.tail(),sep="\n")
#-==========================================
# df=pd.read_excel('Book1.xlsx')
# # x=df.assign(taghsim=df["sepallenght"]/df["sepalwidyh"])
# # y=df.assign(mmad=lambda x:x["sepallenght"]/x["sepalwidyh"])
# print(x)
# # print(y)
# df['divi']=df["sepallenght"]/df["sepalwidyh"]
#=======================================================================================
# x=pd.read_excel("sub.xlsx")
# print(x.count())
# df = x.dropna(how='any',axis=0)
# print(df)
#==========================================================================================
# x=pd.read_excel("sub.xlsx")
# z=x.query("Value==0 ")
# print(z)
# c=x.query("Value ==0").assign(ali=lambda d:d["Value"]/2)
# print(c)
#==============================================================
# x = pd.read_excel("Book1.xlsx")
# c=x.plot(x="A",y="B")
# print(c)
# c=x.to_csv("csv")
# print(c)
#====================================
# x=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
# c=x.assign(c=lambda x:x["A"]+x["B"],D=lambda r:r["c"]+r["A"])
# print(c)
# d=x.iloc[1:3:2]
# print(d)
#==============================================
# x=pd.read_excel("Book1.xlsx")
# d=x[x['A']==4.5]
# print(d)
#==================================
# x=pd.read_excel("sub.xlsx",na_values={"EquipmentName":["Measurement Sub1"],"Value":[0]})
# c=[0,"Measurement Sub1"]
# d=pd.read_excel("sub.xlsx",na_values=c)
# print(x)
# print(d)
#===============================================
# c=[0]
# x=pd.read_excel("sub.xlsx",na_values=c)
# v=x.dropna(axis=0,how='any',inplace=False)
# print(v)
# print(x)
#==================================================
# x=pd.read_excel('Book1.xlsx')
# c=x["A"].fillna(1)#x['A'].median,inplace=False
# print(c)
# c=x["A"].fillna(method="ffill")
# print(c)
#=====================================
# x=pd.read_excel("Book1.xlsx")
# print(x.shape)
# d=x[["A","B"]]
# print(d)
#=============================
# x=[1,2,3,4]
# y=[1,2,3,4]
# h=plt.plot(x,y)
# plt.savefig('foo.png')
# x=pd.read_excel("Book1.xlsx")
# v=plt.plot(x["A"],x["B"])
# plt.savefig('fo1.png')
#===========================
# x=pd.read_excel("Book1.xlsx")
# c=x[x["A"]>4.4]
# print(c)
# s=x[x["A"].isin([4,5.1])]
# print(s)
#===========================
# x=pd.read_excel("Book1.xlsx")
# c=x[x["A"].notna()]
# print(c)
#=========================================
# x=pd.read_excel("Book1.xlsx")
# c=x.loc[x['A']>4.5,"B"]
# print(c)
# print(c.index)
#============================
# x=pd.read_excel("Book1.xlsx")
# v=x[x["A"].notna()]
# print(v)
#======================================
# x=pd.read_excel("Book1.xlsx")
# v=x.to_csv('test.csv',index=False)
# v.to_excel
# print(x)
#==========================================
# data={"TEAM":['A','B','C','D','E','F','G','H'],
#       "Rank":[1,2,2,3,1,4,2,3],
#       "YEAR":[2014,2015,2014,2020,2019,2018,2012,2020],
#       'POINTS':[897,789,650,770,900,820,670,699]}
# df=pd.DataFrame(data)
# c=df.style.hide_index()
# print(df.to_string(index=False))
# x=df.groupby("TEAM").groups#groupby(["TEAM","RANK",'YEAR'])
# print(x)
# c=df.groupby("YEAR")
# for i,j in c:
#       print(i,j,sep=' ## \n')
# v=c.get_group(2014)["Rank"]
# print(v)
#print(c)
# w=c['POINTS'].agg(np.mean)#np.size
# print(w)
# scor=lambda x:(x+x.mean())/2
# t=c.transform(scor)
# print(t)
# g=c.filter(lambda x:len(x)>=2)
# print(g)
#===============================================================
# data_scatt={"U":[1,2,3,4],"S":[1,2,3,4]}
# c=pd.DataFrame(data_scatt)#columns=['un',"st"]
# print(c)
# d=c.plot(x='U',y='S',kind='scatter')
# plt.show()
#===============================================
# x={'A':["a","b","c"],"B":[34,45,21]}
# s=pd.DataFrame(x)
# p=s.plot(x='A',y='B',kind='bar')#kind=scatter or line
# plt.show()
#=================================================================
# data={"Task":[40,30,70]}
# x=pd.DataFrame(data,index=["AA","BB","CC"])#
# x=x.plot.pie(y='Task',figsize=(5,5),autopct='%1.1f%%',startangle=20)#
# plt.show()
# print(x)
#========================================================
# x={'date':['AA','AA','AA','BB','BB','BB','BB','BB','CC','CC','CC'],'type':['A','B','C','A','B','C','B','A','B','B','c'],'sales':[1000,300,200,400,1000,700,200,300,700,400,500]}
# df=pd.DataFrame(x)#,columns=['date','type','sales']
# v=df.groupby(['date','type']).groups
# print(pd.DataFrame(v))
# pl=df.plot(x='date',y='sales',kind='bar')
# plt.show()
#================================================
# red=pd.read_excel('Book1.xlsx')
# df=pd.DataFrame(red)
# df['T']=df["A"]/df['B']
# df=df.rename(columns={"A":'mmad'})
# #print(df.mean())
# # print(df['B'].mean())
# # print(df[["B",'C']].mean())
# all_1=df.agg({"C":["mean","max","min"],"B":['mean','max','min']})
# # print(all_1)
# #print(df)
# m_1=df[['C','B']].groupby('B').mean()
# # print(m_1)
# mn=df.groupby('B')['mmad'].mean()
# # print(mn)
# c=df.groupby('E').mean()
# print(c)
#====================================================
# re=pd.read_excel('Book1.xlsx')
# df=pd.DataFrame(re)
# gr=df['A'].value_counts(dropna=False)
# # print(gr)
# sor=df.sort_values(by=['B','A'],ascending=False)
# print(sor)
#===================================================
# df=pd.read_excel('impressions.xlsx',index_col='device_id',parse_dates=True)
# df=pd.DataFrame(df)
# print(pd.DataFrame(df))
# po=df.pivot(columns='',values=)
#=====================================
# df=pd.read_excel('impressions.xlsx',index_col='device_id')
# df=pd.DataFrame(df)
# df=df[df['device_os']=='ios']
# print(df.reset_index())
#pot=df.pivot(columns='device_id',values='accuracy')
# print(pot)
# pivot_table=df.pivot_table(index='sdk_ts',values='device_id',columns='device_os',aggfunc='mean')#
# print(pivot_table)

#=======================================
# read=pd.read_excel('sub.xlsx')
# df=pd.DataFrame(read)

# not_Nan=df.dropna(axis=0,how='any')
# zero=not_Nan[not_Nan['Value']==0]
# x=zero.groupby("EquipmentName").size().reset_index(name='COUNT')
# ft=not_Nan.groupby('Value')
# #print(x)
# pl=x.plot(x='EquipmentName',y='COUNT',kind='bar')
# plt.show()
#===============================================
# read=pd.read_excel('sub.xlsx')
# df=pd.DataFrame(read)
# t1=df[df['Value']==0 ]
# t1=t1[t1['EquipmentName']=='Measurement Sub6']
# t1=t1.groupby('CreationDate').size().reset_index(name='count')
# # f=t1[['Value','ParameterName','EquipmentName']].agg(np.size)#tamrinnnn
# d=t1.to_excel("sub_1.xlsx")
# print(d)
#===================================
# df1=pd.DataFrame({'key':['k0','k1','k2','k3','k4','k5'],"A":['A0','A1','A2','A3','A4','A5']})
# df2=pd.DataFrame({'key':['k0','k1','k2'],"B":['B0','B1','B2']})
# join_1=df1.join(df2.set_index('key'),on='key')#,lsuffix='_caller',rsuffix='_other'
# print(join_1)
# dfm1=pd.DataFrame({'1key':["A","B","C","f"],'value':[1,2,3,4]})
# dfm2=pd.DataFrame({'rkey':["A","B","C","D"],'value':[4,5,6,7]})
# mr=dfm1.merge(dfm2,left_on='1key',right_on='rkey')
# print(mr)
#===============================================================
# red=pd.read_excel('impressions.xlsx')
# red=pd.DataFrame(red)
# red=red.iloc[:20,:5]
# red=red.rename(columns={'sdk_ts':'time'})
# red['time']=pd.to_datetime(red['time'])
# print(red['time'])
# max_1=red['time'].max()
# min_1=red['time'].min()
# print(max_1,min_1,sep='\n')
# print(max_1-min_1)
# red['month']=red['time'].dt.month#month,weekday,day,year
# # print(red)
# day=red.groupby([red['time'].dt.week,'device_id'])
# print(day.groups)
#================================
# re=pd.read_excel('impressions.xlsx')
# re=pd.DataFrame(re)
# # print(re['device_make'].str.lower())
# re['fname']=re['device_carrier'].str.split(';').str.get(0)
# # print(re['fname'])
# mr=re['device_os'].str.contains('ios')
# fil=re[mr]
# # print(fil)
# len_max=re['device_id'].str.len()
# # print(len_max)
# lo_c=re.loc[re['device_id'].str.len()]
# # print(lo_c)
# re['device_os']=re['device_os'].replace({'Android':'mmad'})
# print(re.to_string())
#================================================
# x=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]},index=['111','222','333'])
# print(x)
#=========================================================
# xx=[0,10,2'0]
# yy=[30,40,50]
# cc=["A","B","C"]
# coler=['blue','green','pink']
# size=np.ar'ray([210,410,510])
# c=plt.plot(yy,xx)
# c=plt.scatter(xx,yy,c=coler,s=size)#
# c=plt.hist(xx,bins='auto')#bins=auto
# c=plt.pie(xx,labels=cc)
# plt.figure(figsize=(50,50),dpi=80)
# plt.yticks([30,40],['A','B'])
# plt.margins(0.1)
# plt.text(0,30,"mmad",fontsize=10)
# plt.show()
#=========================================
# iran=[20,30,40,50,60,70,80]
# armanetan=[10,20,30,40,50,60,70]
# year=[1960,1970,1980,1990,2000,2010,2020]
# plt.plot(iran,year,ls='-',marker='+')
# plt.plot(armanetan,year,ls='-.',marker='*',lw=1.765,mew=8)
# plt.legend(['iran','armanetan'],loc='best')
# plt.yticks([1960,1970,1980,1990,2000,2010,2020],['20m','30m','40m','50m','60m','70m','80m'])
# plt.annotate('iran 1990 ',xytext=(1980,40),xy=(1980,40),arrowprops={'facecolor':"silver",'width':4},fontsize=15)
# plt.show()
#===========================================
# iran=[20,30,40,50,60,70,80]
# armanetan=[10,20,30,40,50,60,70]
# year=[1960,1970,1980,1990,2000,2010,2020]
# plt.subplot(1,2,1)
# plt.plot(year,iran)
# plt.title('iran')
# plt.subplot(1,2,2)
# plt.plot(year,armanetan)
# plt.title('armanestan')
# plt.show()
#===============================
# df=pd.DataFrame({'c1':[1,2],'c2':[2,3]})
# df=df.astype('int32')
# print(df.dtypes)
#==================================================
# df=pd.DataFrame({'age':[1,2,3,4,5,6],'phone':[7,8,9,10,11,12]})
# d2=df.apply(lambda x:x[0]+2)
# d1=df.apply(lambda x:x+2)
# print(d2)
# print(d1)
#===========================

