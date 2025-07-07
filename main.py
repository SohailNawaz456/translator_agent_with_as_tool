# Import necessary classes from your agent framework
from agents import Agent, Runner
from connection import config

# ------------------------------
# Step 1: Define individual translator agents
# Each agent specializes in translating English to one specific language
# ------------------------------

italian_agent = Agent(
    name="Italian Translator",
    instructions="Translate any English text into Italian"
)

french_agent = Agent(
    name="French Translator",
    instructions="Translate any English text into French"
)

german_agent = Agent(
    name="German Translator",
    instructions="Translate any English text into German"
)

# ------------------------------
# Step 2: Define the main routing agent
# This agent decides which language agent to use based on user request
# ------------------------------

translation_router = Agent(
    name="Translation Router",
    instructions="""
    You are a translation assistant. Route the translation request to the correct language agent.
    Use the appropriate tool to convert English text into either Italian, German, or French based on the request.
    """,
    tools=[
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian"
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French"
        ),
        german_agent.as_tool(
            tool_name="translate_to_german",
            tool_description="Translate the user's message to German"
        )
    ]
)

# ------------------------------
# Step 3: Execute a translation request using the router agent
# The request asks for translation into Italian.
# The router agent will choose the correct tool based on the prompt.
# ------------------------------

result = Runner.run_sync(
    translation_router,
    "Translate 'I Love Learning' into italian",
    run_config=config
)

# ------------------------------
# Step 4: Print the final translated output
# ------------------------------
print(result.final_output)
