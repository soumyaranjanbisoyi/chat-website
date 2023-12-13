import os
import streamlit as st
from test2 import WebsiteChatApp
import json
import openai
import constants


api_key = st.secrets.api_credential.openai_key
openai.api_key = api_key
os.environ['OPENAI_API_KEY'] = api_key


def get_individual_answer(question):
    obj = WebsiteChatApp()
    response = obj.get_website_resp(question)
    return response

def get_summarized_answer(question):
    response1 = get_individual_answer(question)
    res_str = '\n\n'.join(list(response1.values()))
    gpt_prompt = f"""Summarize this
    \n\n
    {res_str}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.2,
        max_tokens=250,
        n=10,
        stop=None
    )

    summary = response.choices[0].text.strip()
    print(response.choices)
    return summary




def save_websites_to_session(website_name):
    """Save websites to the session file."""
    session_file_path = "websites_session.json"
    with open(session_file_path, "r") as f:
        data = json.load(f)
    data.append(website_name)

    with open(session_file_path, "w") as f:
        json.dump(data, f)

