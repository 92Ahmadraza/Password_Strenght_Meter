import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")

password_input = st.text_input("Enter your password", type="password")

if password_input:
    score, feedback = check_password_strength(password_input)

    # Strength classification
    if score <= 2:
        st.error("Strength: Weak")
    elif score <= 4:
        st.warning("Strength: Moderate")
    else:
        st.success("Strength: Strong")

    # Show feedback
    if feedback:
        st.write("### Suggestions to improve your password:")
        for f in feedback:
            st.write(f"- {f}")
    else:
        st.balloons()
        st.write("✅ Your password is strong and meets all the recommended criteria!")

