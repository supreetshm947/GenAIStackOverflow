from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
KEY=os.getenv("KEY")

COHERE_KEY=os.getenv("COHERE_KEY")

GEMINI_KEY=os.getenv("GEMINI_KEY")
