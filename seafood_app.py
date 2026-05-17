import os
import google.genai as genai
import pandas as pd
import numpy as np

def analyze_invoice_with_gemini(image_path, api_key):
    try:
        client = genai.Client(api_key=api_key)
        uploaded_file = client.files.upload(file=image_path)
        prompt = 'Analyze invoice and extract items.'
        response = client.models.generate_content(model='gemini-2.5-flash', contents=[uploaded_file, prompt])
        client.files.delete(name=uploaded_file.name)
        return response.text
    except Exception as err:
        return f'Error: {str(err)}'
