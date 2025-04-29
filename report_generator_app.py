import streamlit as st
import openai
import os

st.set_page_config(page_title="RadiologyGPT", layout="centered")
st.title("🧠 Radiology Report Generator")
st.write("Enter study details and generate structured report.")

# Get API key securely from secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

# Input fields
study_type = st.selectbox("Select Study Type", ["MRI Brain", "CT Thorax", "MRI Knee"])
clinical = st.text_input("Enter Clinical Indication")
findings = st.text_area("Enter Compressed Findings")

if st.button("Generate Report"):
    with st.spinner("Generating report..."):

        prompt = f"""
        You are a radiologist trained in writing structured reports.
        Create a radiology report using this format:

        1. Sequences
        2. Clinical Indication
        3. Imaging Findings (bullet points)
        4. Impression (summary sentence)

        Study: {study_type}
        Clinical Indication: {clinical}
        Compressed Findings: {findings}
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can change to gpt-4 if needed
                messages=[
                    {"role": "system", "content": "You are a helpful radiology assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            report = response.choices[0].message.content
            st.subheader("📝 Final Report")
            st.code(report, language="markdown")

        except Exception as e:
            st.error(f"Error generating report: {e}")
