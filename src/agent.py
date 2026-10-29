from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase

model = ChatGroq(model="openai/gpt-oss-120b")

agent = create_agent(
    model,
    tools=[],
    system_prompt="You are a helpful assistant.",
)

db = SQLDatabase.from_uri("duckdb:////Users/pranavgovindu/College/Research/Summer Research/crash_reports_2023_2026.duckdb")

sql_toolkit = SQLDatabaseToolkit(db=db, llm=model)

sql_agent = create_agent(
    model,
    tools=sql_toolkit.get_tools(),
    system_prompt=(
        "You are an agent designed to interact with a SQL database. "
        "Given an input question, create a syntactically correct DuckDB query, "
        "run it, and return the answer based on the query results. "
        "Always look at the tables in the database first to see what you can query, "
        "then query the schema of the relevant tables before writing a query."
    ),
)