from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

class CreateDatabase:
    def __init__(self,data_path, file_type, db_path, chunk_size, chunk_overlap):
        self.data_path = data_path
        self.file_type = file_type
        self.db_path = db_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
    def create(self,):
        loader = DirectoryLoader(self.data_path, 
                                 glob=("*."+self.file_type))
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            add_start_index=True,
            )
        
        chunks = text_splitter.split_documents(documents)
        print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
        
        print("Creating embeddings of those chunks using Llama3...")
        print("This usually takes a lot of time \
            depending upon the system's compute capacity...\
                For 2277 chunks of 1000 size it took 198 mins on\
                    Mac M2 with 24g memory")

        db = Chroma.from_documents(
        chunks, OllamaEmbeddings(model="llama3"), persist_directory=self.db_path
            )

        db.persist()
        print(f"Saved {len(chunks)} chunks to {self.db_path}.")
                
