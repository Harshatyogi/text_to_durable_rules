import streamlit as st
import requests

st.set_page_config(page_title="Text → Durable Rules")

st.title("🧠 Text to Durable Rules Generator")

text = st.text_area("Enter policy / rule text")

if st.button("Generate Rule"):
    res = requests.post(
        "http://127.0.0.1:8000/generate-rule",
        params={"text": text}
    )

    if res.status_code == 200:
        data = res.json()

        st.subheader("📦 Generated JSON")
        st.json(data["json"])

        st.subheader("⚙️ Durable Rules Code")
        st.code(data["durable_rule"], language="python")
    else:
        st.error("Failed to generate rule")
