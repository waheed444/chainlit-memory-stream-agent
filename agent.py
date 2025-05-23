import chainlit as cl
from streaming import Aiagent

@cl.on_chat_start     # Use Decorator
async def on_chat_start():
    # Your custom logic goes here...
    cl.user_session.set("history",[])
    await cl.Message(content = "I am your AI Assistant!").send()
    
@cl.on_message     # Use Decorator
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    
    user_input = message.content
    history.append({"role" : "user" , "content" : user_input})
    response = await Aiagent(history)
    history.append({"role" : "Assistant" , "content" : response})
    # Send a response back to the user
    await cl.Message(content=f"Agent: {response}").send()
    