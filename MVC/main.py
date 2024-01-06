from controller.map_controller import MapController


def main():
    file_path = '../data/sampa_zona_urb.geojson'
    controller = MapController(file_path)
    controller.display_map()

    controller.filter_area()


if __name__ == '__main__':
    main()
