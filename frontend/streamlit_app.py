import streamlit as st

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from app.generator import generate_test_cases

st.title("🧪 AI Test Case Generator")

st.write("Welcome to the Agents League Hackathon Project")

requirement = st.text_area(
    "Paste your requirement or user story here:"
)

if st.button("Generate Test Cases"):

    if requirement.strip() == "":
        st.error("Please enter a requirement.")
    else:
        results = generate_test_cases(requirement)

        st.subheader("Generated Output")

        st.text(results)