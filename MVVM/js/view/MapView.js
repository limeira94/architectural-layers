class MapView {
    constructor() {
        this.viewModel = new MapViewModel();
        this.map = this.initializeMap();
        this.addDrawingTools();
    }

    initializeMap() {
        const map = L.map('map').setView([51.505, -0.09], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        return map;
    }

    addDrawingTools() {
        const drawnItems = new L.FeatureGroup();
        this.map.addLayer(drawnItems);

        const drawControl = new L.Control.Draw({
            edit: {
                featureGroup: drawnItems,
                edit: false,
                remove: false
            },
            draw: {
                polygon: true,
                polyline: true,
                rectangle: true,
                circle: false,
                marker: true
            }
        });
        this.map.addControl(drawControl);

        this.map.on(L.Draw.Event.CREATED, (event) => {
            const layer = event.layer;
            const type = event.layerType;
            let coordinates;

            if (type === 'polygon') {
                coordinates = layer.getLatLngs();
                this.viewModel.addPolygon(coordinates);
            } else if (type === 'polyline') {
                coordinates = layer.getLatLngs();
                this.viewModel.addPolyline(coordinates);
            } else if (type === 'marker') {
                const latLng = layer.getLatLng();
                this.viewModel.addMarker(latLng);
            }
            drawnItems.addLayer(layer);
        });
    }
}
