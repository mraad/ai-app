import json

from phi.tools import Toolkit


class RouteTools(Toolkit):
    def __init__(self):
        super().__init__(name="route_tools")

        self.register(self.route_fastest)
        self.register(self.route_safest)

    def route_fastest(
            self,
            orig_lon: str,
            orig_lat: str,
            dest_lon: str,
            dest_lat: str,
    ) -> str:
        """Use a routing service to get the fastest route from origin longitude, latitude
        to destination longitude, latitude.

        :param orig_lon: The origin longitude.
        :param orig_lat: The origin latitude.
        :param dest_lon: The destination longitude.
        :param dest_lat: The destination latitude.
        :return: The fastest route as a JSON document.
        """
        doc = {
            "orig_lon": orig_lon,
            "orig_lat": orig_lat,
            "dest_lon": dest_lon,
            "dest_lat": dest_lat,
            "route": f"Fastest Route from {orig_lat}/{orig_lon} to {dest_lat}/{dest_lon}",
        }
        return json.dumps(doc)

    def route_safest(
            self,
            orig_lon: str,
            orig_lat: str,
            dest_lon: str,
            dest_lat: str,
    ) -> str:
        """Use a routing service to get the safest route from origin longitude, latitude
        to destination longitude, latitude.

        :param orig_lon: The origin longitude.
        :param orig_lat: The origin latitude.
        :param dest_lon: The destination longitude.
        :param dest_lat: The destination latitude.
        :return: The safest route as a JSON document.
        """
        doc = {
            "orig_lon": orig_lon,
            "orig_lat": orig_lat,
            "dest_lon": dest_lon,
            "dest_lat": dest_lat,
            "route": f"Safest Route from {orig_lat}/{orig_lon} to {dest_lat}/{dest_lon}",
        }
        return json.dumps(doc)
