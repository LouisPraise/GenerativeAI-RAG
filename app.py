import streamlit as st
import os
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

st.set_page_config(page_title="My courses assistant", page_icon="🎓")
st.title("🎓 IA Assistant- My courses")

# my model
@st.cache_resource
def load_query_engine():
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    
    # Protecting my grop key api
    api_key = st.secrets["GROQ_API_KEY"] 
    llm = Groq(model="llama-3.3-70b-versatile", api_key=api_key)
    
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context, embed_model=embed_model)
    
    return index.as_query_engine(llm=llm, streaming=True)


query_engine = load_query_engine()

# I'd like the model generate me the history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user interface
if prompt := st.chat_input("YOUR QUESTION..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        response = query_engine.query(prompt)
        
        for chunk in response.response_gen:
            full_response += chunk
            placeholder.markdown(full_response + "▌")
        
        placeholder.markdown(full_response)

        # courses REFERENCES
        with st.expander("📚 REFERENCES"):
            for source in response.source_nodes:
                file_name = source.node.metadata.get('file_name', 'Source inconnue')
                score = round(source.score, 2)
                st.write(f"**Fichier :** {file_name} (Pertinence : {score})")
                st.caption(f"Extrait : {source.node.get_content()[:200]}...")
                st.divider()

        st.session_state.messages.append({"role": "assistant", "content": full_response})
