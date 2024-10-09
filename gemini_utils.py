from langchain_google_genai import ChatGoogleGenerativeAI
from constants import GEMINI_KEY
from langchain_core.prompts import ChatPromptTemplate


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
