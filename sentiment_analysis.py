#Description
import streamlit as st
import sys
sys.path.append('src/')
import joblib 


#Title
st.write("""
# SENTIMENT ANALYSIS
""")

#Get Feature input from users

def get_user_text():
    user_test = st.text_input('Enter text here: ', '')
    return(user_test)
    
#Store the user inputs
user_text = get_user_text()

model = joblib.load('src/SVC(pipeline)')

sentiment = model.predict([user_text])
if sentiment == 0:
    sentiment = 'Negative'
elif sentiment == 1:
    sentiment = 'Positive'
st.write(sentiment)


    

import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "sentiment_analysis.py"]
    sys.exit(stcli.main())
