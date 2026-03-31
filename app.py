import os 
from dotenv import load_dotenv
load_dotenv()   
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
api_key=os.getenv("OPENAI_API_KEY")
os.environ["USER_AGENT"] = "langchain-rag-app"


# Initialize the OpenAI LLM
llm=ChatOpenAI(
    openai_api_key=api_key,
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=1000
)


import warnings
warnings.filterwarnings("ignore")

#creating embeddings

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-small"
)



from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


# Scraping data from website
import bs4
loader= WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title","post-header"),
        )
    ),
)

docs=loader.load()


#Convert the documents into chunks
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

splits=text_splitter.split_documents(docs)

vector_store = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


#prompt template
system_prompt = (
    "You are a strict question answering assistant. "
    "Answer ONLY using the provided context. "
    "If the answer is not in the context, say 'I don't know'. "
    "DO NOT use your own knowledge.\n\n"
    "{context}"
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)


# Create the chain
question_answer_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)


# Building the Streamlit app
import streamlit as st

st.title("Website AI Assistant (RAG-Based)")
st.write(""" This chatbot answers questions based on the following website:
         
🔗 https://lilianweng.github.io/posts/2023-06-23-agent/

Answers are limited to this content. Unrelated questions → 'I don't know'.""")

question = st.text_input("Enter your question:")




if question:
    response=rag_chain.invoke({"input": question})
    st.write("Answer:")
    st.write(response["answer"])