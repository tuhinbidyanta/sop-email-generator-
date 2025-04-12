import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import time

'''
Write a '{option[0]}' for a student name Tuhin Bidyanta on the topic '{topic}' {add}. "
              "Make it professional and well-structured.
'''

link ='https://scholar.google.co.in/citations?user=meyQexUAAAAJ&hl=en'
add =' I am studing in MSc tech in applied geophysics in IIT Dhanbad and lookong for internship'
option = ['statement of purpose', 
          'mail to professor not use the word Dear use Respected Sir / mam with Subject name of mail', 
          'research proposal', 
          'cover letter']

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
        print("Error fetching webpage:", e)
        time.sleep(6)  # Wait for 6 seconds before retrying
        return []

def generate_sop(topic):
    genai.configure(api_key="AIzaSyDSGJ9xFQ3hPkANXoDppFtX5eEXkBsEAew")
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = (f"Write a '{option[1]}' for me.  My name is Tuhin Bidyanta {add} on the topic '{topic}' . "
              "Make it professional and well-structured.")
    response = model.generate_content(prompt)
    return response.text if response else "Failed to generate SOP."

# def main():
#     url = link # Replace with the actual URL
#     topics = extract_text_from_class(url)
    
#     if not topics:
#         print("No topics found.")
#         return
#     # dedicated SOP generation for each topic
#     '''
#     for topic in topics:
#         print(f"\nSOP for topic: {topic}\n")
#         print(generate_sop(topic))
#         print("-" * 80)
#     '''
#     # SOP generation for all topics at once
#     all_topics = "\n".join(topics)
#     print(f"\nSOP for all topics: {all_topics}\n")
#     print("-" * 80)
#     print(generate_sop(all_topics))
#     print("-" * 80)

# if __name__ == "__main__":
#     main()
