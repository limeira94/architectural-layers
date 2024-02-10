
class MapViewModel {
    constructor() {
        this.model = new MapModel();
    }

    addPolygon(coordinates) {
        console.log('Polygon coordinates:', coordinates);
        this.model.storePolygonCoordinates(coordinates);
    }

    addPolyline(coordinates) {
        this.model.storePolylineCoordinates(coordinates);
    }

    addMarker(coordinates) {
        this.model.storeMarkerCoordinates(coordinates);
    }


}

