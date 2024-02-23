
# Import Libraries
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

# Load Dataframes 
df_age_2023 = pd.read_pickle('Data/Dashboard Dataframes/df_age_2023.pkl')
df_LearnCourse_2023_ = pd.read_pickle('Data/Dashboard Dataframes/df_LearnCourse_2023_.pkl')
df_TimeSearching_2023 = pd.read_pickle('Data/Dashboard Dataframes/df_TimeSearching_2023.pkl')
df_AISearch_WorkedWith_ = pd.read_pickle('Data/Dashboard Dataframes/df_AISearch_WorkedWith_.pkl')
df_AISelect = pd.read_pickle('Data/Dashboard Dataframes/df_AISelect.pkl')
df_AIBen = pd.read_pickle('Data/Dashboard Dataframes/df_AIBen.pkl')
df_AIToolCurrently_ = pd.read_pickle('Data/Dashboard Dataframes/df_AIToolCurrently_.pkl')
df_Skills_Jobs = pd.read_pickle('Data/Dashboard Dataframes/df_Skills_Jobs.pkl')
df_MiscTech = df_Skills_Jobs['MiscTechHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True).reset_index().rename(columns={'index':'MiscTech',0:'count'}).replace({'.NET Framework (1.0 - 4.8)':'.NET Framework'})

st.markdown('<p style="color:#2929a3;font-size:50px;text-align:center;"><strong>Developers Dashboard </strong></p>',unsafe_allow_html=True)

col1_1 , col1_2 , col1_3 = st.columns([2,3,2])
col2_1 , col2_2 , col2_3 = st.columns([2,3,2])
col3_1 , col3_2 , col3_3 = st.columns([2,3,2])
col4_1 , col4_2 , col4_3 = st.columns([2,3,2])
col5_1 , col5_2 , col5_3 = st.columns([2,4,2])
col6_1 , col6_2 , col6_3 = st.columns([2,4,2])
col7_1 , col7_2 , col7_3 = st.columns([2,6,2])

with col1_1:
    st.plotly_chart(px.bar(data_frame=df_age_2023.sort_values(by='count', ascending=True), x='count', y='Age', orientation='h', text_auto=True, title='Age Distribution', height=450, width=500, color_discrete_sequence=['#2929a3']).update_layout(xaxis_title='', yaxis_title=''))
with col1_3:
    st.plotly_chart(px.bar(df_LearnCourse_2023_.sort_values(ascending=True), text_auto=True, orientation='h', title='Educational Platforms Distribution',height=450, width=500, color_discrete_sequence=['#2929a3']).update_layout(xaxis_title='', yaxis_title=''))
    
with col2_1:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['LanguageHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 Programming Languages').update_layout(xaxis_title='', yaxis_title=''))
with col2_3:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['DatabaseHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 Databases').update_layout(xaxis_title='', yaxis_title=''))
    
with col3_1:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['PlatformHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 Platforms').update_layout(xaxis_title='', yaxis_title=''))
with col3_3:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['WebframeHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 Webframes').update_layout(xaxis_title='', yaxis_title=''))
    
with col4_1:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['ToolsTechHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 Tools').update_layout(xaxis_title='', yaxis_title=''))
with col4_3:
    st.plotly_chart(px.bar(data_frame=df_Skills_Jobs['NEWCollabToolsHaveWorkedWith'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True), text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 CollabTools').update_layout(xaxis_title='', yaxis_title=''))
    
with col5_1:
    st.plotly_chart(px.bar(data_frame=df_MiscTech, x='count', y='MiscTech', text_auto=True, color_discrete_sequence=['#2929a3'], width=500, height=450, orientation='h', title='Top 10 MiscTech').update_layout(xaxis_title='', yaxis_title=''))
with col5_3:
    st.plotly_chart(px.pie(data_frame=df_TimeSearching_2023, names = 'TimeSearching', values = 'count', title='Time Searching',height=450, width=500, color_discrete_sequence=['#191966','#2929a3','#4646d2','#5b5bd7','#8484e1']))
    
with col6_1:
    st.plotly_chart(px.bar(df_AISearch_WorkedWith_.sort_values(ascending=True), text_auto=True, title='AI Tools Distribution',orientation='h', height=450, width=500, color_discrete_sequence=['#2929a3']).update_layout(xaxis_title='', yaxis_title=''))
with col6_3:
    st.plotly_chart(px.pie(data_frame=df_AIBen, names='AIBen', values='proportion', title='Trust in AI Tools', color_discrete_sequence=['#191966','#2929a3','#4646d2','#5b5bd7','#8484e1'], width=500, height=450))

    
with col7_1:
    st.plotly_chart(px.bar(data_frame=df_AIToolCurrently_.sort_values(ascending=False), text_auto=True, title='Things Where AI Tools Prefered to Use', color_discrete_sequence=['#2929a3'], width=500, height=500).update_layout(xaxis_title='', yaxis_title=''))
with col7_3:
    st.plotly_chart(px.pie(data_frame=df_AISelect, names='AISelect', values='proportion', color_discrete_sequence=['#191966','#2929a3','#4646d2'], title='Using or not AI Tools', width=450, height=500))    
