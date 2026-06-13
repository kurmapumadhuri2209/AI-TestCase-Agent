import streamlit as st

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from app.generator import generate_test_cases


st.set_page_config(
    page_title="RequirementIQ",
    page_icon="🧪",
    layout="wide"
)


st.sidebar.title("RequirementIQ")
st.sidebar.write("AI-powered QA Reasoning Agent")

st.sidebar.markdown("---")

st.sidebar.subheader("What it generates")
st.sidebar.write("✅ Functional Test Cases")
st.sidebar.write("✅ Edge Cases")
st.sidebar.write("✅ Negative Test Cases")
st.sidebar.write("✅ Missing Requirements")
st.sidebar.write("✅ Test Data Suggestions")
st.sidebar.write("✅ Risk Analysis")

st.sidebar.markdown("---")

st.sidebar.subheader("Supported Requirement Types")
st.sidebar.write("🔐 Password Reset")
st.sidebar.write("🔑 Login")
st.sidebar.write("📝 Registration / Sign Up")
st.sidebar.write("🛒 Shopping Cart")


st.title("🧪 RequirementIQ")
st.subheader("QA Reasoning Agent for Smarter Test Design")

st.write(
    "RequirementIQ helps QA teams convert software requirements and user stories "
    "into structured test cases, edge cases, missing requirement questions, "
    "test data suggestions, and risk insights."
)

st.markdown("---")

st.subheader("Enter Requirement or User Story")

requirement = st.text_area(
    "Paste your requirement below:",
    height=180,
    placeholder="Example: As a customer, I want to reset my password using email so that I can regain access to my account."
)

col1, col2 = st.columns([1, 3])

with col1:
    generate_button = st.button("Generate QA Analysis")

with col2:
    st.write("")


if generate_button:

    if requirement.strip() == "":
        st.error("Please enter a requirement or user story before generating results.")
    else:
        with st.spinner("Analyzing requirement and generating QA output..."):
            results = generate_test_cases(requirement)

        st.success("QA Analysis Generated Successfully")

        st.subheader("Generated QA Output")

        st.text(results)