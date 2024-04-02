from pydantic import BaseModel, Field


class RouteModel(BaseModel):
    orig_lon: str = Field(
        ...,
        description="The route origin longitude value",
    )
    orig_lat: str = Field(
        ...,
        description="The route origin latitude value",
    )
    dest_lon: str = Field(
        ...,
        description="The route destination longitude value",
    )
    dest_lat: str = Field(
        ...,
        description="The route destination latitude value",
    )
    route: str = Field(
        ...,
        description="The route from origin to destination",
    )
