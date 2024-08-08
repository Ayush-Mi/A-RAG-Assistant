from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings


class Assistant:
    def __init__(self, db_path):
        self.embeddings = OllamaEmbeddings(model='llama3')
        self.db = Chroma(persist_directory=db_path,
                         embedding_function= self.embeddings)
        self.model = OllamaLLM(model='llama3')
        
    def query(self, question):
        results = self.db.similarity_search_with_relevance_scores(question, k=3)
        prompt = self.create_prompt(results, question)
        answer = self.llm_response(prompt)
        return answer
    
    def create_prompt(self, results, question):
        PROMPT_TEMPLATE = """
        Answer the question based only on the following context:
        {context}
        ---
        Answer the question based on the above context: {question}
        """

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=question)
        return prompt
    
    def llm_response(self,prompt):
        response = self.model.predict(prompt)
        return response