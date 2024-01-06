import json


class GeoData:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)

    def get_dados(self):
        return self.data

    def filter_per_area(self, area_min, area_max):
        data_filter = [
            feature
            for feature in self.data['features']
            if area_min <= feature['properties']['AREA_KM2'] <= area_max
        ]
        return {'type': 'FeatureCollection', 'features': data_filter}
