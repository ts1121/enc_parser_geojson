import json

# The GeoJSONExporter class is designed to export features to a GeoJSON file.
# It takes a list of features and an output path, and writes the features in GeoJSON format.
# Each feature should contain a geometry and properties.
class GeoJSONExporter:

    # Initializes the GeoJSONExporter with features and an output path.
    # The features should be a list of dictionaries, each containing 'geometry' and 'properties
    def __init__(self, features, output_path):
        self.features = features
        self.output_path = output_path

    # Exports the features to a GeoJSON file.
    # The output file will be created or overwritten with the GeoJSON representation of the features.
    def export(self):
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": feat['geometry'],
                    "properties": feat['properties']
                }
                for feat in self.features
            ]
        }
        with open(self.output_path, "w") as f:
            json.dump(geojson, f, indent=2)
        