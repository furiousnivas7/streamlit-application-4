import streamlit as st
import json
from datetime import datetime
import os
# import openai
# from openai import OpenAI

def save_data_as_json(file_name):
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            return json.dumps(json.load(file))
    return json.dumps([])

# def call_gbt3(prompt):
#     openai.api_key = os.environ['OPEN_API_KEY']
#     client=OpenAI()

    responce = client.completinons.create(
        model="gpt-3.5-turbo-instruct",  
        prompt=prompt,  
        max_tokens = 1000 
    )

    return responce.choices[0].text
# Function to save data to a JSON file
def save_data(data, filename="user_data.json"):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=7)

# Streamlit app
def main():
    if 'full_prompt' not in st.session_state:
        st.session_state.full_prompt=""
    if 'gpt3_response' not in st.session_state:
        st.session_state.gpt3_response=""

    if 'user_data.json' not in st.session_state:
        file_name="user_data.json"
        st.session_state.user_data_json = ""


    st.title("User Information Form")
    file_name = "user_data.json"
    st.session_state.user_data_json = str(save_data_as_json(file_name))
    user_data = save_data(file_name)

    user_prompt = st.text_input("Enter your prompt for GPT-3.5")  
    button = st.button("Send Data to GPT-3.5") 

    # if button:
    #     full_prompt = str(st.session_state.user_data_json) + user_prompt  
    #     gpt3_response = call_gbt3(full_prompt)  
    #     st.write(gpt3_response)  


    with st.form("user_info_form",clear_on_submit=True):
        name = st.text_input("Name")
        age  =st.number_input("Age" ,placeholder="insert the age",value=None)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        interest = st.text_area("Interest")
        work =st.text_input("work" ,placeholder="goverment or private")
        salary=st.number_input("salary",placeholder="enter your salary")
        dob = st.date_input("Date of Birth")
        religion = st.text_input("Religion")
        photo = st.file_uploader("Upload a photo")


        if name and age and gender and interest and work and salary and dob and religion and photo:
            submitted = st.form_submit_button("Submit")
            if submitted:
                user_data = {
                    "name": name,
                    "age":age,
                    "gender": gender,
                    "interest": interest,
                    "work":work,
                    "salary":salary,
                    "dob": dob.strftime("%Y-%m-%d"),
                    "religion": religion,
                    "photo": photo.read()
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
