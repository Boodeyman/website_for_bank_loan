import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


st.write("# Significant variables & there dependence")
st.write("Let's look at our significant variables and find out their average values, minimums, maximums, and spreads. What dependencies can we discover if we compare the variables of our dataset with each other?")
df = pd.read_csv("german_credit_data.csv")
df['Risk'] = df['Risk'].replace('good', 'low')
df['Risk'] = df['Risk'].replace('bad', 'high')

df_main = df[['Age', 'Credit amount', 'Duration']].describe()
st.dataframe(df_main)

st.write("# BI VARIATE ANALYSIS (HUE=Risk)")
st.write("My hypotheses is that as age increases, the length and amounts of loans will increase. Let's find the pattern from the 3 graphs below.")
sig_var_1 = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Age', y='Credit amount', hue='Risk')
st.pyplot(sig_var_1.get_figure())

sig_var_2 = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Duration', y='Credit amount', hue='Risk')
st.pyplot(sig_var_2.get_figure())

sig_var_3  = plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Age', y='Duration', hue='Risk')
st.pyplot(sig_var_3.get_figure())
