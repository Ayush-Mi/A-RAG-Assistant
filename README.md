# A RAG Assistant

A RAG Assistant is a chatbot application built with Python, utilizing the `Llama3` and `langchain` where the information is retrieved from a document and the user can ask questions related to it. All the data processing happens on the local system and no data is sent to the cloud.

## Dataset
The application uses Llama3 on a dataset collected from Abraham Lincoln Administration 1861's commencement speeech titled [At the Commencement of the Second Session of the Thirty-seventh Congress](https://history.state.gov/historicaldocuments/lincoln)

![](https://static.history.state.gov/frus/frus1861/covers/frus1861.jpg)

## Usage

To run the chatbot application make sure to install Llama3 with Ollama by following instructions from [here]([https://ollama.com/](https://ollama.com/library/llama3))

Install the following via pip:
1. langchain
2. langchain_community
3. langchain_ollama
4. "unstructured[pdf]"

Run the `demo.ipynb` notebook to create a vector embedding of the document and then query it.

The chatbot app was built using code from chatGPT with few customisation as per the application requirement. To run the chatbot, execute the following command from the project folder location in terminal `python chat.py`

## Demo
| |  |  |
|----------|----------|----------|
|![Image1](https://github.com/Ayush-Mi/A-RAG-Assistant/blob/main/img/img1.png) | ![Image1](https://github.com/Ayush-Mi/A-RAG-Assistant/blob/main/img/img2.png) | ![Image1](https://github.com/Ayush-Mi/A-RAG-Assistant/blob/main/img/img3.png)|
## Project Structure

Here's a brief overview of the project structure:

- `chat.py`: The main script to start the chatbot application.
- `assistant.py`: Contains the logic for querying the chatbot and processing responses.
- `create_db.py`: Contains the code to create a vector embedding database in ChromaDB using Llama3 embeddings
- `ref_books/`: A directory containing all the reference books or data to answer a query
- `db_path/`: ChromaDB database containing the vector embedding. This is created once the vector embeddings are extracted

## References

- [Office of Historians](https://history.state.gov/historicaldocuments/lincoln)
- [Ollama](https://ollama.com/library/llama3)
- [Llama3](https://ai.meta.com/blog/meta-llama-3/)
- [ChatGPT](https://openai.com/chatgpt/)
- [LangChain](https://langchain.com/)

