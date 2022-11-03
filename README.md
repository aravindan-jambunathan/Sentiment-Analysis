# Sentiment-Analysis
Sentiment analysis studies the subjective information in an expression, that is, the opinions, appraisals, emotions, or attitudes towards a topic,   
person or entity. Expressions can be classiNed as positive, negative, or neutral. For example: “I really like the new design of your website!”  
→ Positive. • You are provided with a dataset of the ‘restaurant review’ taken from kaggle. Build a machine learning model by using  
Support vector classiNer(SVM) and count vectorizer using two methods(direct method, pipeline method) to predict the label of the review either as 
positive or negative. • Also use MultinomialNB (Naïve bayes) and count vectorizer using two methods(direct method, pipeline method) to classiNy if  
the sentiment is positive or negative and compare the accuracies of all 4 models of the models • https://www.kaggle.com/d4rklucif3r/restaurant-reviews •   
[[NOTE :There are two features - ‘review’ - the sentence and ‘sentiment’ - the label for the review. 1 means positive review and 0 means negative review.]].
1.Create a dataframe.<br/>
2.process the data and do visualizations (represent using matplotlib / seaborn the number of positive reviews and negative reviews)(ex-use a bar graph).<br/> 
3.create svc model and count vectorizer separately (method 1).<br/>    
4.(method 2) create a pipeline with Vectorization model and ML algorithm to predict the Nnal sentiment.<br/>  
5.create NB model and count vectorizer separately (method 1).<br/> 
6.(method 2) create a pipeline with Vectorization model and ML algorithm to predict the Nnal sentiment for the multinomialNB and CountVectorizer.<br/> 
7.Use joblib to create and save it as a model (USE THE MODEL WITH THE HIGHEST ACCURACY)(joblib is similar to pickle).<br/> 
8.Using the new model created using joblib, predict the output of a new review.<br/> 
9.Create a streamlit webapp for sentiment analysis using the joblib model (pipeline model).<br/> 
