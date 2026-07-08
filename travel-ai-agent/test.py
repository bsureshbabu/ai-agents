from llm.ollama_client import get_llm

llm = get_llm()

response = llm.invoke("Hello")

print(response.content)