from langchain_community.vectorstores import Neo4jVector
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate
)
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains import RetrievalQAWithSourcesChain

def get_vector_chain(embedding_model, embeddings_store_url, username, password):
    kg = Neo4jVector.from_existing_index(
        embedding=embedding_model,
        url=embeddings_store_url,
        username=username,
        password=password,
        database="neo4j",  # neo4j by default
        index_name="stackoverflow",  # vector by default
        text_node_property="body",  # text by default
        retrieval_query="""
        WITH node AS question, score AS similarity
        CALL {
            WITH question
            MATCH (question)<-[:ANSWERS]-(answer)
            WITH answer
            ORDER BY answer.is_accepted DESC, answer.score DESC
            WITH collect(answer)[..2] AS answers
            RETURN reduce(str='', answer IN answers | str + 
                          '\n### Answer (Accepted: ' + toString(answer.is_accepted) +
                          ' Score: ' + toString(answer.score) + '): ' + answer.body + '\n') AS answerTexts
        }
        RETURN '##Question: ' + question.title + '\n' 
               + COALESCE(answerTexts, 'No answers available') AS text, 
               similarity AS score, 
               {source: question.link} AS metadata
        ORDER BY similarity ASC
        """,
    )

    return kg

def get_qa_rag_chain(llm, embedding_model, embeddings_store_url, username, password):
    general_system_template = """ 
        Use the following pieces of context to answer the question at the end.
        The context contains question-answer pairs and their links from Stackoverflow.
        You should prefer information from accepted or more upvoted answers.
        Make sure to rely on information from the answers and not on questions to provide accurate responses.
        When you find particular answer in the context useful, make sure to cite it in the answer using the link.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        ----
        {summaries}
        ----
        Each answer you generate should contain a section at the end of links to 
        Stackoverflow questions and answers you found useful, which are described under Source value.
        You can only use links to StackOverflow questions that are present in the context and always
        add links to the end of the answer in the style of citations.
        Generate concise answers with references sources section of links to 
        relevant StackOverflow questions only at the end of the answer.
        """
    general_user_template = "Question:```{question}```"
    messages = [
        SystemMessagePromptTemplate.from_template(general_system_template),
        HumanMessagePromptTemplate.from_template(general_user_template),
    ]
    qa_prompt = ChatPromptTemplate.from_messages(messages)

    qa_chain = load_qa_with_sources_chain(
        llm,
        chain_type="stuff",
        prompt=qa_prompt,
    )

    kg = get_vector_chain(embedding_model, embeddings_store_url, username, password)

    kg_qa = RetrievalQAWithSourcesChain(
        combine_documents_chain=qa_chain,
        retriever=kg.as_retriever(search_kwargs={"k": 2}),
        reduce_k_below_max_tokens=False,
        max_tokens_limit=3375,
    )
    return kg_qa