from textwrap import dedent

from phi.assistant import Assistant
from phi.llm.ollama import Ollama

from geo.models.geocode import GeocodeModel
from geo.tools.geocode import GeocodeTools


def get_geocode_assistant(
        model: str = "mistral",
        temperature: float = 0.0,
        debug_mode: bool = False,
) -> Assistant:
    return Assistant(
        name="geocode_assistant",
        role=dedent("""
        convert an address or a place to a latitude and longitude and
        convert a latitude and longitude to a place or an address.
        """),
        llm=Ollama(model=model, options={"temperature": temperature}),
        description=dedent("""
        You are an assistant with geocoding capabilities.
        You can convert an address or a place to a latitude and longitude and vice versa.
        """),
        output_model=GeocodeModel,
        parse_output=False,
        tools=[GeocodeTools()],
        use_tools=True,
        show_tool_calls=True,
        prevent_prompt_injection=True,
        debug_mode=debug_mode,
    )
