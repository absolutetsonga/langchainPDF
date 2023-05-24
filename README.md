# Ask Your PDF

This is a Streamlit web application that allows you to upload a PDF file and ask questions about its content. The application extracts text from the PDF, splits it into smaller chunks, creates embeddings for each chunk, and builds a knowledge base. You can then enter a question related to the PDF, and the application will search for relevant information and provide an answer.

## Installation

To run this application, you need to install the required dependencies. You can use the following command to install them:

```shell
pip install -r requirements.txt
```

## Usage

After installing the dependencies, you can run the application using the following command:

```shell
streamlit run app.py
```

This will start the Streamlit development server, and you can access the application in your browser at `http://localhost:8501`.

## How It Works

1. The application starts by loading the necessary libraries and setting up the environment.
2. It provides an interface for uploading a PDF file.
3. Once a PDF file is uploaded, the application extracts the text from the file.
4. The text is split into smaller chunks using the `CharacterTextSplitter` class, which separates the text based on a specified separator, chunk size, and overlap.
5. Embeddings are created for each chunk of text using the `OpenAIEmbeddings` class.
6. The chunks and their embeddings are used to build a knowledge base using the `FAISS` vector store.
7. The user is prompted to enter a question about the PDF.
8. If a question is provided, the application searches the knowledge base for relevant information using the `similarity_search` method.
9. The `load_qa_chain` function is used to load a question-answering chain from the `OpenAI` language model.
10. The question-answering chain is executed with the input documents from the knowledge base and the user's question.
11. The application displays the response to the user's question.

## Dependencies

The following dependencies are required to run this application:

- `dotenv`: A library for loading environment variables from a .env file.
- `PyPDF2`: A library for reading PDF files.
- `langchain`: A library for natural language processing tasks, such as text splitting, embeddings, vector stores, and question-answering.
- `os`: A module for interacting with the operating system.
- `streamlit`: A library for building web applications with Python.

You can find the specific versions of these dependencies in the `requirements.txt` file.

## License

This project is licensed under the MIT License. You can find the full license text in the `LICENSE` file.

## Disclaimer

This application utilizes various libraries and APIs to provide its functionality. Please refer to the documentation of each library and API for their respective terms of use and licenses.

This project is provided as-is, without any warranty or guarantee of its performance or suitability for any purpose. Use it at your own risk.