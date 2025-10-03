from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


MODEL = LiteLlm("openai/gpt-5-nano-2025-08-07")


def get_weather(city: str):
    return f"The weather in {city} is sunny."


geo_agent = Agent(
    name="GeoAgent",
    instruction="You help the user with geography related questions",
    model=MODEL,
    description="Transfer to this agent if the user asks about geography related questions",
)


weather_agent = Agent(
    name="WeatherAgent",
    instruction="You help the user with weather related questions",
    model=MODEL,
    tools=[get_weather],
    sub_agents=[geo_agent],
)


root_agent = weather_agent
