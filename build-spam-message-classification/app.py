import streamlit as st
import pickle

st.title("Spam classification")

model = pickle.load(open("model.pkl","rb"))

message = st.text_input("Enter a message")

submit = st.button("Predict")

if submit:
    prediction = model.predict([message])

    if prediction[0] == 'ham':
        st.success(f"This message is a legit ({prediction[0]})") 

    else:
        st.warning(f"This message is not a {prediction[0]}")

st.balloons()
