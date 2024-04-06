



prompt_template = """
Use the following information to answer the user question. 
If you need more information, please ask the user for clarification.
If you cannot find the answer, please let the user know, do not try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful Answer:
"""