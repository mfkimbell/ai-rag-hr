# ai-rag-pdf

### Architechture
<img width="1205" alt="rag_arch" src="https://github.com/user-attachments/assets/29c9b5a1-cdb1-4007-874b-447f282145f9">

### Demo

![demo-ezgif com-speed](https://github.com/user-attachments/assets/da96d8f1-0f08-40f1-9b09-fe73a8690cb2)

### Tools Used

* `PyPDFLoader` - Lanchain library for loading pdf data
* `FAISS` - Vector Storage and simliarity search through Langchain
* `Titan Text v1` - Creating text embeddings
* `Bedrock` - LangChain module for integrating with AWS Bedrock for LLM interactions.
* `Streamlit` - Framework for building interactive web applications (particularly in data science)
* `Docker` - Containerization platform used for running the application locally.
* `Claude-v2` - Large language model used

### Local Testing

To test the application locally, follow these steps:

1. **Clone the repo:**
   
```bash
git clone https://github.com/mfkimbell/ai-rag-hr.git
```

2. **Pull the Docker Image:**

    ```bash
    docker pull mfkimbell/ai-rag-doc:latest
    ```

2. **Run the Docker Container:**

    ```bash
    docker run --env-file .env -p 8501:8501 mfkimbell/ai-rag-doc:latest
    ```

    Ensure that you have a `.env` file with the necessary environment variables.

`AWS_ACCESS_KEY_ID`
`AWS_SECRET_ACCESS_KEY`
`AWS_DEFAULT_REGION`

3. **Access Webapp**

   ```http://0.0.0.0:8501/```
   or
   ```http://localhost:8501/```


