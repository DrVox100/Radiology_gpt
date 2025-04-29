import streamlit as st

st.set_page_config(page_title="RadiologyGPT", layout="centered")

st.title("🧠 Radiology Report Generator")
st.write("If you see this, your Streamlit app is running correctly.")

study_type = st.selectbox("Select Study Type", ["MRI Brain", "CT Thorax", "MRI Knee"])
clinical = st.text_input("Enter Clinical Indication")
findings = st.text_area("Enter Compressed Findings")

if st.button("Generate"):
    st.success("Your inputs have been received.")
    st.markdown(f"- **Study**: {study_type}\n- **Clinical**: {clinical}\n- **Findings**: {findings}")
