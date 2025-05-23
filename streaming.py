import os
from agents import Agent , Runner , OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled
from  dotenv import load_dotenv
import asyncio

load_dotenv()

# Set Provider, Base URL and API Key
provider = AsyncOpenAI(
        api_key = os.getenv("GIMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Creating model and configure model
model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash-exp",
        openai_client = provider     
)
async def Aiagent(user_input):                    # Create async func()
    # Creating Agent
    MyAgent = Agent(name = "Assistant", instructions = "You will response to the user query.", model = model)
    # Running Agent
    response = await Runner.run(starting_agent=MyAgent, input=user_input)

    return(response.final_output)     # Generate Response

result = asyncio.run(Aiagent("Hello, tell me about Pakistan in 3 lines?"))
print(result)                  # Run async func()

# Disable the OpenAPI Tracing because we use Gemini API
set_tracing_disabled(disabled = True)