# Medical-Chatbot-Using-Llama2

## Problem Statement:
The healthcare industry faces challenges in providing accessible and timely medical advice to individuals seeking information about their health concerns. Many people may hesitate to visit healthcare professionals due to various reasons, including time constraints, financial limitations, or simply not wanting to bother medical professionals for minor issues. Some individuals even go as far as relying on potentially unreliable sources on the internet. To address this issue, I developed a medical chatbot that can provide accurate and reliable medical advice to users based on their symptoms and medical history. It would provide relevant information in a conversational manner helping users manage their health concerns and making timely and informed decisions about their well-being.


## Steps to run the project

Clone the repository:
```bash
Project repo: https://github.com/
```

Set Up Virtual Environment:
```bash
python -m venv mchatbot
```

Activate Virtual Environment:
```bash
mchatbot\Scripts\activate
```

Install Dependencies:
```bash
pip install -r requirements.txt
```

Create a .env file in the root directory.
Add your Pinecone credentials:
```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
Download the Llama 2 Model from the provided link in the "model" folder.
Keep the model in the model directory.

Run Setup Script:
```bash
python store_index.py
```

Run the Application
```bash
python app.py
```

Access the Application:

Open your web browser and go to localhost.

## Tech Stack:
- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone