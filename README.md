# Medical-Chatbot-Using-Llama2

## Introduction
# Medical-Chatbot-Using-Llama2

## Introduction
Welcome to the Medical Chatbot project! This chatbot is designed to assist you with your medical queries by providing services such as disease diagnosis and medication suggestions.


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