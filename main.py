import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #1e3a5f; /* Deep Blue */
            color: #ffffff; /* White text */
        }
        .main {
            text-align: center;
        }
        .stTitle {
            color:#1e3a5f;
        }
        .stWrite {
            color: #1e3a5f;
         }
        .stTextInput {
            width: 70% !important;
            margin: left;
            border: 2px solid #4ecdc4; /* Soft Cyan */
            border-radius: 8px;
            padding: 8px;
            border-color: #4ecdc2;
        }
        .stButton button {
            background-color: #4ecdc4; /* Soft Cyan */
            color: #1e3a5f; /* Deep Blue */
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #3caea3;
            color: white;
            text-color:white;
            border-color:#3caea3;
        }
        .stAlert {
            border-radius: 8px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("Password Strength Meter")
st.write("Enter Your Password below to check its strength!🔐")

# Function to check password strength
def check_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be **at least 8 characters long**.")

    # Check uppercase & lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟠 Password should include both **uppercase and lowercase letters**.")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟡 Password should include **numbers**.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        score += 1
    else:
        feedback.append("🔵 Password should include **special characters**.")

    # Check for common passwords
    common_passwords = ["12345678", "password", "qwerty"]
    if password in common_passwords:
        feedback.append("⚠️ This password is **too common** and easily guessed!")

    # Display results
    if score == 4:
        st.success("✅ Your password is **Strong** and **Secure**!")
    elif score == 3:
        st.info("🔹 Your password is **Moderate**. It can be improved.")
    else:
        st.error("❌ Your password is **Weak**. Follow the suggestions to strengthen it.")

    # Display feedback
    if feedback:
        with st.expander("💡 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password input
password = st.text_input("🔑 Enter Your Password:", type="password", help="Password should be at least 8 characters long, include both uppercase and lowercase letters, numbers, and special characters.")

# Button to check password
if st.button("🔍 Check Password"):
    if password:
        check_password(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")


st.write("-------------------------------")
st.write("**Made by Rida Fatima**")