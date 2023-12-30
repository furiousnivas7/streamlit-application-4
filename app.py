import streamlit as st
import json
from datetime import datetime

# Function to save data to a JSON file
def save_data(data, filename="user_data.json"):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)

# Streamlit app
def main():
    st.title("User Information Form")

    with st.form("user_info_form"):
        name = st.text_input("Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        interest = st.text_input("Interest")
        dob = st.date_input("Date of Birth")

        submitted = st.form_submit_button("Submit")
        if submitted:
            user_data = {
                "name": name,
                "gender": gender,
                "interest": interest,
                "dob": dob.strftime("%Y-%m-%d")
            }
            save_data(user_data)
            st.success("Data Saved Successfully!")

    with open("user_data.json", "r") as json_file:
        st.download_button(
            label="Download JSON file",
            data=json_file,
            file_name="user_data.json",
            mime="application/json"
        )


if __name__ == "__main__":
    main()
