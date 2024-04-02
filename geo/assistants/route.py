from textwrap import dedent

from phi.assistant import Assistant
from phi.llm.ollama import Ollama

from geo.models.route import RouteModel
from geo.tools.route import RouteTools


def get_route_assistant(
        model: str = "mistral",
        temperature: float = 0.0,
        debug_mode: bool = False,
) -> Assistant:
    return Assistant(
        name="route_assistant",
        role="find the fastest or safest route from an origin location to a destination location",
        llm=Ollama(model=model, options={"temperature": temperature}),
        description=dedent("""
        You are an assistant with routing capabilities.
        You can find the fastest or safest route from an origin location to a destination location.
        """),
        output_model=RouteModel,
        tools=[RouteTools()],
        use_tools=True,
        show_tool_calls=True,
        prevent_prompt_injection=True,
        debug_mode=debug_mode,
    )
