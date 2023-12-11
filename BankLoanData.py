import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.set_page_config(initial_sidebar_state="collapsed")

# st.set_page_config(
#     page_title='Bank Loan Data'
# )

tab1, tab2, tab3, tab4 = st.tabs(['🏠Home', '🧹Data cleanup', '📈Significant variables', '✈️Purpose'])

with tab1:
    st.write("# Bank Loan Data")

    st.link_button("GitHub Code", "https://github.com/Boodeyman")

    df = pd.read_csv("german_credit_data.csv")
    df['Risk'] = df['Risk'].replace('good', 'low')
    df['Risk'] = df['Risk'].replace('bad', 'high')
    df["Average loan"] = df['Credit amount'] / df["Duration"]
    df = df.drop(236)
    st.dataframe(df)


    # check = st.checkbox('See EDA')
    # if check:
    with st.expander("See EDA"):
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

    df_skill = px.pie(values=df['Job'].value_counts(), names=df['Job'].value_counts().index).update_layout(title='Histogram of job skills', height=450, width=350)
    # plt.figure(figsize=(10, 5))
    # sns.countplot(data=df, x='Job', palette='spring')
    st.plotly_chart(df_skill)

    st.write('# Saving accounts')
    avg_sacc = df[['Average loan', 'Credit amount', 'Saving accounts', 'Risk']].groupby(by=['Saving accounts', 'Risk'],
                                                                                        as_index=False).mean()
    sav_acc = plt.figure(figsize=(10, 5))
    sns.barplot(data=avg_sacc, x='Saving accounts', y='Average loan', hue='Risk')
    st.pyplot(sav_acc)

with tab2:
    df = pd.read_csv("german_credit_data.csv")
    df['Risk'] = df['Risk'].replace('good', 'low')
    df['Risk'] = df['Risk'].replace('bad', 'high')

    st.write("# Average loan & Job. Outlier")
    st.write(
        "Add a new column 'Average loan', which will contain the amount people borrow per month (monthly repayment amount without interest)")
    st.write(
        "Check the resulting column with the level of professionalism, what would be the relationship between 'Job' & 'Average loan'? Is it true that the higher the level of education, the larger the loan amount?")

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
    st.write(
        "My data set has columns with NaN values and I need to find similarity to complete those columns or drop them if similarity is not found")

    nan = df.isna().sum() / df.shape[0]
    st.dataframe(nan)

with tab3:
    st.write("# Significant variables & there dependence")
    st.write(
        "Let's look at our significant variables and find out their average values, minimums, maximums, and spreads. What dependencies can we discover if we compare the variables of our dataset with each other?")
    df = pd.read_csv("german_credit_data.csv")
    df['Risk'] = df['Risk'].replace('good', 'low')
    df['Risk'] = df['Risk'].replace('bad', 'high')

    df_main = df[['Age', 'Credit amount', 'Duration']].describe()
    st.dataframe(df_main)

    st.write("# BI VARIATE ANALYSIS (HUE=Risk)")
    st.write(
        "My hypotheses is that as age increases, the length and amounts of loans will increase. Let's find the pattern from the 3 graphs below.")
    sig_var_1 = plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='Age', y='Credit amount', hue='Risk')
    st.pyplot(sig_var_1.get_figure())

    sig_var_2 = plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='Duration', y='Credit amount', hue='Risk')
    st.pyplot(sig_var_2.get_figure())

    sig_var_3 = plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='Age', y='Duration', hue='Risk')
    st.pyplot(sig_var_3.get_figure())

with tab4:
    df = pd.read_csv("german_credit_data.csv")
    df['Risk'] = df['Risk'].replace('good', 'low')
    df['Risk'] = df['Risk'].replace('bad', 'high')

    df["Average loan"] = df['Credit amount'] / df["Duration"]
    df = df.drop(236)
    avg_purpose = df[['Average loan', 'Purpose', 'Risk']].groupby(by=['Purpose', 'Risk'],
                                                                  as_index=False).mean()
    avg_job = df[['Average loan', 'Credit amount', 'Job', 'Purpose']].groupby(by=['Purpose', 'Job'],
                                                                              as_index=False).mean()

    st.write('# Purpose')
    st.write("A loan can be taken out for a variety of purposes. The most common are:")

    p_c = plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)
    sns.countplot(data=df, x='Purpose', hue='Risk')
    st.pyplot(p_c.get_figure())

    p_cc = plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)
    sns.barplot(data=avg_purpose, x='Purpose', y='Average loan', hue='Risk', palette='viridis')
    st.pyplot(p_cc.get_figure())

    st.write("# Purpose & Loan amount")
    st.write(
        "Is it true that if person has good job skills => bigger payment => bigger loan amount which can be taken out? Let's check out the graph below.")

    p_ccc = plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45)
    sns.barplot(data=avg_job, x='Purpose', y='Credit amount', hue='Job')
    st.pyplot(p_ccc.get_figure())

