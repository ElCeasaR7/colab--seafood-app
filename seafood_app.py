import os
import google.genai as genai

# تهيئة العميل المستقر لعام 2026 واختبار الاتصال
client = genai.Client()

chat = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "temperature": 0,
        "tools": [{"code_execution": {}}]
    }
)
print("Seafood Financial OS Engine is ready on GitHub!")
