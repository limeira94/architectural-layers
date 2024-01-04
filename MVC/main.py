from controller.mapa_controller import MapaController


def main():
    file_path = '../data/sampa_zona_urb.geojson'
    controller = MapaController(file_path)
    controller.exibir_mapa()
    

if __name__ == '__main__':
    main()