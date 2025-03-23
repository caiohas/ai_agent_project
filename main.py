from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter as chaves de API do ambiente
openai_api_key = os.getenv('OPENAI_API_KEY')

# Verificar se a chave foi carregada
if not openai_api_key:
    raise ValueError("A chave da OpenAI não foi carregada.")

# Selecionando a versão do LLM
llm_OpenAI = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

# Estrutura correta para o método `invoke`
response1 = llm_OpenAI.invoke([{"role": "user", "content": "O que é o Clube Atlético Mineiro?"}])
print(response1.content)  # Correção: acessando como `.content`
