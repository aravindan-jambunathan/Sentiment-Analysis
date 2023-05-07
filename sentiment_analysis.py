import streamlit as st
import joblib 

model = joblib.load('src/SVC(pipeline)')

def get_user_text():
    user_test = st.text_input('Enter text here:', '')
    if not user_test:
        st.warning('Please enter some text.')
    return user_test
    
st.write("# SENTIMENT ANALYSIS")

user_text = get_user_text()

if user_text:
    sentiment = model.predict([user_text])
    if sentiment == 0:
        sentiment = 'Negative'
    elif sentiment == 1:
        sentiment = 'Positive'
    st.write(sentiment)

if __name__ == '__main__':
    st.set_page_config(page_title='Sentiment Analysis', page_icon=':satisfied:')
    st.write('This app analyzes the sentiment of text.')
    st.write('Enter some text and click the button to see the sentiment.')
    st.write('Created by [Your Name]')
    st.write('---')
    st.write('### Input')
    user_text = get_user_text()
    st.write('### Output')
    if user_text:
        sentiment = model.predict([user_text])
        if sentiment == 0:
            sentiment = 'Negative'
        elif sentiment == 1:
            sentiment = 'Positive'
        st.write(sentiment)
