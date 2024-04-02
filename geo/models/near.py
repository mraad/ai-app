from pydantic import BaseModel, Field


class NearModel(BaseModel):
    name: str = Field(
        ...,
        description="The name of the nearest location.",
    )
    latitude: str = Field(
        ...,
        description="The latitude of the nearest location.",
    )
    longitude: str = Field(
        ...,
        description="The longitude of the nearest location.",
    )
