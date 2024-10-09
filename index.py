import streamlit as st
from stackoverflow_utils import search_stackoverflow
from gemini_utils import get_keywords_from_query


st.title("Stack Overflow Q&A Assistant")
query = st.text_input("Enter your question:")

if st.button("Submit"):
    with st.spinner("Searching for answers..."):
        keywords = get_keywords_from_query(query)
        results = search_stackoverflow(query, pagesize=100)

    # Display results
    if results:
        st.success("Here are the results:")
        for idx, item in enumerate(results):
            st.markdown(f"**{idx + 1}. Title:** [{item['title']}]({item['link']})")
            st.markdown(f"   - **Score:** {item['score']}  - **Answer Count:** {item['answer_count']}")
    else:
        st.warning("No results found.")

