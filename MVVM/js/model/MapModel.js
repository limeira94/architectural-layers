
class MapModel {
    constructor() {
        this.polygons = [];
        this.polylines = [];
        this.points = [];
    }

    storePolygonCoordinates(coordinates) {
        this.polygons.push(coordinates);
    }

    storePolylineCoordinates(coordinates) {
        this.polylines.push(coordinates);
    }

    storeMarkerCoordinates(coordinates) {
        this.points.push(coordinates);
    }
}