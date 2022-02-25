import pandas as pd

CAC40 = pd.read_csv('CAC40.csv')
CAC40 = CAC40.loc[:,['Close']]
CAC40.insert(0,'Jour',[i for i in range(1, len(CAC40)+1)])
print(CAC40.head(5))

DAX = pd.read_csv('DAX30.csv')
DAX = DAX.loc[:,['Close']]
DAX.insert(0,'Jour',[i for i in range(1, len(DAX)+1)])

print(DAX.head(5))

FTSE = pd.read_csv('FTSE.csv', sep=";")
print(FTSE.head(5))

DJI = pd.read_csv('DJI.csv', sep=";")
print(DJI.head(5))

IXIC = pd.read_csv('NASDAQ.csv')
IXIC = CAC40.loc[:,['Close']]
IXIC.insert(0,'Jour',[i for i in range(1, len(IXIC)+1)])

print(IXIC.head(5))


import numpy as np

def score_function(DATAFRAME):
    score = [0]
    for i in range(1,len(DATAFRAME)):
        taux = np.log(DATAFRAME['Close'][i]/DATAFRAME['Close'][i-1])
        if taux > 0.005:
            score.append(1)
        if taux <= 0.005 and taux >=-0.005 :
            score.append(0)
        if taux < -0.005:
            score.append(-1)
    DATAFRAME.insert(1,'Score', score)

score_function(DAX)
score_function(CAC40)
score_function(IXIC)
score_function(DJI)
score_function(FTSE)

print(DAX.head(5))
print(CAC40.head(5))
print(IXIC.head(5))
print(DJI.head(5))
print(FTSE.head(5))

print("----- Table de probabilité pour le dataframe DAX ------ ")
table_DAX= DAX['Score'].value_counts()/sum(DAX['Score'].value_counts())
print(table_DAX)

print("----- Table de probabilité pour le dataframe CAC40 ------ ")
table_CAC40= CAC40['Score'].value_counts()/sum(CAC40['Score'].value_counts())
print(table_CAC40)

print("----- Table de probabilité pour le dataframe FTSE ------ ")
table_FTSE=FTSE['Score'].value_counts()/sum(FTSE['Score'].value_counts())
print(table_FTSE)

print("----- Table de probabilité pour le dataframe DJI ------ ")
table_DJI=DJI['Score'].value_counts()/sum(DJI['Score'].value_counts())
print(table_DJI)

print("----- Table de probabilité pour le dataframe IXIC ------ ")
table_IXIC= IXIC['Score'].value_counts()/sum(IXIC['Score'].value_counts())
print(table_IXIC)


liste = []

def Proba(DATAFRAME):
    
    for i in range(0,len(DATAFRAME['Score'])-1):
        Test = DATAFRAME['Score'][i],DATAFRAME['Score'][i+1]
        TestS = str(Test)
        liste.append(TestS)

Proba(IXIC)

print("------------ Pr(ST, ST+1) ---------------")

df = pd.DataFrame(columns=['0','1','-1'])
lign1 = pd.DataFrame(
    data=np.array([[liste.count('(0, 0)'),
    liste.count('(0, 1)'),
    liste.count('(0, -1)')]]),
    columns=['0','1','-1'])
lign2 = pd.DataFrame(
    data=np.array([[liste.count('(1, 0)'),
    liste.count('(1, 1)'),
    liste.count('(1, -1)')]]),
    columns=['0','1','-1'])
lign3 = pd.DataFrame(
    data=np.array([[liste.count('(-1, 0)'),
    liste.count('(-1, 1)'),
    liste.count('(-1, -1)')]]),
    columns=['0','1','-1'])
df = pd.concat([df,lign1], ignore_index=True)
df = pd.concat([df,lign2], ignore_index=True)
df = pd.concat([df,lign3], ignore_index=True)
df=df.rename(index={2: '-1'}) 
print(df)
print(df/sum(df.sum()))

print("------------ Pr(ST | ST+1) pareil que Pr(ST-1, ST) ---------------")
print(df/df.sum())

