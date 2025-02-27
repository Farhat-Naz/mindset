import streamlit as st

st.set_page_config(page_title= "groth mindset project", )
st.title("Groth Mindset Challenge: Wen App with Streamlit")
st.header(" Welcome to Your Growth Journey!")
st.write("Embrace challange, learn from mistakes, and unlock your full potential. This AI-prowered app helps you build a growth mindset with reflection, challenges, and achievements!")
st.header("Today's Growth Mindset Quote")
st.write('"Sucess is not final, failure is not fatal: it is the courage to continue."-Winston churchill')

st.header("What is Your Challenge Today")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")
    
    #reflexing
    
    st.header("Reflect on your Learning")
    reflection = st.text_area("Write your reflection: {reflection}")
    
    if reflection:
        st.success(f"Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")
        
        #acheivements
        
        st.header("Celebrate Your Wins!")
        acheivment = st.text_input("Share something you've recently accomplished:")
        
        if acheivment:
            st.success(f"Amazing: {acheivment}")
        else:
            st.info("Big or small , every acheivement count! Share one now")
            
            #footer
        st.write("- - -")
        st.write("Keep believing in yourself. Growth is a journey, not a destination!")
        st.write("** Created by Farhat Naz**")
        
    