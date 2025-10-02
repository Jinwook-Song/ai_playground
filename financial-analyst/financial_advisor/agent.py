from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


MODEL = LiteLlm("openai/gpt-5-nano-2025-08-07")
# MODEL = LiteLlm("openai/gpt-4o")


weather_agent = Agent(
    name="WeatherAgent",
    instruction="You help the user with weather related questions",
    model=MODEL,
)


root_agent = weather_agent
