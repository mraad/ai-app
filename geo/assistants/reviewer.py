from phi.assistant import Assistant
from phi.llm.ollama import Ollama


def get_reviewer_assistant(
        model: str = "mistral",
        temperature: float = 0.0,
) -> Assistant:
    return Assistant(
        name="reviewer_assistant",
        role="Review the final output of a team assistant to make sure the output in a JSON format",
        llm=Ollama(model=model, options={"temperature": temperature}),
        description="""
        You are an assistant that reviews the final output of a team assistant to make sure the output in a JSON format.
        """,
        debug_mode=True,
    )
