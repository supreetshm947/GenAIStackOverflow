from langchain_google_genai import ChatGoogleGenerativeAI
from src.constants import GEMINI_KEY
from langchain_core.prompts import ChatPromptTemplate
# from src.utils import escape_curly_braces


def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        google_api_key=GEMINI_KEY
    )
    return llm


def get_answer_for_query(query, posts):
    llm = get_llm()

    system_message = (
        "You are an assistant specialized in providing answers based solely on the provided Stack Overflow posts. "
        "Do not use your general knowledge or assumptions. Use the content from the posts to formulate your answer."
        "If there are no posts provided, simply say you dont know the answers, dont make it up."
        "It could be that the provided posts do not provide a clear context for the asked query or talk about completely different, "
        "in that case apologize and tell user you only have details regarding the context of most relevant gathered posts and make up an answer based on it."
        "In the end, provide a further reading section where you list the links of the Stack overflow posts which you used to answer, so not all just the one you used to construct the answer."
    )

    # Prepare the prompt template with the system message and the user query

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human",
             f"{query}\n\nHere are the related Stack Overflow posts:\n" + "\n".join(escape_curly_braces(str(post)) for post in posts)),
        ]
    )

    chain = prompt | llm
    out = chain.invoke(
        {
            "input": query,
        }
    )

    return out.content



def get_keywords_from_query(query):
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Extract the keywords from the given query and just return the Keywords as list.",
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm
    out = chain.invoke(
        {
            "input": query,
        }
    )

    return eval(out.content)