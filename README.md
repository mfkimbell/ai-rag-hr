# ai-rag-doc

### Demo

![demo-ezgif com-speed](https://github.com/user-attachments/assets/da96d8f1-0f08-40f1-9b09-fe73a8690cb2)



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


