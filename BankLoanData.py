import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


st.set_page_config(
    page_title='Bank Loan Data'
)

st.write("# Bank Loan Data")

st.link_button("GitHub Code", "https://github.com/Boodeyman")

df = pd.read_csv("/Users/Admin/Desktop/HSE/my_project/german_credit_data.csv")
df['Risk'] = df['Risk'].replace('good', 'low')
df['Risk'] = df['Risk'].replace('bad', 'high')
df["Average loan"] = df['Credit amount'] / df["Duration"]
df = df.drop(236)
st.dataframe(df)


check = st.checkbox('See EDA')
if check:
    st.write('# EDA')
    st.text(
"""
DATASET SHAPE:  (1000, 10) 
--------------------------------------------------
FETURE DATA TYPES:
<class 'pandas.core.frame.DataFrame'>                  
Index: 1000 entries, 0 to 999
Data columns (total 10 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Age               1000 non-null   int64 
 1   Sex               1000 non-null   object
 2   Job               1000 non-null   int64 
 3   Housing           1000 non-null   object
 4   Saving accounts   817 non-null    object
 5   Checking account  606 non-null    object
 6   Credit amount     1000 non-null   int64 
 7   Duration          1000 non-null   int64 
 8   Purpose           1000 non-null   object
 9   Risk              1000 non-null   object
dtypes: int64(4), object(6)
memory usage: 85.9+ KB
None
--------------------------------------------------
NUMBER OF UNIQUE VALUES PER FEATURE: 
Age                  53
Sex                   2
Job                   4
Housing               3
Saving accounts       4
Checking account      3
Credit amount       921
Duration             33
Purpose               8
Risk                  2
dtype: int64
--------------------------------------------------
NULL VALUES PER FEATURE
Age                   0
Sex                   0
Job                   0
Housing               0
Saving accounts     183
Checking account    394
Credit amount         0
Duration              0
Purpose               0
Risk                  0
dtype: int64
"""
)

st.write('# Gender & Risk')
st.write("Let's look at the risk ratio associated with past lending history and then compare that to gender")

df_risk_2 = plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Risk', palette='spring')
st.pyplot(df_risk_2.get_figure())

df_risk_1 = plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Sex', hue='Risk', palette='magma')
st.pyplot(df_risk_1.get_figure())


st.write('# Job skill level')
st.write("Let's take a look at the people with what level of professionalism are most likely to take out a loan and what might that be related to?")

df_skill = px.pie(values=df['Job'].value_counts(),names=df['Job'].value_counts().index).update_layout(title='Histogram of job skills')
# plt.figure(figsize=(10, 5))
# sns.countplot(data=df, x='Job', palette='spring')
st.plotly_chart(df_skill)

st.write('# Saving accounts')
avg_sacc = df[['Average loan', 'Credit amount', 'Saving accounts', 'Risk']].groupby(by=['Saving accounts', 'Risk'],
                                                                                    as_index=False).mean()
sav_acc = plt.figure(figsize=(10, 5))
sns.barplot(data=avg_sacc, x='Saving accounts', y='Average loan', hue='Risk')
st.pyplot(sav_acc)

