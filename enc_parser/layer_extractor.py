import json

#The LayerExtractor class is designed to extract features from a given layer in an OGR datasource.
#It reads the features from the layer and returns them in a structured format, including geometry and properties.
class LayerExtractor:

    # Initializes the LayerExtractor with a specific layer.
    # The layer should be an OGR layer object.
    def __init__(self, layer):
        self.layer = layer

    # Extracts features from the layer.
    # If feature_names is provided, only features containing those names will be included.
    def extract_features(self, feature_names=None):
        features = []
        self.layer.ResetReading()
        layer_name = self.layer.GetName() if self.layer else "Unknown Layer"
        for feature in self.layer:
            if feature_names is None or any(f in feature.keys() for f in feature_names):
                geometry = feature.GetGeometryRef()
                geometry_json = json.loads(geometry.ExportToJson()) if geometry else None
                properties = {k: feature.GetField(k) for k in feature.keys()}
                properties["layer"] = layer_name
                features.append({
                    'geometry': geometry_json,
                    'properties': properties
                })
        return features