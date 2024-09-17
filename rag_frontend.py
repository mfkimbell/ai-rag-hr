# The below frontend code is provided by AWS and Streamlit.
import streamlit as st 
import rag_backend as demo 

st.set_page_config(page_title="Document Q & A with RAG") ### Modify Heading

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Document Q & A with RAG 📄</p>'
st.markdown(new_title, unsafe_allow_html=True) 

if 'vector_index' not in st.session_state: 
    with st.spinner("🧙 All we have to decide is what to do with the time that is given us - Gandalf"): ###spinner message
        st.session_state.vector_index = demo.doc_index() 

input_text = st.text_area("Input text", label_visibility="collapsed") 
go_button = st.button("Search", type="primary") 

if go_button: 
    
    with st.spinner("🧙 Not all who wander are lost - Gandalf"): 
        response_content = demo.doc_rag_response(index=st.session_state.vector_index, question=input_text) ### replace with RAG Function from backend file
        st.write(response_content) 