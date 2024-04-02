from textwrap import dedent

from phi.assistant import Assistant
from phi.knowledge.base import AssistantKnowledge
from phi.llm.ollama import Ollama

from geo.models.near import NearModel
from geo.tools.near import NearTools


def get_near_assistant(
        knowledge_base: AssistantKnowledge,
        model: str = "mistral",
        temperature: float = 0.0,
        debug_mode: bool = False,
) -> Assistant:
    return Assistant(
        name="near_assistant",
        role="find the nearest feature in a spatial layer url",
        llm=Ollama(model=model, options={"temperature": temperature}),
        description=dedent("""
        You are an assistant that can find places near given longitude and latitude coordinates.
        You do this by finding the nearest feature in a spatial layer url.
        """),
        output_model=NearModel,
        tools=[NearTools()],
        use_tools=True,
        show_tool_calls=True,
        prevent_prompt_injection=True,
        knowledge_base=knowledge_base,
        add_references_to_prompt=True,
        debug_mode=debug_mode,
    )
