import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureSearch
from langchain.document_loaders import DirectoryLoader 
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

load_dotenv()

openai.api_type = "azure"
openai.api_base = OPENAI_API_BASE
openai.api_key = OPENAI_API_KEY
openai.api_version = OPENAI_API_VERSION

llm = AzureChatOpenAI(deployment_name = "gpt-4", openai_api_key = OPENAI_API_KEY, openai_api_base = OPENAI_API_BASE, openai_api_version = OPENAI_API_VERSION)
embeddings = OpenAIEmbeddings(deployment = "text-embedding-ada-002", chunk_size = 1, openai_api_key = OPENAI_API_KEY, openai_api_base = OPENAI_API_BASE, openai_api_version = OPENAI_API_VERSION)

acs = AzureSearch(azure_search_endpoint = AZURE_AI_SEARCH_SERVICE_NAME, azure_search_key = AZURE_AI_SEARCH_API_KEY, index_name = AZURE_AI_SEARCH_INDEX_NAME, embedding_function = embeddings.embed_query)