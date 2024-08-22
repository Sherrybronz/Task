import random
import string
import streamlit as st

def generate_password(length):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(random.choice(characters) for i in range(length))
    return password

st.title("Password Generator")
password_length = st.number_input("Enter the desired password length:")
if st.button("Generate Password"):
    generated_password = generate_password(password_length)
    st.write("Generated Password: ", generated_password)

