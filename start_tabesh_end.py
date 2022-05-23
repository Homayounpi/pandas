import pandas as pd
df_en=pd.read_excel('subActicePower.xlsx')
df_ta=pd.read_excel('irradiation11.xlsx')
name_sub='Measurement Sub6'
df_en=df_en[df_en['EquipmentName']==name_sub]
# df_en=pd.DataFrame({})
# df_ta=pd.DataFrame({})
class start_tabesh:
    def __init__(self,df_en,df_ta):
        self.df_ta=df_ta
        self.df_en=df_en
    def start_end_energy(self):
        #aghe file energy khali bashad
        if (self.df_en.empty)&(self.df_ta.empty):
            df = pd.DataFrame({'name': ['no energy', 'no energy']})
            return df['name']
        elif self.df_en.empty:
            df=pd.DataFrame({'name':['no energy','no energy']})
            return df['name']
        # aghe file energy khali nabashad
        df_main = self.df_en[ self.df_en['Value'] >= 50]
        df_main = pd.concat([df_main.head(1),df_main.tail(1)])
        df_main['CreationDate']=pd.to_datetime(df_main['CreationDate'])
        return df_main['CreationDate']
    def start_tabessh(self):
        # aghe file enerjy nadashtim
        if (self.df_en.empty)&(self.df_ta.empty):
            df = pd.DataFrame({'name': ['no tabesh']})
            return df['name'].iloc[0]
        elif self.df_en.empty:
            self.df_ta['CreationDate']=pd.to_datetime(self.df_ta['CreationDate'])
            start_tabe = self.df_ta[(self.df_ta['CreationDate'].dt.hour >= 4)&(self.df_ta['CreationDate'].dt.hour < 8)&
                                    (self.df_ta['Value'] > 5) & (self.df_ta['Value'].shift(-1) > 5) &
                                    (self.df_ta['Value'].shift(-2) > 5) & (self.df_ta['Value'].shift(-3) > 5) &
                                    (self.df_ta['Value'].shift(-4) > 5)]
            start_tabe=start_tabe.head(1)['CreationDate']
            return start_tabe.iloc[0]
        #aghe file tabesh nadashtim
        elif self.df_ta.empty:
            return 'no tabesh'
        #aghe  har 2 ta file dashtim
        self.df_ta['CreationDate'] = pd.to_datetime(self.df_ta['CreationDate'])
        start_tabe=self.df_ta[(self.df_ta['CreationDate']<=self.start_end_energy().iloc[0])&
                                  (self.df_ta['Value']<3)&(self.df_ta['Value'].shift(1)<3)&
                                  (self.df_ta['Value'].shift(2)<3)&(self.df_ta['Value'].shift(3)<3)&
                                  (self.df_ta['Value'].shift(4)<3)]
        start_tabe = start_tabe.tail(1)
        return start_tabe['CreationDate'].iloc[0]
    def end_tabesh(self):
        #aghe file energy nadashtim
        if (self.df_ta.empty)&(self.df_en.empty):
            df = pd.DataFrame({'name': ['no tabesh']})
            return df['name'].iloc[0]
        elif self.df_en.empty:
            self.df_ta['CreationDate'] = pd.to_datetime(self.df_ta['CreationDate'])
            end_tabe = self.df_ta[(self.df_ta['CreationDate'].dt.hour >= 16) &(self.df_ta['CreationDate'].dt.hour < 20)&
                                  (self.df_ta['Value'] < 5) & (self.df_ta['Value'].shift(-1) < 5) &
                                  (self.df_ta['Value'].shift(-2) < 5) & (self.df_ta['Value'].shift(-3) < 5) &
                                  (self.df_ta['Value'].shift(-4) < 5)]
            end_tabe=end_tabe.head(1)['CreationDate']
            return end_tabe.iloc[0]
        #aghe file tabesh nadashtim
        elif self.df_ta.empty:
            df=pd.DataFrame({'name':['no tabesh','no tabesh']})
            return 'no tabesh'
        #aghe har 2 ta file dashe bashim
        end_tabe = self.df_ta[(self.df_ta['CreationDate'] > self.start_end_energy().iloc[1]) &
                                    (self.df_ta['Value'] < 3) & (self.df_ta['Value'].shift(-1) < 3) &
                                    (self.df_ta['Value'].shift(-2) < 3) & (self.df_ta['Value'].shift(-3) < 3) &
                                    (self.df_ta['Value'].shift(-4) < 3)]
        self.df_ta['CreationDate'] = pd.to_datetime(self.df_ta['CreationDate'])
        end_tabe = end_tabe.head(1)
        return end_tabe['CreationDate'].iloc[0]
valu=start_tabesh(df_en,df_ta)
df=pd.DataFrame({'valus':['start_energy','end_energy','start_tabesh','end_tabesh'],
                 'date':[valu.start_end_energy().iloc[0],valu.start_end_energy().iloc[1],
                         valu.start_tabessh(),valu.end_tabesh()]})
print(df.to_string())



