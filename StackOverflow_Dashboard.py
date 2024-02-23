
# Import Libraries
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

# Load Dataframes
df_NEWSOSites_2023_ = pd.read_pickle('Data/Dashboard Dataframes/df_NEWSOSites_2023_.pkl')
df_SurveyLength_2023 = pd.read_pickle('Data/Dashboard Dataframes/df_SurveyLength_2023.pkl')
df_SurveyEase_2023 = pd.read_pickle('Data/Dashboard Dataframes/df_SurveyEase_2023.pkl')
df_SOPartFreq_2023 = pd.read_pickle('Data/Dashboard Dataframes/df_SOPartFreq_2023.pkl')
df_SOPartFreq_2023 = df_SOPartFreq_2023.sort_values(by='count', ascending=False).replace({'I have never participated in Q&A on Stack Overflow':'Never used it','A few times per month or weekly':'A few times','Less than once per month or monthly':'Less than once per month'})

st.markdown('<p style="color:#2929a3;font-size:50px;text-align:center;"><strong>StackOverflow Dashboard </strong></p>',unsafe_allow_html=True)

col1_1 , col1_2 , col1_3 = st.columns([2,3,2])
col2_1 , col2_2 , col2_3 = st.columns([2,3,2])
col3_1 , col3_2 , col3_3 = st.columns([2,3,2])

with col1_1:
    st.plotly_chart(px.bar(df_NEWSOSites_2023_.sort_values(ascending=False), text_auto=True, orientation='v', color_discrete_sequence=['#2929a3'], height=450, width=500,title='StackOverflow Sites Usage').update_layout(xaxis_title='', yaxis_title=''))
with col1_3:
        st.plotly_chart(px.bar(data_frame=df_SOPartFreq_2023,x = 'SOPartFreq', y = 'count', text_auto=True, orientation='v', color_discrete_sequence=['#2929a3'], height=450, width=500, title='StackOverFlow Website Visits').update_layout(xaxis_title='', yaxis_title=''))

with col2_1:
    st.plotly_chart(px.pie(data_frame=df_SurveyLength_2023.sort_values(by='count', ascending=True), names='SurveyLength', values='count', color_discrete_sequence=['#2929a3'], height=450, width=500, title='Survey Length'))
    
with col2_3:
    st.plotly_chart(px.pie(data_frame=df_SurveyEase_2023.sort_values(by='count', ascending=True), names='SurveyEase', values='count', color_discrete_sequence=['#2929a3'],height=450, width=500, title='Survey Ease'))
    
    
