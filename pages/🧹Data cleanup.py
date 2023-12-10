import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("german_credit_data.csv")
df['Risk'] = df['Risk'].replace('good', 'low')
df['Risk'] = df['Risk'].replace('bad', 'high')

st.write("# Average loan & Job. Outlier")
st.write("Add a new column 'Average loan', which will contain the amount people borrow per month (monthly repayment amount without interest)")
st.write("Check the resulting column with the level of professionalism, what would be the relationship between 'Job' & 'Average loan'? Is it true that the higher the level of education, the larger the loan amount?")

page_names = ['Outlier', 'No outlier']
page = st.radio('', page_names)
df["Average loan"] = df['Credit amount'] / df["Duration"]

if page == 'Outlier':
    avg = df[['Job', 'Risk', 'Average loan']].groupby(by=['Job', 'Risk'], as_index=False).mean()
    st.dataframe(avg)

    a_1 = plt.figure(figsize=(10, 5))
    plt.suptitle('Dependence with outlier', fontsize=20)
    sns.barplot(data=avg, x='Job', y='Average loan', hue='Risk', palette='magma')
    st.pyplot(a_1.get_figure())
else:
    avg_outlier = df.drop(236)[['Job', 'Risk', 'Average loan']].groupby(by=['Job', 'Risk'], as_index=False).mean()
    st.dataframe(avg_outlier)

    a_2 = plt.figure(figsize=(10, 5))
    plt.suptitle('Dependence without outlier', fontsize=20)
    sns.barplot(data=avg_outlier, x='Job', y='Average loan', hue='Risk', palette='magma')
    st.pyplot(a_2.get_figure())


st.write('# NaN values')
st.write("My data set has columns with NaN values and I need to find similarity to complete those columns or drop them if similarity is not found")

nan = df.isna().sum() / df.shape[0]
st.dataframe(nan)

