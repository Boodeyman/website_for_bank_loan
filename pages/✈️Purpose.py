import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/Users/Admin/Desktop/HSE/my_project/german_credit_data.csv")
df['Risk'] = df['Risk'].replace('good', 'low')
df['Risk'] = df['Risk'].replace('bad', 'high')
df["Average loan"] = df['Credit amount'] / df["Duration"]
df = df.drop(236)
avg_purpose = df[['Average loan', 'Purpose', 'Risk']].groupby(by=['Purpose', 'Risk'],
                                                              as_index=False).mean()
avg_job = df[['Average loan', 'Credit amount', 'Job', 'Purpose']].groupby(by=['Purpose', 'Job'],
                                                                          as_index=False).mean()

st.write('# Purpose')
st.write("There are many purposes to take a loan. The most common are:")

p_c = plt.figure(figsize=(10, 5))
plt.xticks(rotation=45)
sns.countplot(data=df, x='Purpose', hue='Risk')
st.pyplot(p_c.get_figure())

p_cc = plt.figure(figsize=(10, 5))
plt.xticks(rotation=45)
sns.barplot(data=avg_purpose, x='Purpose', y='Average loan', hue='Risk', palette='viridis')
st.pyplot(p_cc.get_figure())

p_ccc = plt.figure(figsize=(10, 5))
plt.xticks(rotation=45)
sns.barplot(data=avg_job, x='Purpose', y='Credit amount', hue='Job')
st.pyplot(p_ccc.get_figure())
