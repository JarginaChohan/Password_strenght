import streamlit as st
import re
import random
import string

st.title("Password Strength Meter")
st.subheader("Created by: Jargina Chohan")
st.write("This is a Password Strength Meter web application that helps you check the strength of your password.")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password length should be at least 8 characters.")

    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters (fixed regex)
    if re.search(r'[!@#$%&+=*\-_(){};:"<>?,./]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine password strength
    if score == 4:
        return "Strong Password!", "green", feedback
    elif score == 3:
        return "Moderate Password!", "orange", feedback
    else:
        return "Weak Password!", "red", feedback

# Function to generate a strong random password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(12))

# Input for password
password = st.text_input("Enter Your Password:", type="password")

# Evaluate password strength when input is given
if password:
    strength, color, suggestions = check_password_strength(password)
    st.markdown(f"<h3 style='color:{color};'>{strength}</h3>", unsafe_allow_html=True)
    
    if suggestions:
        st.write("Suggestions to improve your password:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
else:
    st.write("Please enter a password.")

# Generate a strong password
st.write("Automatically Generate a Strong Password")
if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.code(f"Suggested Strong Password: {strong_password}", language="plaintext")
