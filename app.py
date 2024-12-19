import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Add custom CSS for better UI
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f7f7f7;
        color: #333333;
    }
    .stApp {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stSelectbox, .stNumberInput {
        margin-bottom: 15px;
    }
    .stTitle {
        color: #007bff;
        text-align: center;
        font-weight: bold;
    }
    .stText {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title('Student Result Prediction')

# Original code for user inputs and prediction
school = st.selectbox('School', ['Combined School', 'Single Gender School'])
if school == 'Combined School':
    school = 0
else:
    school = 1

sex = st.selectbox('Sex', ['F', 'M'])
if sex == 'F':
    sex = 0
else:
    sex = 1

age = st.number_input('Age', min_value=15, max_value=22, value=18)

address = st.selectbox('Address', ['Urban', 'Rural'])
if address == 'Urban':
    address = 0
else:
    address = 1

famsize = st.selectbox('Family Size', ['Less or Equal Than 3', 'More Than 3'])
if famsize == 'Less or Equal Than 3':
    famsize = 0
else:
    famsize = 1

Pstatus = st.selectbox('Parent\'s Cohabitation Status', ['Living Together', 'Apart'])
if Pstatus == 'Living Together':
    Pstatus = 0
else:
    Pstatus = 1

Medu = st.selectbox('Mother\'s Education', ['None', 'Primary Education', '5th to 9th Grade', 'Secondary Education', 'Higher Education'])
if Medu == 'None':
    Medu = 0
elif Medu == 'Primary Education':
    Medu = 1
elif Medu == '5th to 9th Grade':
    Medu = 2
elif Medu == 'Secondary Education':
    Medu = 3
else:
    Medu = 4

Fedu = st.selectbox('Father\'s Education', ['None', 'Primary Education', '5th to 9th Grade', 'Secondary Education', 'Higher Education'])
if Fedu == 'None':
    Fedu = 0
elif Fedu == 'Primary Education':
    Fedu = 1
elif Fedu == '5th to 9th Grade':
    Fedu = 2
elif Fedu == 'Secondary Education':
    Fedu = 3
else:
    Fedu = 4

Mjob = st.selectbox('Mother\'s Job', ['Teacher', 'Health', 'Services', 'At home', 'Other'])
if Mjob == 'Teacher':
    Mjob = 0
elif Mjob == 'Health':
    Mjob = 1
elif Mjob == 'Services':
    Mjob = 2
elif Mjob == 'At home':
    Mjob = 3
else:
    Mjob = 4

Fjob = st.selectbox('Father\'s Job', ['Teacher', 'Health', 'Services', 'At home', 'Other'])
if Fjob == 'Teacher':
    Fjob = 0
elif Fjob == 'Health':
    Fjob = 1
elif Fjob == 'Services':
    Fjob = 2
elif Fjob == 'At home':
    Fjob = 3
else:
    Fjob = 4

reason = st.selectbox('Reason to Choose This School', ['Close to Home', 'School Reputation', 'Course Preference', 'Other'])
if reason == 'Close to Home':
    reason = 0
elif reason == 'School Reputation':
    reason = 1
elif reason == 'Course Preference':
    reason = 2
else:
    reason = 3

guardian = st.selectbox('Guardian', ['Mother', 'Father', 'Other'])
if guardian == 'Mother':
    guardian = 0
elif guardian == 'Father':
    guardian = 1
else:
    guardian = 2

traveltime = st.selectbox('Travel Time', ['Less than 15 min.', '15 to 30 min.', '30 min. to 1 hour', 'More than 1 hour'])
if traveltime == 'Less than 15 min.':
    traveltime = 1
elif traveltime == '15 to 30 min.':
    traveltime = 2
elif traveltime == '30 min. to 1 hour':
    traveltime = 3
else:
    traveltime = 4

studytime = st.selectbox('Study Time', ['Less than 2 hours', '2 to 5 hours', '5 to 10 hours', 'More than 10 hours'])
if studytime == 'Less than 2 hours':
    studytime = 1
elif studytime == '2 to 5 hours':
    studytime = 2
elif studytime == '5 to 10 hours':
    studytime = 3
else:
    studytime = 4

failures = st.selectbox('Past Class Failures', ['None', '1', '2', '3', 'More than 3'])
if failures == 'None':
    failures = 0
elif failures == '1':
    failures = 1
elif failures == '2':
    failures = 2
elif failures == '3':
    failures = 3
else:
    failures = 4

schoolsup = st.selectbox('School Support', ['Yes', 'No'])
if schoolsup == 'Yes':
    schoolsup = 1
else:
    schoolsup = 0

famsup = st.selectbox('Family Support', ['Yes', 'No'])
if famsup == 'Yes':
    famsup = 1
else:
    famsup = 0

paid = st.selectbox('Paid Classes', ['Yes', 'No'])
if paid == 'Yes':
    paid = 1
else:
    paid = 0

activities = st.selectbox('Activities', ['Yes', 'No'])
if activities == 'Yes':
    activities = 1
else:
    activities = 0

nursery = st.selectbox('Nursery', ['Yes', 'No'])
if nursery == 'Yes':
    nursery = 1
else:
    nursery = 0

higher = st.selectbox('Higher Education', ['Yes', 'No'])
if higher == 'Yes':
    higher = 1
else:
    higher = 0

internet = st.selectbox('Internet Access', ['Yes', 'No'])
if internet == 'Yes':
    internet = 1
else:
    internet = 0

romantic = st.selectbox('Romantic Relationship', ['Yes', 'No'])
if romantic == 'Yes':
    romantic = 1
else:
    romantic = 0

famrel = st.selectbox('Family Relationship', ['Very Bad', 'Bad', 'Normal', 'Good', 'Very Good'])
if famrel == 'Very Bad':
    famrel = 1
elif famrel == 'Bad':
    famrel = 2
elif famrel == 'Normal':
    famrel = 3
elif famrel == 'Good':
    famrel = 4
else:
    famrel = 5

freetime = st.selectbox('Free Time', ['Very Low', 'Low', 'Normal', 'High', 'Very High'])
if freetime == 'Very Low':
    freetime = 1
elif freetime == 'Low':
    freetime = 2
elif freetime == 'Normal':
    freetime = 3
elif freetime == 'High':
    freetime = 4
else:
    freetime = 5

goout = st.selectbox('Going Out', ['Very Low', 'Low', 'Normal', 'High', 'Very High'])
if goout == 'Very Low':
    goout = 1
elif goout == 'Low':
    goout = 2
elif goout == 'Normal':
    goout = 3
elif goout == 'High':
    goout = 4
else:
    goout = 5

Dalc = st.selectbox('Weekday Drug Consumption', ['Very Low', 'Low', 'Normal', 'High', 'Very High'])
if Dalc == 'Very Low':
    Dalc = 1
elif Dalc == 'Low':
    Dalc = 2
elif Dalc == 'Normal':
    Dalc = 3
elif Dalc == 'High':
    Dalc = 4
else:
    Dalc = 5

Walc = st.selectbox('Weekend Drug Consumption', ['Very Low', 'Low', 'Normal', 'High', 'Very High'])
if Walc == 'Very Low':
    Walc = 1
elif Walc == 'Low':
    Walc = 2
elif Walc == 'Normal':
    Walc = 3
elif Walc == 'High':
    Walc = 4
else:
    Walc = 5

health = st.selectbox('Health', ['Very Bad', 'Bad', 'Normal', 'Good', 'Very Good'])
if health == 'Very Bad':
    health = 1
elif health == 'Bad':
    health = 2
elif health == 'Normal':
    health = 3
elif health == 'Good':
    health = 4
else:
    health = 5

absences = st.number_input('Absences', min_value=0, max_value=93, value=0)

model = pickle.load(open('model.pkl', 'rb'))
prediction_list = [school, sex, age, address, famsize, Pstatus, Medu, Fedu, Mjob, Fjob, reason, guardian, traveltime, studytime, failures, schoolsup, famsup,
                   paid, activities, nursery, higher, internet, romantic, famrel, freetime, goout, Dalc, Walc, health, absences]

if st.button('Predict'):
    prediction = model.predict([prediction_list])[0]
    if prediction > 0.5:
        st.success('The student will pass the exam')
    else:
        st.error('The student will fail the exam')
