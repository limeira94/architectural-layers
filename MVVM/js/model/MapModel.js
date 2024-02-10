
class MapModel {
    constructor() {
        this.polygons = [];
        this.polylines = [];
        this.points = [];
    }

    storePolygonCoordinates(coordinates) {
        this.polygons.push(coordinates);
        console.log('Storing polygon coordinates:', coordinates);
    }

    storePolylineCoordinates(coordinates) {
        this.polylines.push(coordinates);
        console.log('Storing polyline coordinates:', coordinates);
    }

    storeMarkerCoordinates(coordinates) {
        this.points.push(coordinates);
        console.log('Storing point coordinates:', coordinates);
    }

}