from model.model_geo import GeoData
from view.view_map import MapGUI


class MapController:
    def __init__(self, file_path):
        self.model = GeoData(file_path)
        self.view = MapGUI()

    def display_map(self):
        self.model.load_data()
        data = self.model.get_dados()
        self.view.create_map(data)

    def filter_area(self):
        area_min, area_max = self.view.request_area()
        data_filter = self.model.filter_per_area(area_min, area_max)
        self.view.create_map(data_filter)
