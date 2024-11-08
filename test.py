from langchain_community.graphs import Neo4jGraph
from src.constants import NEO4J_USERNAME, NEO4J_PASSWORD, NEO4J_URI, COHERE_EMBEDDING_SIZE, STACK_OVERFLOW_NUM_PAGE
from src.llm.gemini_utils import get_llm
from src.api.stackoverflow_utils import search_stackoverflow_with_tags
from src.model.neo4j_utils import insert_so_data
from src.chains import get_vector_chain, get_qa_rag_chain
from src.llm.embedding_model import MyEmbeddingModel



if __name__=="__main__":
    neo4j_graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD)
    embedding_model = MyEmbeddingModel()
    create_vector_index(neo4j_graph, COHERE_EMBEDDING_SIZE)
    create_constraints(neo4j_graph)
    llm = get_llm()
    # load_so_data(neo4j_graph, embedding_model, num_page=1)
    qa = get_qa_rag_chain(llm, embedding_model, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
    result = qa(
        {"question": "How to delete everything in neo4j"})["answer"]
    print(result)
