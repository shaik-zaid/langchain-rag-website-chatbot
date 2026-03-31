# Website AI Assistant

This project is a Retrieval-Augmented Generation (RAG) based AI assistant that answers questions using the content of a specific website.

It extracts information from a given webpage, processes it into embeddings, and uses an LLM to generate accurate, context-based answers.

---

## 🚀 Features

- Ask questions about a specific website
- Uses RAG (Retrieval-Augmented Generation)
- Context-aware answers (no hallucination)
- Returns *"I don't know"* for unrelated queries
- Simple Streamlit-based UI

---

## 🔗 Source Website

This project currently uses:

https://lilianweng.github.io/posts/2023-06-23-agent/

---

## ⚠️ Limitations

- Answers are generated **only from the above website content**
- Unrelated questions will return: *"I don't know"*
- Supports a single website at a time

---

## 🧠 How It Works

1. Load website content using a web loader  
2. Split text into chunks  
3. Convert text into embeddings  
4. Store embeddings in a vector database (Chroma)  
5. Retrieve relevant chunks based on user query  
6. Generate answer using LLM with retrieved context  

---

## ⚙️ Setup

```bash
git clone https://github.com/shaik-zaid/langchain-rag-website-chatbot
cd langchain-rag-website-chatbot

# create environment
conda create -p .venv python=3.10 -y
conda activate .venv/

pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Usage

- Enter a question related to the website content  
- The system retrieves relevant context  
- The LLM generates a grounded answer  

---

## 🔧 Customization

You can use this system with any website by updating the URL in the code:

```python
web_paths=("YOUR_WEBSITE_URL",)
```

---

## 🛠 Tech Stack

- LangChain  
- OpenAI (LLM + Embeddings)  
- ChromaDB  
- Streamlit  
- BeautifulSoup  

---

## 🎯 Project Goal

To demonstrate a simple and reliable RAG pipeline that:
- Uses external knowledge sources  
- Avoids hallucinations  
- Provides transparent and controlled answers  

---

## 📌 Future Improvements

- Multi-website support  
- Chat history / memory  
- Source citation display  
- Upload custom documents (PDF, text)  

---

## 📄 License

This project is for educational purposes.