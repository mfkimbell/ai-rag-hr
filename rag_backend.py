import os
import boto3
from langchain_aws import BedrockEmbeddings, BedrockLLM
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator

def doc_index():
    # Load the PDF document
    data_load = PyPDFLoader('https://resume-mfk.s3.amazonaws.com/09_2024+Mitchell+Kimbell+Resume+.pdf')

    # Split the text using RecursiveCharacterTextSplitter
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=300, chunk_overlap=10)

    # Create embeddings using Bedrock
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-embed-text-v1'
    )

    # Create VectorStore index
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS
    )

    # Create index for Document
    db_index = data_index.from_loaders([data_load])
    return db_index

def doc_llm():
    # Initialize AWS Bedrock Runtime client using Boto3
    client = boto3.client("bedrock-runtime", region_name="us-east-1")  # Use your AWS region

    # Create an instance of BedrockLLM
    llm = BedrockLLM(
        client=client,
        model_id='anthropic.claude-v2',
        model_kwargs={
            "max_tokens_to_sample": 3000,
            "temperature": 0.1,
            "top_p": 0.9
        }
    )
    return llm

def doc_rag_response(index, question):
    rag_llm = doc_llm()
    doc_rag_query = index.query(question=question, llm=rag_llm)
    return doc_rag_query
