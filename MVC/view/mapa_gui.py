import folium


class MapaGUI:
    def criar_mapa(self, geojson_data):
        mapa = folium.Map(location=[-23.5489, -46.6388], zoom_start=11)
        folium.GeoJson(geojson_data).add_to(mapa)
        mapa.save('mapa.html')