import streamlit as st


def on_submit():
    print(input_text)


heading = st.header("Demo for text classification")
input_text = st.text_input(
    "Enter text here",
    placeholder="Demo text",
)
submit_button = st.button("Submit", on_click=on_submit)
output_text = st.text("This is prediction")










