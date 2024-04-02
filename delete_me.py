import json

from phi.document import Document
from phi.embedder.ollama import OllamaEmbedder
from phi.knowledge.document import DocumentKnowledgeBase
from phi.vectordb.qdrant import Qdrant

from geo.assistants.geocode import get_geocode_assistant
from geo.teams.geo import get_geo_team


def _main_team() -> None:
    embedder = OllamaEmbedder(model="nomic-embed-text", dimensions=768)
    vector_db = Qdrant("doccol", location=":memory:", embedder=embedder)
    doc1 = Document(
        content=json.dumps(
            {
                "description": "Point layer containing active and past forest fires",
                "url": "http://localhost/fires",
            }
        ),
    )

    doc2 = Document(
        content=json.dumps(
            {
                "description": "Linestring layer containing rivers and creeks",
                "url": "http://localhost/rivers",
            }
        ),
    )
    documents = [doc1, doc2]
    knowledge_base = DocumentKnowledgeBase(documents=documents, vector_db=vector_db)
    knowledge_base.load()

    assistant = get_geo_team(knowledge_base, debug_mode=True)
    res = assistant.run("""What is the river near Beirut, Lebanon?""", stream=False
                        )
    print(res)


def _main_geocode() -> None:
    assistant = get_geocode_assistant(debug_mode=True)
    print(assistant.run("Geocode Beirut, Lebanon", stream=False))


if __name__ == "__main__":
    _main_geocode()
