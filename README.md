| 프로젝트 기간 | 25.08.12 ~                                                  |
| ------------- | ----------------------------------------------------------- |
| 프로젝트 목적 | ai agent (crewai, autogen, openai sdk, googl adk, langraph) |
| Github        |                                                             |
| Docs          | https://platform.openai.com/docs/pricing                    |
|               |                                                             |

---

- basic

  ```python
  import openai

  client = openai.OpenAI()

  response = client.chat.completions.create(
      model="gpt-5-nano-2025-08-07",  # https://platform.openai.com/docs/pricing
      n=5,
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What is the capital of the moon?"},
      ],
  )

  for choice in response.choices:
      print(choice.message.content)

  ```

- agent의 동작 방식

  ```python
  import openai

  client = openai.OpenAI()

  PROMPT = """
  I have the following functions in my system.

  'get_weather'
  'get_currency'
  'get_news'

  All of them receive the name of a country as an argument (i.e. get_weather('Spain'))

  Please, answer with the name of the function that you would like me to run.

  Please, say nothing else, just the name of the function with the arguments.

  Answer the following question:

  What is the weather in Korea?
  """

  response = client.chat.completions.create(
      model="gpt-5-nano-2025-08-07",  # https://platform.openai.com/docs/pricing
      messages=[
          {"role": "user", "content": PROMPT},
      ],
  )

  ```

- simple chatbot with memory

  ```python
  import openai

  client = openai.OpenAI()
  messages = []
  ```

  ```python
  def call_ai():
      response = client.chat.completions.create(
          model="gpt-5-nano-2025-08-07",
          messages=messages,
      )

      message = response.choices[0].message.content
      messages.append({"role": "assistant", "content": message})
      return message

  ```

  ```python
  while True:
      message = input("Send a message to the LLM...")
      if message == "quit" or message == "q":
          break
      else:
          messages.append({"role": "user", "content": message})
          print(f"User: {message}")
          response = call_ai()
          print(f"Assistant: {response}")
  ```

- tool

  ```python
  import openai
  import json

  client = openai.OpenAI()
  messages = []
  ```

  ```python
  def get_weather(city):
      return f"The weather in {city} is sunny."

  FUNCTION_MAP = {
      "get_weather": get_weather,
  }

  ```

  ```python
  TOOLS = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get the weather in a given city",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "city": {
                          "type": "string",
                          "description": "The name of the city to get the weather for",
                      }
                  },
                  "required": ["city"],
              },
          },
      }
  ]
  ```

  ```python
  from openai.types.chat import ChatCompletionMessage

  def process_ai_response(message: ChatCompletionMessage):
      if message.tool_calls and len(message.tool_calls) > 0:
          messages.append(
              {
                  "role": "assistant",
                  "content": message.content or "",
                  "tool_calls": [
                      {
                          "id": tool_call.id,
                          "type": "function",
                          "function": {
                              "name": tool_call.function.name,
                              "arguments": tool_call.function.arguments,
                          },
                      }
                      for tool_call in message.tool_calls
                  ],
              }
          )

          for tool_call in message.tool_calls:
              function_name = tool_call.function.name
              arguments = tool_call.function.arguments

              print(f"Calling function: '{function_name}' with arguments: {arguments}")

              try:
                  arguments = json.loads(arguments)
              except json.JSONDecodeError:
                  print(f"Error parsing arguments: {arguments}")
                  arguments = {}

              function_result = FUNCTION_MAP[function_name](**arguments)
              print(f"Function result: {function_result}")

              messages.append(
                  {
                      "role": "tool",
                      "tool_call_id": tool_call.id,
                      "name": function_name,
                      "content": function_result,
                  }
              )

          call_ai()

      else:
          messages.append({"role": "assistant", "content": message.content})
          print(f"Assistant: {message.content}")

  def call_ai():
      response = client.chat.completions.create(
          model="gpt-5-nano-2025-08-07",
          messages=messages,
          tools=TOOLS,
      )

      process_ai_response(response.choices[0].message)

  ```

  ```python
  while True:
      message = input("Send a message to the LLM...")
      if message == "quit" or message == "q":
          break
      else:
          messages.append({"role": "user", "content": message})
          print(f"User: {message}")
          call_ai()

  ```

  `
