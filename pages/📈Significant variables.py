import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


st.write("# Significant variables & there dependence")

df = pd.read_csv("/Users/Admin/Desktop/HSE/my_project/german_credit_data.csv")
df['Risk'] = df['Risk'].replace('good', 'low')
df['Risk'] = df['Risk'].replace('bad', 'high')

df_main = df[['Age', 'Credit amount', 'Duration']].describe()
st.dataframe(df_main)

st.write("# BI VARIATE ANALYSIS (HUE=Risk)")

sig_var_1 = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Age', y='Credit amount', hue='Risk')
st.pyplot(sig_var_1.get_figure())

sig_var_2 = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Duration', y='Credit amount', hue='Risk')
st.pyplot(sig_var_2.get_figure())

sig_var_3  = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Age', y='Duration', hue='Risk')
st.pyplot(sig_var_3.get_figure())
