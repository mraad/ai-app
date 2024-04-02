import json

from phi.tools import Toolkit


class NearTools(Toolkit):
    def __init__(self):
        super().__init__(name="near_tools")

        self.register(self.near_url)

    def near_url(
            self,
            longitude: str,
            latitude: str,
            url: str,
    ) -> str:
        """Find the nearest feature in a spatial layer given a longitude and latitude value.

        :param longitude: The longitude to search nearby.
        :param latitude: The latitude to search nearby.
        :param url: The URL of the spatial layer to search.
        :return: The nearest feature as a JSON document.
        """
        # call arcgis FC.....
        doc = {
            "name": "Near Location",
            "longitude": longitude,
            "latitude": latitude,
        }
        return json.dumps(doc)
