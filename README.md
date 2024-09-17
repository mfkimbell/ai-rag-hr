# ai-rag-hr

pip3 install flask-sqlalchemy

pip3 install pypdf

pip3 install faiss-gpu

or

pip3 install faiss-cpu

pip install -U langchain-community

docker build -t ai-rag-doc .


docker run -p 8501:8501 --env-file .env --name ai-rag-doc ai-rag-doc
