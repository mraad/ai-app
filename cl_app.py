#
# nohup chainlit run cl_app.py &> chainlit.log &
#
import chainlit as cl

from geo.assistants.geocode import get_geocode_assistant


@cl.on_chat_start
async def _on_chat_start():
    assistant = get_geocode_assistant(debug_mode=True)
    cl.user_session.set("assistant", assistant)
    print("Started")


@cl.on_chat_end
async def _on_chat_end():
    print("Ended")


@cl.on_message
async def _on_message(message: cl.Message):
    assistant = cl.user_session.get("assistant")
    # res = assistant.run(f"# OBJECTIVE #{message.content}")
    res = assistant.run(message.content)
    # Send a response back to the user
    await cl.Message(
        content=str(res),
    ).send()
