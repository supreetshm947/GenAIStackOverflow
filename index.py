import streamlit as st
from stackoverflow_utils import search_stackoverflow_with_query, search_stackoverflow_with_tags
from db_utils import save_to_postgres, save_vector_to_qdrant, retrieve_similar_vectors, get_post_by_question_id
from cohere_utils import get_embeddings_for_query
from gemini_utils import get_answer_for_query
from constants import VECTOR_SEARCH_THRESHOLD

st.title("Stack Overflow Q&A Assistant")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    with st.spinner("Searching for answers..."):
        if query and query.strip() != "":
            # Step 1: Searching for similar vectors in the database
            with st.spinner("Searching for similar vectors in the database..."):
                vector_query = get_embeddings_for_query(query)
                similar_vectors = retrieve_similar_vectors(vector_query, VECTOR_SEARCH_THRESHOLD)

            # Step 2: If similar vectors are not found, retrieving relevant posts from the API
            if len(similar_vectors) < 2:
                with st.spinner("No similar vectors found, fetching relevant posts from Stack Overflow..."):
                    results_query = search_stackoverflow_with_query(query) or []
                    results_tag = search_stackoverflow_with_tags(query) or []
                    results = list(set(results_query + results_tag))

                    # Step 3: Saving new posts to the database and updating Qdrant with vector embeddings
                    with st.spinner("Processing retrieved posts..."):
                        for post in results:
                            question_id = post.question_id
                            question_title = post.title
                            save_to_postgres(post)
                            vector_embedding = get_embeddings_for_query(question_title)
                            save_vector_to_qdrant(question_id, vector_embedding)

                    # Step 4: Recomputing similar vectors after saving new posts
                    with st.spinner("Getting best matching posts..."):
                        similar_vectors = retrieve_similar_vectors(vector_query, VECTOR_SEARCH_THRESHOLD)

            # Step 5: Collecting related posts based on similar vectors
            with st.spinner("Gathering related posts data from DB..."):
                related_posts = []
                for vector in similar_vectors:
                    related_posts.append(get_post_by_question_id(vector.id))

            # Step 6: Using LLM to get the answer for the query based on related posts
            with st.spinner("Generating an answer based on the related posts..."):
                llm_output = get_answer_for_query(query, related_posts)

            # Step 7: Displaying the final results or warning if no results found
            if llm_output:
                st.success("Here are the results:")
                st.markdown(llm_output)
            else:
                st.warning("No results found.")
        else:
            st.warning("Please provide a query.")

