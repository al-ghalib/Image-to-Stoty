import os
import requests
import streamlit as st
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", st.secrets.get("HUGGINGFACEHUB_API_TOKEN"))
HUGGINGFACE_BASE_URL = "https://api-inference.huggingface.co/models/"

def get_headers():
    if not API_TOKEN:
        raise EnvironmentError("Missing Hugging Face API token.")
    return {"Authorization": f"Bearer {API_TOKEN}"}


def call_hf_api(model_path: str, payload=None, data=None, is_binary=False):
    url = f"{HUGGINGFACE_BASE_URL}{model_path}"
    headers = get_headers()

    try:
        if payload:
            response = requests.post(url, headers=headers, json=payload)
        elif data:
            response = requests.post(url, headers=headers, data=data)
        else:
            raise ValueError("Either payload or data must be provided.")

        if response.status_code != 200:
            raise Exception(f"API Error {response.status_code}: {response.text}")

        return response.content if is_binary else response.json()

    except Exception as e:
        raise Exception(f"Failed to call Hugging Face API: {str(e)}")