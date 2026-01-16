from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while True:
    query = input("User: ")

    if query.lower() in ["quit","bye","exit"]:
        print("GoodBye")
        break

    result = llm.invoke(query)

    print("AI: ", result.content, "\n")


