from phi.assistant.team import Team
from phi.knowledge import AssistantKnowledge

from geo.assistants.geocode import get_geocode_assistant
from geo.assistants.near import get_near_assistant
from geo.assistants.reviewer import get_reviewer_assistant
from geo.assistants.route import get_route_assistant


def get_geo_team(
        knowledge_base: AssistantKnowledge,
        debug_mode: bool = False,
) -> Team:
    team = Team(name="geo_team",
                assistants=[
                    get_geocode_assistant(debug_mode=debug_mode),
                    get_route_assistant(debug_mode=debug_mode),
                    get_near_assistant(knowledge_base, debug_mode=debug_mode),
                ],
                # reviewer=get_reviewer_assistant(),
                debug_mode=debug_mode)
    return team
