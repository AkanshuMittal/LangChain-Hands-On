from dotenv import load_dotenv
load_dotenv()

## db, llm, tools, create_agent, system_prompt
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

db = SQLDatabase.from_uri("sqlite:///tasks.db")
db.run("""
       CREATE TABLE IF NOT EXISTS tasks (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT NOT NULL,
           description TEXT,
           status TEXT check (status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       );
""")

print("Table created successfully")