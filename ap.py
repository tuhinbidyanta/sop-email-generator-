import requests
import google.generativeai as genai
from bs4 import BeautifulSoup

def extract_text_from_class(url, class_name="gsc_a_t"):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all(class_=class_name)

        texts = [element.get_text(strip=True) for element in elements]
        return texts
    except requests.exceptions.RequestException as e:
        return [f"Error fetching webpage: {e}"]

def generate_sop(topics, additional_prompt="", prompt_type="statement of purpose"):
    genai.configure(api_key="AIzaSyDSGJ9xFQ3hPkANXoDppFtX5eEXkBsEAew")
    model = genai.GenerativeModel("gemini-1.5-flash")

    combined_topics = ", ".join(topics)
    prompt = (f"Write a single comprehensive {prompt_type} for me.My name is Tuhin Bidyanta "
              f"{additional_prompt} "
              f"based on the topics {combined_topics}. "
              "Make it professional and well-structured.")

    response = model.generate_content(prompt)
    return response.text if response else "Failed to generate"
