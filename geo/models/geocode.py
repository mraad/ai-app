from pydantic import BaseModel, Field


class GeocodeModel(BaseModel):
    name: str = Field(
        ...,
        description="The name of the geocoded location.",
    )
    latitude: str = Field(
        ...,
        description="The latitude of the geocoded location.",
    )
    longitude: str = Field(
        ...,
        description="The longitude of the geocoded location.",
    )
