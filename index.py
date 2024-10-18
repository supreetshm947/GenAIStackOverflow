import streamlit as st
from stackoverflow_utils import search_stackoverflow
from db_utils import save_to_postgres, save_vector_to_qdrant, retrieve_similar_vectors, get_post_by_question_id
from cohere_utils import get_embeddings_for_query
from gemini_utils import get_answer_for_query

st.title("Stack Overflow Q&A Assistant")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    with st.spinner("Searching for answers..."):
        if query or not query.strip()=="":
            results = search_stackoverflow(query)
            for post in results:
                save_to_postgres(post)
                question_id = post['question_id']
                question_title = post['title']
                vector_embedding = get_embeddings_for_query(question_title)
                save_vector_to_qdrant(question_id, vector_embedding)

            vector_query = get_embeddings_for_query(query)
            similar_vectors = retrieve_similar_vectors(vector_query)

            related_posts = []
            for vector in similar_vectors:
                related_posts.append(get_post_by_question_id(vector.id))

            llm_output = get_answer_for_query(query, related_posts)

            if llm_output:
                st.success("Here are the results:")
                st.text(llm_output)
                # for idx, item in enumerate(results):
                #     st.markdown(f"**{idx + 1}. Title:** [{item['title']}]({item['link']})")
                #     st.markdown(f"   - **Score:** {item['score']}  - **Answer Count:** {item['answer_count']}")
            else:
                st.warning("No results found.")
        else:
            st.warning("Please provide a query.")


