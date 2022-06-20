import pandas as pd
import numpy as np
import streamlit as st
import pickle
from PIL import Image
from pyngrok import ngrok

with open('bank_rf.pkl','rb') as f:
    model=pickle.load(f)

def run():
    img=Image.open('rbi.jpg')
    img=img.resize((700,156))
    st.image(img,use_column_width=False)
    st.title("Bank Subscription")
    
    
    #age
    age=st.slider("Mention the age of the customer",0,80)
    
    #job
    job_display=('Admin','Blue Collar','Entrepreneur','House Maid','Management','Retired','Self Employed','Services','Student','Technician','Unemployed')
    job_options=list(range(len(job_display)))
    job=st.selectbox("Mention the job",job_options,format_func=lambda x:job_display[x])
    
    #marital
    marital_display=('Divorced','Married','Single')
    marital_options=list(range(len(marital_display)))
    marital=st.selectbox("Mention the marital status",marital_options,format_func=lambda x:marital_display[x])
    
    #education
    edu_display=('Primary','Secondary','Tertiary')
    edu_options=list(range(len(edu_display)))
    edu=st.selectbox("Mention the Educational qualification",edu_options,format_func=lambda x:edu_display[x])
    
    #default
    def_display=('No','Yes')
    def_options=list(range(len(def_display)))
    default=st.selectbox("Does the customer have credit",def_options,format_func=lambda x:def_display[x])
    
    #balance
    bal=st.slider("Mention the account balance",-10000,120000)
    
    #housing
    hou_display=('No','Yes')
    hou_options=list(range(len(hou_display)))
    housing=st.selectbox("Does the customer have housing loan",hou_options,format_func=lambda x:hou_display[x])
    
    #personalloan
    per_display=('No','Yes')
    per_options=list(range(len(per_display)))
    per=st.selectbox("Does the customer have personal loan",per_options,format_func=lambda x:per_display)
    
    #contact
    con_display=('Cellular','Telephone')
    con_options=list(range(len(con_display)))
    con=st.selectbox("Contact type",con_options,format_func=lambda x:con_display[x])
    
    #last_day_contact
    last_day=st.slider("Mention the last day(number) of contact",1,31)
    
    #last_month_contact
    last_mon_display=('April','August','December','February','January','July','June','March','May','November','October','September')
    last_mon_options=list(range(len(last_mon_display)))
    last_month=st.selectbox("Mention the last month of contact",last_mon_options,format_func=lambda x:last_mon_display[x])
    
    #duration
    dur=st.slider("Mention the duration of the call",0,5000)
    
    #campaign
    campaign=st.slider("No of contacts performed during this campaign",0,70)
    
    #pdays
    days=st.number_input("No of days passed after calling in previous campaign?('-1' means not called)")
    
    #previous
    previous=st.number_input("No of contacts performed before")
    
    if st.button("Submit"):
        features=[[age,job,marital,edu,default,bal,housing,per,con,last_day,last_month,dur,campaign,days,previous]]
        prediction=model.predict(features)
        lc=[str(i) for i in prediction]
        ans=int("".join(lc))
        if ans==0:
            st.error('Hello!'
                     "Customer has not subscribed the term deposit")
        else:
            st.success("Hello!"
                       "Customer has subscribed the term deposit")
run()