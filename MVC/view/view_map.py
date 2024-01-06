import folium


class MapGUI:
    def create_map(self, geojson_data):
        map_ = folium.Map(location=[-23.5489, -46.6388], zoom_start=11)
        folium.GeoJson(geojson_data).add_to(map_)
        map_.save('map.html')

    def request_area(self):
        try:
            area_min = float(
                input(
                    'Enter the value of the minimum area in km² (for example, 0.5): '
                )
            )

            area_max = float(
                input(
                    'Enter the value of the maximum area in km² (for example, 10.0):'
                )
            )

            return area_min, area_max

        except ValueError:
            print('Please, enter a valid number.')
            return None, None
