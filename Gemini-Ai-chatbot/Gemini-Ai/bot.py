import google.generativeai as genai

def generate(prompt):
    genai.configure(api_key='AIzaSyBoBHDL2yCZucWFP2zKrbUimA8B90bhmps')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


