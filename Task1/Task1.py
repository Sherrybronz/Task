import random
import streamlit as st

def generate_password(length, has_uppercase, has_lowercase, has_digits, has_specialcharacter):
    upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digits=['0','1','2','3','4','5','6','7','8','9']
    specialcharacter=['!','@','#','$','%','^','&','*','(',')','_','<','>','?']
    characters = ''
    if has_uppercase:
        characters = characters + ''.join(upper)
    if has_lowercase:
        characters = characters + ''.join(lower)
    if has_digits:
        characters = characters + ''.join(digits)
    if has_specialcharacter:
        characters = characters + ''.join(specialcharacter)
    password = "".join(random.choice(characters) for i in range(length))
    return password

def main():
    st.title("Password Generator")
    password_length = st.number_input("Enter the Desired Password Length:", min_value=4, max_value=128)
    st.write("Enter What Should be Included in Your Password : ")
    has_uppercase = st.checkbox("Include Uppercase Letters")
    has_lowercase = st.checkbox("Include Lowercase Letters")
    has_digits = st.checkbox("Include Digits")
    has_specialcharacter = st.checkbox("Include Special Characters")
    if not (has_uppercase or has_lowercase or has_digits or has_specialcharacter):
        st.error("Please Select Atleast One Category.")
    else:
        if st.button("Generate Password"):
            generated_password = generate_password(password_length, has_uppercase, has_lowercase, has_digits, has_specialcharacter)
            st.write("Generated Password: ", generated_password)

if __name__=="__main__":
    main()
