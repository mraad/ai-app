import json

from phi.tools import Toolkit

from geo.models.geocode import GeocodeModel


class GeocodeTools(Toolkit):
    def __init__(self):
        super().__init__(name="geocode_tools")

        self.register(self.get_lon_lat_from_name)
        self.register(self.get_name_from_lon_lat)

    # def get_lon_lat_from_name(self, name: str) -> str:
    #     """Use a geocoding service to get the latitude and longitude of a given location name.
    #
    #     :param name: The name of the location to geocode.
    #     :return: The latitude and longitude of the location as a JSON document.
    #     """
    #     doc = {
    #         "Paris, France": {"latitude": "48.8566", "longitude": "2.3522"},
    #         "New York, USA": {"latitude": "40.7128", "longitude": "-74.0060"},
    #         "Beirut, Lebanon": {"latitude": "33.8938", "longitude": "35.5018"},
    #     }.get(name, {"latitude": "0.0", "longitude": "0.0"})
    #     # print(">>>>>>>>>>> GET LON LAT FROM NAME <<<<<<<<<<<<")
    #     return json.dumps(doc)

    def get_lon_lat_from_name(self, name: str) -> GeocodeModel:
        """Use a geocoding service to get the latitude and longitude of a given location name.

        :param name: The name of the location to geocode.
        :return: A GeocodeModel instances.
        """
        model = {
            "Paris, France": GeocodeModel(name="Paris", latitude="48.8566", longitude="2.3522"),
            "New York, USA": GeocodeModel(name="New York", latitude="40.7128", longitude="-74.0060"),
            "Beirut, Lebanon": GeocodeModel(name="Beirut", latitude="33.8938", longitude="35.5018"),
        }.get(name, GeocodeModel(name="UNK", latitude="0.0", longitude="0.0"))
        return model

    def get_name_from_lon_lat(self, lon: str, lat: str) -> str:
        """Use a geocoding service to get the nearest location name of a given latitude and longitude.

        :param lon: The longitude of the name to geocode.
        :param lat: The latitude of the name to geocode.
        :return: The name, latitude and longitude as a JSON document.
        """
        lon = float(lon)
        lat = float(lat)
        lut = [{
            "latitude": "48.8566",
            "longitude": "2.3522",
            "name": "Paris, France"
        }, {
            "latitude": "40.7128",
            "longitude": "-74.0060",
            "name": "New York, USA"
        }, {
            "latitude": "33.8938",
            "longitude": "35.5018",
            "name": "Beirut, Lebanon"
        }]

        def _dist2(doc_):
            dy = float(doc_["latitude"]) - lat
            dx = float(doc_["longitude"]) - lon
            return dx * dx + dy * dy

        best = min(lut, key=_dist2)
        # print(">>>>>>>>>> GET NAME FROM LON LAT <<<<<<<<<<<<")
        return json.dumps(best)
